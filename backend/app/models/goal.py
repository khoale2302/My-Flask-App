
from ..extensions import db


class Goal(db.Model):
    __tablename__ = "goals"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(150), nullable=False)

    description = db.Column(db.Text, nullable=True)

    deadline = db.Column(db.Date, nullable=True)

    status = db.Column(
        db.String(30),
        default="pending"
    )

    def __repr__(self):
        return f"<Goal {self.title}>"
