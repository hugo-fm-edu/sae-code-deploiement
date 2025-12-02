# Faire un programme Java pour faire un simple print et le déployé sur docker

#Etape 1 : Compilation
FROM eclipse-temurin:21-jdk AS build

WORKDIR /app

#Mauvaise pratique : le programme est directement dans l'image et donc non-persistante
#Il vaut mieux créer un volume dans lequel se trouve le .java

#Copier le code source
COPY Hello.java .

#Compiler le programme
RUN javac Hello.java

#Etape 2 : image finale minimaliste
FROM eclipse-temurin:21-jre

WORKDIR /app

#Copier le fichier compilé
COPY --from=build /app/Hello.class .

#Commande exécutée au lancement du conteneur
CMD ["java", "Hello"]

#docker build -t mon-app .
#docker run mon-app