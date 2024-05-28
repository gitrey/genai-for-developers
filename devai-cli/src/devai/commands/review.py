# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import click
from devai.util.file_processor import format_files_as_string
from vertexai.generative_models import GenerativeModel, ChatSession
from google.cloud.aiplatform import telemetry
import os
from google.cloud import secretmanager
from google.api_core.exceptions import NotFound
from google.api_core.gapic_v1.client_info import ClientInfo
import logging


USER_AGENT = 'cloud-solutions/genai-for-developers-v1.0'

model_name="gemini-1.5-pro-preview-0514"


def ensure_env_variable(var_name):
    """Ensure an environment variable is set."""
    value = os.getenv(var_name)
    if value is None:
        raise EnvironmentError(f"Required environment variable '{var_name}' is not set.")
    return value

def get_prompt( secret_id: str) -> str:
    try:
        project_id = ensure_env_variable('PROJECT_ID')
        logging.info("PROJECT_ID:", project_id)

        client = secretmanager.SecretManagerServiceClient(
        client_info=ClientInfo(user_agent=USER_AGENT)
        )
        name = f"projects/{project_id}/secrets/{secret_id}/versions/latest"
        try:
            response = client.access_secret_version(name=name)
            payload = response.payload.data.decode("utf-8")
            logging.info(f"ID: {secret_id} in project {project_id}")
            return payload
        except NotFound:
            logging.info(f"ID not found: {secret_id} in project {project_id}")
            return None
    except EnvironmentError as e:
        logging.error(e)


# Uncomment after configuring JIRA and GitLab env variables - see README.md for details

# from devai.commands.jira import create_jira_issue
# from devai.commands.gitlab import create_gitlab_issue_comment

@click.command(name='code')
@click.option('-c', '--context', required=False, type=str, default="")
def code(context):
    """
    This function performs a code review using the Generative Model API.

    Args:
        context (str): The code to be reviewed.
    """
    #click.echo('code')
    
    source='''
            ### Context (code) ###
            {}

            '''
    qry = get_prompt('review_query')

    if qry is None:
        qry='''
            ### Instruction ###
            You are a senior software engineer and architect with over 20 years of experience, specializing in the language of the provided code snippet and adhering to clean code principles. You are meticulous, detail-oriented, and possess a deep understanding of software design and best practices.

            Your task is to perform a comprehensive code review of the provided code snippet. Evaluate the code with a focus on the following key areas:

            Correctness: Ensure the code functions as intended, is free of errors, and handles edge cases gracefully.
            Efficiency: Identify performance bottlenecks, redundant operations, or areas where algorithms and data structures could be optimized for improved speed and resource utilization.
            Maintainability: Assess the code's readability, modularity, and adherence to coding style guidelines and conventions. Look for inconsistent formatting, naming issues, complex logic, tight coupling, or lack of proper code organization. Suggest improvements to enhance clarity and maintainability.
            Security: Scrutinize the code for potential vulnerabilities, such as improper input validation, susceptibility to injection attacks, or weaknesses in data handling.
            Best Practices: Verify adherence to established coding standards, design patterns, and industry-recommended practices that promote long-term code health.

            ### Output Format ###
            Structure:  Organize your findings by class and method names. This provides clear context for the issues and aids in refactoring. 
            Tone: Frame your findings as constructive suggestions or open-ended questions. This encourages collaboration and avoids a purely critical tone. Examples:
            "Could we explore an alternative algorithm here to potentially improve performance?"
            "Would refactoring this logic into smaller functions enhance readability and maintainability?"
            Specificity:  Provide detailed explanations for each issue. This helps the original developer understand the reasoning and implement effective solutions.
            Prioritization: If possible, indicate the severity or potential impact of each issue (e.g., critical, high, medium, low). This helps prioritize fixes.
            No Issues:  If your review uncovers no significant areas for improvement, state "No major issues found. The code appears well-structured and adheres to good practices.

            Prioritize your findings based on their severity or potential impact (e.g., critical, high, medium, low).
            If no major issues are found, state: "No major issues found. The code appears well-structured and adheres to good practices."
            Frame your feedback as constructive suggestions or open-ended questions to foster collaboration and avoid a purely critical tone. Example: "Could we explore an alternative algorithm here to potentially improve performance?"

            ### Example Dialogue ###
            <query> First questions are to detect violations of coding style guidelines and conventions. Identify inconsistent formatting, naming conventions, indentation, comment placement, and other style-related issues. Provide suggestions or automatically fix the detected violations to maintain a consistent and readable codebase if this is a problem.
                    import "fmt"
                    
                    func main() {
                        name := "Alice"
                        greeting := fmt.Sprintf("Hello, %s!", name)
                        fmt.Println(greeting)
                    }
                    
                    
                    <response> [
                        {
                            "question": "Indentation",
                            "answer": "yes",
                            "description": "Code is consistently indented with spaces (as recommended by Effective Go)"
                        },
                        {
                            "question": "Variable Naming",
                            "answer": "yes",
                            "description": "Variables ("name", "greeting") use camelCase as recommended"
                        },
                        {
                            "question": "Line Length",
                            "answer": "yes",
                            "description": "Lines are within reasonable limits" 
                        },
                        {
                            "question": "Package Comments", 
                            "answer": "n/a",
                            "description": "This code snippet is too small for a package-level comment"
                        }
                    ]
                    
                    
                    <query> Identify common issues such as code smells, anti-patterns, potential bugs, performance bottlenecks, and security vulnerabilities. Offer actionable recommendations to address these issues and improve the overall quality of the code.
                    
                    "package main
                    
                    import (
                        "fmt"
                        "math/rand"
                        "time"
                    )
                    
                    // Global variable, potentially unnecessary 
                    var globalCounter int = 0 
                    
                    func main() {
                        items := []string{"apple", "banana", "orange"}
                    
                        // Very inefficient loop with nested loop for a simple search
                        for _, item := range items {
                            for _, search := range items {
                                if item == search {
                                    fmt.Println("Found:", item)
                                }
                            }
                        }
                    
                        // Sleep without clear reason, potential performance bottleneck
                        time.Sleep(5 * time.Second) 
                    
                        calculateAndPrint(10)
                    }
                    
                    // Potential divide-by-zero risk
                    func calculateAndPrint(input int) {
                        result := 100 / input 
                        fmt.Println(result)
                    }"
                    
                    <response> [
                        {
                            "question": "Global Variables",
                            "answer": "no",
                            "description": "Potential issue: Unnecessary use of the global variable 'globalCounter'. Consider passing values as arguments for better encapsulation." 
                        },
                        {
                            "question": "Algorithm Efficiency",
                            "answer": "no",
                            "description": "Highly inefficient search algorithm with an O(n^2) complexity. Consider using a map or a linear search for better performance, especially for larger datasets."
                        },
                        {
                            "question": "Performance Bottlenecks",
                            "answer": "no",
                            "description": "'time.Sleep' without justification introduces a potential performance slowdown. Remove it if the delay is unnecessary or provide context for its use."
                        },
                        {
                            "question": "Potential Bugs",
                            "answer": "no",
                            "description": "'calculateAndPrint' function has a divide-by-zero risk. Implement a check to prevent division by zero and handle the error appropriately."
                        },
                        { 
                            "question": "Code Readability",
                            "answer": "no",
                            "description": "Lack of comments hinders maintainability. Add comments to explain the purpose of functions and blocks of code."
                        } 
                    ]

            '''

    # Load files as text into source variable
    source=source.format(format_files_as_string(context))

    code_chat_model = GenerativeModel(model_name)
    with telemetry.tool_context_manager(USER_AGENT):
        code_chat = code_chat_model.start_chat()
        code_chat.send_message(qry)
        response = code_chat.send_message(source)

    click.echo(f"Response from Model: {response.text}")

    #create_jira_issue("Code Review Results", response.text)
    # create_gitlab_issue_comment(response.text)


@click.command()
@click.option('-c', '--context', required=False, type=str, default="")
def performance(context):
    """
    This function performs a performance review using the Generative Model API.

    Args:
        context (str): The code to be reviewed.
    """
    #click.echo('performance')
    
    source='''
            ### Context (code) ###
            {}

            '''
    qry = get_prompt('review_query')

    if qry is None:
        print("No review query found")
        qry='''
            ### Instruction ###
            You are a seasoned application performance tuning expert with deep knowledge of the nuances of various programming languages. Your task is to meticulously review the provided code snippet (please specify the language), focusing on identifying performance pitfalls and optimization opportunities. Tailor your analysis to the specific programming language used.
            If the code snippet involves a framework or library, consider performance implications related to that technology.
            If possible, suggest alternative approaches or code snippets that demonstrate potential optimizations.

            If the code's purpose is unclear, ask clarifying questions to better understand its intent.

            Pay close attention to the following aspects during your review:

            Inefficient Operations: Identify constructs known to be slow in the specific language, such as:

            Excessive string concatenation or manipulation.
            Unnecessary object creation or excessive memory allocation.
            Suboptimal loop structures or inefficient iteration patterns.
            Redundant computations or repeated function calls.
            I/O-bound Operations: Examine:

            File access and manipulation.
            Database queries and interactions.
            Network communication calls (e.g., APIs, web requests).
            Any blocking operations that could introduce latency.
            Algorithmic Complexity: Analyze algorithms for:

            Time complexity (e.g., O(n^2), O(n log n), O(n)).
            Space complexity (memory usage).
            Look for potential improvements using more efficient data structures or algorithms.
            Memory Management: Identify:

            Memory leaks (objects that are no longer needed but still consume memory).
            Memory bloat (unnecessarily large data structures or excessive memory usage).
            Data retention beyond its useful life.
            Concurrency (if applicable): Look for:

            Race conditions (where multiple threads access shared data simultaneously, leading to unpredictable results).
            Deadlocks (where two or more processes are waiting for each other to release resources, causing a standstill).
            Thread starvation (where a thread is unable to access resources it needs).


            ### Output Format ###
            Structure: Organize your findings by file and function/method names for clear context.
            Tone: Frame your findings as constructive suggestions or open-ended questions.
            Example: "Could we consider a more efficient way to handle string concatenation in this loop?"
            Specificity: Provide detailed explanations for each issue, referencing language-specific documentation or best practices where relevant.
            Prioritization: Indicate the severity or potential impact of each issue (e.g., critical, high, medium, low).
            No Issues: If no major performance issues are found, clearly state this.


            ### Example Dialogue ###

            User: (Provides Python code snippet)

            AI: (Provides output following the structured format, including language-specific insights, constructive suggestions, and prioritized recommendations)
            '''
    # Load files as text into source variable
    source=source.format(format_files_as_string(context))

    code_chat_model = GenerativeModel(model_name)
    with telemetry.tool_context_manager(USER_AGENT):
        code_chat = code_chat_model.start_chat()
        code_chat.send_message(qry)
        response = code_chat.send_message(source)

    click.echo(f"Response from Model: {response.text}")

    # create_jira_issue("Performance Review Results", response.text)
    # create_gitlab_issue_comment(response.text)

@click.command()
@click.option('-c', '--context', required=False, type=str, default="")
def security(context):
    """
    This function performs a security review using the Generative Model API.

    Args:
        context (str): The code to be reviewed.
    """
    #click.echo('simple security')

    source='''
            ### Context (code) ###: 
            {}
            '''
    
    qry = get_prompt('review_query')

    if qry is None:
        qry='''
            ### Instruction ###
            You are an experienced security programmer conducting a code review. Your task is to meticulously examine the provided code snippet (please specify the language) for potential security vulnerabilities. Tailor your review to the specific programming language and its security considerations. Consider the context of the code snippet (e.g., web application, backend service) to assess the relevance and impact of vulnerabilities. 

            Pay close attention to the following types of security vulnerabilities during your review:

            Input Validation and Sanitization:

            Identify instances where user-supplied input is not properly validated or sanitized before being used in:
            Database queries (SQL injection, NoSQL injection).
            Command execution (command injection).
            File system operations (path traversal).
            Displaying content (cross-site scripting - XSS).
            Authentication and Authorization:

            Examine how the code handles authentication (verifying user identity). Look for:
            Weak or easily guessable passwords.
            Hardcoded credentials.
            Missing or inadequate authentication mechanisms.
            Review authorization (granting access to resources). Ensure:
            Proper access controls are in place.
            Users are not able to escalate their privileges.
            Session Management:

            Evaluate how sessions are managed. Look for:
            Insecure cookie settings (e.g., missing "Secure" and "HttpOnly" flags).
            Session fixation vulnerabilities.
            Predictable session IDs.
            Inadequate session timeout enforcement.
            Data Protection:

            Assess how sensitive data is handled. Ensure:
            Data is encrypted in transit and at rest (if applicable).
            Appropriate hashing algorithms are used for passwords and sensitive data.
            Sensitive data is not unnecessarily logged or exposed.
            Error Handling and Logging:

            Examine error handling mechanisms. Make sure:
            Errors are handled gracefully and do not reveal sensitive information.
            Sufficient logging is in place to aid in debugging and incident response.
            Other Vulnerabilities:

            Be vigilant for additional issues such as:
            Cross-site request forgery (CSRF).
            Insecure direct object references (IDOR).
            Business logic flaws.
            Dependency vulnerabilities (outdated or insecure libraries/components).

            ### Output Format ###
            Structure: Group findings by file and function/method names for clarity.
            Issue: Provide a clear, concise description of each vulnerability found, including:
            Type of vulnerability (e.g., XSS, SQL injection).
            Location in the code (file, function/method).
            Potential impact.
            Recommendation: Offer detailed guidance on how to remediate the issue, including:
            Specific code changes or patterns to use.
            Relevant security libraries or frameworks to consider.
            References to secure coding guidelines or best practices.
            Prioritization: Indicate the severity of each issue (critical, high, medium, low).
            No Issues: If no significant vulnerabilities are found, clearly state this.

            Use clear, concise language, avoiding unnecessary jargon.
            Prioritize critical issues that could lead to serious security breaches. If the code's purpose is unclear, ask clarifying questions.
            If you identify an issue, but are unsure of the best solution, recommend further research or consultation with a security specialist


            ### Example Dialogue ###
            User: (Provides PHP code snippet)

            AI: (Provides output following the structured format, including language-specific insights and security recommendations relevant to PHP)
            '''
    # Load files as text into source variable
    source=source.format(format_files_as_string(context))
    
    code_chat_model = GenerativeModel(model_name)
    with telemetry.tool_context_manager(USER_AGENT):
        code_chat = code_chat_model.start_chat()
        code_chat.send_message(qry)
        response = code_chat.send_message(source)

    click.echo(f"Response from Model: {response.text}")

    # create_jira_issue("Security Review Results", response.text)
    # create_gitlab_issue_comment(response.text)

@click.command()
@click.option('-c', '--context', required=False, type=str, default="")
def testcoverage(context):
    """
    This function performs a test coverage review using the Generative Model API.

    Args:
        context (str): The code to be reviewed.
    """

    source='''
            ### Context (code) ###: 
            {}
            '''
    qry='''
        ### Instruction ###
        You are an experienced software engineer specializing in test coverage analysis and best practices. Given a code snippet (in any programming language) and its associated test suite (if available), your task is to perform a thorough assessment and provide actionable recommendations.

        ### Output Format ###
        Provide your findings in a structured format, listing:

        Files/Methods with Test Coverage: Clearly indicate which files and methods within the code snippet have corresponding unit tests.
        If possible, specify the names of the test classes and methods that provide coverage.

        Files/Methods Lacking Test Coverage: Clearly identify which files and methods within the code snippet do not have associated unit tests.
        Prioritize these based on their complexity, criticality, or potential risk of containing bugs.

        Overall Test Coverage Summary: Percentage of lines covered. Percentage of branches/conditions covered (if applicable to the language). Any notable coverage gaps at a high level.

        Detailed Coverage Breakdown:

        Files/Functions/Methods with Test Coverage:

        File name and function/method name.
        Corresponding test file and function/method name (if available).
        Coverage type (e.g., line, branch, condition, etc.).
        Files/Functions/Methods Lacking Test Coverage:

        File name and function/method name.
        Reason for prioritizing (complexity, criticality, risk).
        Specific test scenarios to consider.
        Recommendations for Improvement:

        Prioritized list of functions/methods/areas where new unit tests should be added.
        Guidance on test types to use (e.g., positive, negative, edge case, etc.).
        Tips on improving existing tests (if applicable).
        Additional Insights (Optional):

        Suggestions for refactoring code to make it more testable.
        Identification of potential code smells or areas prone to errors.
        Language-specific best practices for testing (if applicable).


        If no unit tests are present, clearly state this and emphasize the importance of adding them.
        If coverage is already comprehensive, acknowledge this and suggest ways to maintain or enhance the test suite.
        Tailor recommendations to the specific codebase, its context, and the programming language used.
        Use clear, concise language and avoid technical jargon where possible.
        Include code examples relevant to the programming language to illustrate recommendations.


        ### Example Dialogue ###

        User:  (Provides Java code snippet and test suite)

        AI: (Provides output following the structured format, including coverage metrics, detailed breakdown, prioritized recommendations, and additional insights, with examples relevant to Java)

        Key Changes

        Language Agnostic: Prompt is now open to any programming language, with the user specifying the language upfront.
        Flexible Output: Coverage metrics and test types are adjusted to be applicable to various languages (e.g., conditions instead of branches for languages that don't have explicit branching).
        Language-Specific Insights: Encourages the AI to offer best practices or insights specific to the language being analyzed.
        '''
    # Load files as text into source variable
    source=source.format(format_files_as_string(context))
    
    code_chat_model = GenerativeModel(model_name)
    with telemetry.tool_context_manager(USER_AGENT):
        code_chat = code_chat_model.start_chat()
        code_chat.send_message(qry)
        response = code_chat.send_message(source)

    click.echo(f"Response from Model: {response.text}")

    # create_jira_issue("Code Coverage Review Results", response.text)
    # create_gitlab_issue_comment(response.text)

@click.command()
@click.option('-c', '--context', required=False, type=str, default="")
def blockers(context):


    source='''
            ### Context (code) ###: 
            {}
            '''
    qry='''
        ### Instruction ###
        You are an experienced software engineer specializing in blocking. Analyze the code and check if there are components that are in the BLOCKERS list below.
        Provide explanation why you made the decision.

        BLOCKERS: "IBM MQ"

        
        ### Output Format ###
        Provide your findings in a structured JSON format using following JSON schema:
        {
        "onboarding_status": "",
        "blockers": []
        }

        JSON example when BLOCKER is detected:
        {
        "onboarding_status": "BLOCKED",
        "blockers": ['Jenkins']
        }

        JSON example when BLOCKER is NOT detected:
        {
        "onboarding_status": "APPROVED",
        "blockers": []
        }


        ### Example Dialogue ###
        '''
    # Load files as text into source variable
    source=source.format(format_files_as_string(context))
    
    code_chat_model = GenerativeModel(model_name)
    with telemetry.tool_context_manager(USER_AGENT):
        code_chat = code_chat_model.start_chat()
        code_chat.send_message(qry)
        response = code_chat.send_message(source)

    click.echo(f"Response from Model: {response.text}")

    # create_jira_issue("Blockers Review Results", response.text)
    # create_gitlab_issue_comment(response.text)


@click.group()
def review():
    """
    This group of commands provides code review functionalities.
    """
    pass

review.add_command(code)
review.add_command(performance)
review.add_command(security)
review.add_command(testcoverage)
review.add_command(blockers)