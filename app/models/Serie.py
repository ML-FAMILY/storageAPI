from utils.database import db

class Serie(db.Model):
    """Serie Class contains standard information for a Serie."""

    __tablename__ = "serie"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text)
    relative_path = db.Column(db.String, nullable=False, unique=True)
