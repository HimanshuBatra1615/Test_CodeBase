package com.ecommerce;

import java.util.List;
import java.util.ArrayList;

/**
 * Processes orders for users.
 */
public class OrderProcessor {
    
    private UserService userService;
    
    public OrderProcessor(UserService userService) {
        this.userService = userService;
    }
    
    /**
     * Process an order for a given user.
     * BUG: Does not check if user is null before calling user.getName().
     */
    public void processUserOrder(String userId, List<String> itemIds) {
        User user = userService.getUser(userId);
        
        // BUG: user can be null here if userId doesn't exist!
        System.out.println("Processing order for: " + user.getName());
        
        double total = calculateTotal(itemIds);
        
        // BUG: Doesn't handle case where total is 0 (empty items)
        chargeUser(user, total);
    }
    
    private double calculateTotal(List<String> itemIds) {
        double total = 0.0;
        for (String id : itemIds) {
            total += getItemPrice(id);
        }
        return total;
    }
    
    private double getItemPrice(String itemId) {
        // Simulated price lookup
        switch (itemId) {
            case "ITEM-A": return 29.99;
            case "ITEM-B": return 49.99;
            default:
                throw new IllegalArgumentException("Unknown item: " + itemId);
        }
    }
    
    private void chargeUser(User user, double amount) {
        // BUG: NullPointerException if user is null — calls user.getEmail()
        System.out.println("Charging " + amount + " to " + user.getEmail());
    }
}
