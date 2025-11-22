package com.example.spring;

// JPA (Java Persistence API) pour les annotations
// H2 en mémoire

import org.springframework.web.bind.annotation.*;
import java.util.ArrayList;

@RestController
public class MyApi {

    public static ArrayList<Etudiant> liste = new ArrayList<>();

    static {
        liste.add(new Etudiant(0, "A", 19));
        liste.add(new Etudiant(1, "B", 18));
        liste.add(new Etudiant(2, "C", 17));
        liste.add(new Etudiant(3, "D", 16));
    }

    @GetMapping(value = "/liste")
    public ArrayList<Etudiant> getAllEtudiant() {
        return liste;
    }

    @GetMapping(value = "/getEtudiant")
    public Etudiant getEtudiant(int identifiant) {
        return liste.get(identifiant);
    }

    @PostMapping(value = "/addEtudiant")
    public Etudiant addEtudiant(Etudiant etudiant) {
        liste.add(etudiant);
        return etudiant;
    }

    @PutMapping(value = "/modifier")
    public void modifierEtudiant(int identifiant, String nom) {
        liste.get(identifiant).setNom(nom);
    }

    @DeleteMapping(value = "/delete")
    public void supprimerEtudiant(int identifiant) {
        liste.remove(identifiant);
    }

    // Get : renvoier une ressource
    // Post : créer une nouvelle ressource
    // Put : modifier une ressource
    // Delete : supprimer une ressource

    @GetMapping(value = "/b")
    public String bonjour(){
        return "Bonjour !";
    }

    @GetMapping(value = "/bn")
    public String bonsoir(){
        return "Bonsoir";
    }

    @GetMapping(value = "/etudiant")
    public Etudiant getEtudiant(){
        return new Etudiant(1, "A", 19);
    }

    @GetMapping(value = "/somme")
    public double somme(double a, double b){
        return a+b;
    }
}
