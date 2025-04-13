package com.example.Song.s_Serving.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class TableController {
    @GetMapping("/select-table")
    public String selectTablePage() {
        return "select-table";
    }
}
