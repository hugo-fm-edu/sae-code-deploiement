from flask import Blueprint, request, jsonify
from extensions import db
from models.etudiant import Etudiant

etudiant_bp = Blueprint("etudiant_bp", __name__)

@etudiant_bp.get("/")
def get_all():
    return jsonify([e.to_json() for e in Etudiant.query.all()])

@etudiant_bp.get("/<int:id>")
def get_one(id):
    e = Etudiant.query.get_or_404(id)
    return jsonify(e.to_json())

@etudiant_bp.post("/")
def create():
    data = request.json
    e = Etudiant(nom=data.get("nom"), moyenne=data.get("moyenne"))
    db.session.add(e)
    db.session.commit()
    return jsonify(e.to_json()), 201


@etudiant_bp.put("/<int:id>")
def update(id):
    e = Etudiant.query.get_or_404(id)
    data = request.json

    e.nom = data.get("nom", e.nom)
    e.moyenne = data.get("moyenne", e.moyenne)

    db.session.commit()
    return jsonify(e.to_json())

@etudiant_bp.delete("/<int:id>")
def delete(id):
    e = Etudiant.query.get_or_404(id)
    db.session.delete(e)
    db.session.commit()
    return jsonify({"message": "Étudiant supprimé"})
