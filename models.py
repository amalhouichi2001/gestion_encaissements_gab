from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Encaissement(db.Model):
    __tablename__ = "encaissements"

    id = db.Column(db.Integer, primary_key=True)
    date_encaissement = db.Column(db.Date, nullable=False)
    montant = db.Column(db.Numeric(10, 2), nullable=False)
    moyen_paiement = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "date_encaissement": self.date_encaissement.strftime("%Y-%m-%d"),
            "montant": float(self.montant),
            "moyen_paiement": self.moyen_paiement
        }
