package com.example.springh2.entities;

// Hibernate, une des implémentations de JPA

import jakarta.persistence.*;

@Entity
public class Adherent {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Long id;
    private String nom;
    private String adresse;
    private int age;

    public Adherent() {
    }

    public Adherent(Long id, String nom, String adresse, int age) {
        this.id = id;
        this.nom = nom;
        this.adresse = adresse;
        this.age = age;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public String getAdresse() {
        return adresse;
    }

    public void setAdresse(String adresse) {
        this.adresse = adresse;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }
}
