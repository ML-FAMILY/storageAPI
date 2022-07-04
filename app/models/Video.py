from utils.database import db


class Video(db.Model):
    """Video Class contains standard information for a Video."""

    __tablename__ = 'video'
    __mapper_args__ = {'polymorphic_identity': 'video'}

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text)
    duration = db.Column(db.Interval)
    release_year = db.Column(db.Integer)
    filename = db.Column(db.String, nullable=False)

    def __int__(self, title, description, duration, release_year, filename):
        self.title = title
        self.description = description
        self.duration = duration
        self.release_year = release_year
        self.filename
