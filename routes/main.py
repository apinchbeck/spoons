"""
Main blueprint for Spoons routes.

Handles core routes like dashboard, logging energy, and viewing history.
"""

from flask import Blueprint, render_template, request, redirect, url_for
from models.user import db, EnergyLog

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def index():
    """
    Dashboard/homepage route.

    Displays recent energy logs and summary info.
    """
    logs = EnergyLog.query.order_by(EnergyLog.date.desc()).all()
    return render_template("index.html", logs=logs)

@main_bp.route("/log", methods=["GET", "POST"])
def log():
    """
    Route for logging a new energy/task entry.

    GET: Show the log entry form.
    POST: Process form submission and save a new EnergyLog.
    """
    if request.method == "POST":
        task = request.form.get("task")
        energy = request.form.get("energy")
        notes = request.form.get("notes")
        # TODO: Add current user reference when auth is implemented
        new_log = EnergyLog(task=task, energy_spent=int(energy), notes=notes, user_id=1)
        db.session.add(new_log)
        db.session.commit()
        return redirect(url_for("main.index"))
    return render_template("log.html")

