package com.ecommerce;

import java.util.List;
import java.util.ArrayList;

/**
 * Main application entry point for the E-Commerce backend.
 */
public class App {
    
    public static void main(String[] args) {
        System.out.println("Starting E-Commerce Backend v3.2.1");
        
        UserService userService = new UserService();
        OrderProcessor processor = new OrderProcessor(userService);
        
        // Simulate incoming request with user ID
        try {
            // BUG: user ID "999" doesn't exist, causes NullPointerException downstream
            processor.processUserOrder("999", List.of("ITEM-A", "ITEM-B"));
        } catch (Exception e) {
            System.err.println("Fatal error: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
