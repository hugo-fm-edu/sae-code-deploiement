from extensions import db

class Etudiant(db.Model):
    __tablename__ = "etudiants"

    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    moyenne = db.Column(db.Integer, nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "moyenne": self.moyenne
        }
