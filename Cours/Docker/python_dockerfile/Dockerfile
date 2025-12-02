#1. On utilise une image Python officielle
FROM python:3.12-slim

#2. On définit le répertoire de travail
WORKDIR /app

#3. On installe Flask
RUN pip install flask

#4. On copie le fichier app.py dans l'image
COPY app.py .

#5. On documente le port utilisé
EXPOSE 5000

#6. On définit la commande qui démarre l'application
CMD ["python", "app.py"]

#docker build -t mon-app .
#docker run -p 4900:5000 mon-app

#Le fichier app.py vient du tuto API REST réalisé précédemment.
#Cela ne va pas fonctionné car on n'a pas accès directement au conteneur.
#Il faut modifier le app.run() de la manière suivante pour qu'il est le même port que le EXPOSE:
#app.run(host='0.0.0.0', port=5000, debug=True)