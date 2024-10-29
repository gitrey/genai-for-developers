```java
package com.example.demo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Optional;

@RestController
@RequestMapping("/api/accounts")
public class AccountController {

    @Autowired
    private AccountRepository accountRepository;

    @GetMapping("/{id}")
    public ResponseEntity<Account> getAccount(@PathVariable Long id) {
        Optional<Account> account = accountRepository.findById(id);
        return account.map(ResponseEntity::ok).orElseGet(() -> ResponseEntity.notFound().build());
    }

    @PostMapping
    public ResponseEntity<Account> createAccount(@RequestBody Account account) {
        Account savedAccount = accountRepository.save(account);
        return new ResponseEntity<>(savedAccount, HttpStatus.CREATED);
    }
    
    @PutMapping("/{id}/balance")
    public ResponseEntity<Account> updateAccountBalance(@PathVariable Long id, @RequestBody Account updatedAccount) {
        Optional<Account> optionalAccount = accountRepository.findById(id);
        if (optionalAccount.isPresent()) {
            Account account = optionalAccount.get();
            account.setBalance(updatedAccount.getBalance());
            Account updated = accountRepository.save(account);
            return ResponseEntity.ok(updated);
        } else {
            return ResponseEntity.notFound().build();
        }
    }
}


package com.example.demo;

import javax.persistence.*;

@Entity
public class Account {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private double balance;

    public Account() {}

    public Account(double balance) {
        this.balance = balance;
    }


    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public double getBalance() {
        return balance;
    }

    public void setBalance(double balance) {
        this.balance = balance;
    }
}

package com.example.demo;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface AccountRepository extends JpaRepository<Account, Long> {
}
```
