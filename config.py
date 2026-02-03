"""
Configuration settings for the Spoons app.

Includes database URI, secret keys, and other environment-dependent settings.
"""

import os

class Config:
    """Base configuration for the app."""
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev_secret_key")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///spoons.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

