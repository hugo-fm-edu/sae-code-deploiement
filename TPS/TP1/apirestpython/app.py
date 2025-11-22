from flask import Flask
from config import Config
from extensions import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from resources.etudiant_api import etudiant_bp
    app.register_blueprint(etudiant_bp, url_prefix="/api/etudiants")

    with app.app_context():
        db.create_all()

        from models.etudiant import Etudiant
        if Etudiant.query.count() == 0:
            e1 = Etudiant(nom="Dupont", prenom="Alice", email="alice@example.com")
            e2 = Etudiant(nom="Martin", prenom="Bob", email="bob@example.com")
            db.session.add_all([e1, e2])
            db.session.commit()

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5001)
