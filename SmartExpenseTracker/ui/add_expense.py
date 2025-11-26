import customtkinter as ctk
from datetime import datetime
from tkinter import messagebox

class AddExpenseFrame(ctk.CTkFrame):
    def __init__(self, master, db):
        super().__init__(master)
        self.db = db

        self.label = ctk.CTkLabel(self, text="Add New Expense", font=("Arial", 24))
        self.label.pack(pady=20)

        # Date
        self.date_entry = ctk.CTkEntry(self, placeholder_text="Date (YYYY-MM-DD)")
        self.date_entry.pack(pady=10)
        self.date_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))

        # Category
        self.category_var = ctk.StringVar(value="Food")
        self.category_menu = ctk.CTkOptionMenu(self, variable=self.category_var, 
                                               values=["Food", "Transport", "Shopping", "Bills", "Entertainment", "Other"])
        self.category_menu.pack(pady=10)

        # Amount
        self.amount_entry = ctk.CTkEntry(self, placeholder_text="Amount")
        self.amount_entry.pack(pady=10)

        # Description
        self.desc_entry = ctk.CTkEntry(self, placeholder_text="Description")
        self.desc_entry.pack(pady=10)

        # Button
        self.add_btn = ctk.CTkButton(self, text="Add Expense", command=self.add_expense)
        self.add_btn.pack(pady=20)

    def add_expense(self):
        date = self.date_entry.get()
        category = self.category_var.get()
        amount = self.amount_entry.get()
        description = self.desc_entry.get()

        if not amount:
            messagebox.showerror("Error", "Amount is required!")
            return

        try:
            amount = float(amount)
            self.db.add_expense(date, category, amount, description)
            messagebox.showinfo("Success", "Expense added successfully!")
            self.amount_entry.delete(0, 'end')
            self.desc_entry.delete(0, 'end')
        except ValueError:
            messagebox.showerror("Error", "Amount must be a number!")
