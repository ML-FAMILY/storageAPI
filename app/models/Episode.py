from utils.database import db
from models.Video import Video

class Episode(Video):
    """Video Class contains standard information for a Video."""

    __tablename__ = "episode"

    __mapper_args__ = {
        "polymorphic_identity": "episode",
    }

    id = db.Column(db.Integer, db.ForeignKey("video.id"), primary_key=True)
    serie = db.Column(db.Integer, db.ForeignKey("serie.id"), nullable=False)

