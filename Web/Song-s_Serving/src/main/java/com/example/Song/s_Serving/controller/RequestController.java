package com.example.Song.s_Serving.controller;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.client.RestTemplate;

import java.util.HashMap;
import java.util.Map;

@Controller
public class RequestController {

    @Value("${flask.url.request-items}")
    private String flaskRequestUrl;

    @GetMapping("/request-items")
    public String requestItemsPage(@RequestParam("table") int table, Model model) {
        model.addAttribute("table", table);
        return "request-items";
    }

    @PostMapping("/send-request")
    public String sendRequest(@RequestParam Map<String, String> params){
        int table = Integer.parseInt(params.get("table"));
        int water = Integer.parseInt(params.get("water"));
        int coke = Integer.parseInt(params.get("coke"));
        int tissue = Integer.parseInt(params.get("tissue"));
        int spoon = Integer.parseInt(params.get("spoon"));
        boolean callStaff = params.containsKey("callStaff");

        RestTemplate restTemplate = new RestTemplate();
        Map<String, Object> body = new HashMap<>();
        Map<String, Integer> items = new HashMap<>();

        body.put("table", table);
        items.put("water", water);
        items.put("coke", coke);
        items.put("tissue", tissue);
        items.put("spoon", spoon);
        body.put("items", items);
        body.put("callStaff", callStaff);

        restTemplate.postForObject(flaskRequestUrl, body, String.class);

        return "redirect:/";
    }
}
