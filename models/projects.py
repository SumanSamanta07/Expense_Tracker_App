from config import db

class Projects(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(200), nullable=False)
    start_date = db.Column(db.String(100))
    end_date = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))