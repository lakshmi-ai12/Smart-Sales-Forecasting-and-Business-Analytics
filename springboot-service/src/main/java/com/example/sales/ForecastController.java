package com.example.sales;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.Map;

@RestController
public class ForecastController {

    @GetMapping("/api/forecast")
    public Map<String, Object> forecast() {
        return Map.of(
            "status", "ready",
            "message", "Run the Python ML service to generate the forecast and connect its result here."
        );
    }
}
