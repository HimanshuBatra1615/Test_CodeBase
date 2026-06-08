package com.ecommerce;

import java.util.HashMap;
import java.util.Map;

/**
 * Service for managing user data.
 */
public class UserService {
    
    private Map<String, User> userDatabase;
    
    public UserService() {
        userDatabase = new HashMap<>();
        userDatabase.put("001", new User("001", "Alice", "alice@example.com"));
        userDatabase.put("002", new User("002", "Bob", "bob@example.com"));
    }
    
    /**
     * Fetch a user by ID.
     * BUG: Returns null instead of throwing an exception when user is not found.
     * Callers don't check for null, leading to NullPointerException.
     */
    public User getUser(String userId) {
        return userDatabase.get(userId);  // Returns null if not found!
    }
    
    public void addUser(User user) {
        userDatabase.put(user.getId(), user);
    }
}
