import sqlite3
from datetime import datetime

class Database:
    """
    Handles all database interactions for the application.
    Uses SQLite to store expense data.
    """
    def __init__(self, db_name="expenses.db"):
        """Initialize database connection and create tables if they don't exist."""
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """Create the expenses table with necessary columns."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                category TEXT NOT NULL,
                amount REAL NOT NULL,
                description TEXT
            )
        """)
        self.conn.commit()

    def add_expense(self, date, category, amount, description):
        """Add a new expense record to the database."""
        self.cursor.execute("""
            INSERT INTO expenses (date, category, amount, description)
            VALUES (?, ?, ?, ?)
        """, (date, category, amount, description))
        self.conn.commit()

    def get_expenses(self):
        """Retrieve all expenses ordered by date (newest first)."""
        self.cursor.execute("SELECT * FROM expenses ORDER BY date DESC")
        return self.cursor.fetchall()

    def get_summary_by_category(self):
        """Calculate total expenses per category for the dashboard."""
        self.cursor.execute("""
            SELECT category, SUM(amount) 
            FROM expenses 
            GROUP BY category
        """)
        return self.cursor.fetchall()

    def close(self):
        """Close the database connection."""
        self.conn.close()
