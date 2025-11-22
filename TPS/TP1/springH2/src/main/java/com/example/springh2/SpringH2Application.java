package com.example.springh2;

import com.example.springh2.entities.Adherent;
import com.example.springh2.repository.AdherentRepository;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
public class SpringH2Application {

    public static void main(String[] args) {
        SpringApplication.run(SpringH2Application.class, args);
    }

    @Bean
    CommandLineRunner runner(AdherentRepository repository){
        return args -> {
            repository.save(new Adherent(null, "Dupont", "Jean", 29));
            repository.save(new Adherent(null, "Martin", "Marie", 35));
            repository.save(new Adherent(null, "Durand", "Pierre", 42));
            repository.save(new Adherent(null, "Bernard", "Sophie", 28));
        };
    }
}
