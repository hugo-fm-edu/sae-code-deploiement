from flask import Flask, jsonify, request

# Créer l'application flask
app = Flask(__name__)

# Dans un premier temps, on ne va pas utiliser de bases de données
# Sauvegarder les étudiants dans une liste :

students = [
    {"id":1, "prenom":"Samir", "age":31},
    {"id":2, "prenom":"Safa", "age":22},
]

# Définir la racine de l'API :

@app.route('/')
def home():
    return "C'est cool REST !"

# Test de code HTML

@app.route('/message')
def message():
    return "<h1>Bonjour tout le monde !</h1>"

# Test d'une page HTML

@app.route('/html')
def pagehtml():
    return """
<html>
<head>
    <title>Ma page web depuis API REST</title>
<style>
h1 {
    text-align: center;
}
#carreRouge {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 200px;
    height: 200px;
    background-color: red;
}
</style>
</head>
<body>
    <h1>Voici un exemple de page HTML depuis une API REST (Flask)</h1>
    <div id="carreRouge"><p>Je suis un carré rouge</p></div>
</body>
</html>
"""

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

# Ajouter un étudiant, c'est une nouvelle ressource (via POST) :

@app.route('/students', methods=['POST'])
def add_student():
    new_student = request.get_json() # récupérer l'object
    new_student['id'] = len(students)+1 # Assigner un ID automatique
    students.append(new_student)
    return jsonify(new_student), 201

# Afficher un étudiant sachant son identifiant :

@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = next((s for s in students if s['id']==id), None)
    if student:
        return jsonify(student)
    return jsonify({"erreur": "L'étudiant n'est pas trouvé"}), 404

# Mise à jour d'un étudiant :

@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    student = next((s for s in students if s['id']==id), None)
    if not student:
        return jsonify({"erreur": "not exist"}), 404
    
    data = request.get_json()
    student.update(data)
    return jsonify(student)

# Supprimer un étudiant :

@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    global students
    students = [s for s in students if s['id'] !=id]
    return jsonify({"message": "OK"}), 200

if __name__ == '__main__':
    app.run(debug=True)