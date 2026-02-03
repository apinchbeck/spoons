"""
Unit tests for the Spoons MVP app.

Tests core functionality like routes and database models.
"""

import unittest
from app import create_app
from models.user import db

class BasicTests(unittest.TestCase):
    """Basic tests to ensure app starts and database initializes."""

    def setUp(self):
        """Set up test app and test database."""
        self.app = create_app()
        self.app.config["TESTING"] = True
        self.app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        """Clean up after each test."""
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_index_page(self):
        """Test the index page loads correctly."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

