"""
Database models for the Spoons app.

Currently contains User and EnergyLog models.
"""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    """
    Represents a user of the Spoons app.

    Attributes:
        id (int): Primary key
        username (str): Unique username
        email (str): User email
        created_at (datetime): Account creation timestamp
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    energy_logs = db.relationship("EnergyLog", backref="user", lazy=True)

class EnergyLog(db.Model):
    """
    Represents a single energy log entry for a user.

    Attributes:
        id (int): Primary key
        date (datetime): Date of the entry
        task (str): Task or activity name
        energy_spent (int): Energy spent (1-10 scale)
        notes (str): Optional additional notes
        user_id (int): Foreign key referencing User
    """
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    task = db.Column(db.String(140), nullable=False)
    energy_spent = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

