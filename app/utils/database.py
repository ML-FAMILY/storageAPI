from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



def create_tables(app):

    with app.app_context():
        from models import Video, Serie, Episode
        db.create_all()