import customtkinter as ctk
from tkinter import ttk

class ViewExpensesFrame(ctk.CTkFrame):
    def __init__(self, master, db):
        super().__init__(master)
        self.db = db

        self.label = ctk.CTkLabel(self, text="Expense History", font=("Arial", 24))
        self.label.pack(pady=10)

        # Create Treeview
        columns = ("id", "date", "category", "amount", "description")
        self.tree = ttk.Treeview(self, columns=columns, show="headings")
        
        self.tree.heading("id", text="ID")
        self.tree.heading("date", text="Date")
        self.tree.heading("category", text="Category")
        self.tree.heading("amount", text="Amount")
        self.tree.heading("description", text="Description")

        self.tree.column("id", width=30)
        self.tree.column("date", width=100)
        self.tree.column("category", width=100)
        self.tree.column("amount", width=80)
        self.tree.column("description", width=200)

        self.tree.pack(fill="both", expand=True, padx=20, pady=20)

        # Refresh Button
        self.refresh_btn = ctk.CTkButton(self, text="Refresh", command=self.load_data)
        self.refresh_btn.pack(pady=10)

        self.load_data()

    def load_data(self):
        # Clear existing data
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Fetch from DB
        rows = self.db.get_expenses()
        for row in rows:
            self.tree.insert("", "end", values=row)
