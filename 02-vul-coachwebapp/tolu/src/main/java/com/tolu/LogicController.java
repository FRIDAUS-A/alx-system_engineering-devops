package com.tolu;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
//@RequestMapping("login_form")
public class LoginController{

    @PostMapping("/validate")
    public String processLogin(@RequestParam("username"), String name, 
    @RequestParam("password") String pass, Model model) {
        model.addAttribute("name", name);
        model.addAttribute("pass", pass);

    return "result";

    }
}
