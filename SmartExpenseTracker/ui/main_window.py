import customtkinter as ctk
from ui.add_expense import AddExpenseFrame
from ui.view_expenses import ViewExpensesFrame
from ui.dashboard import DashboardFrame

class MainWindow(ctk.CTk):
    def __init__(self, db):
        super().__init__()
        self.db = db
        
        self.title("Smart Expense Tracker")
        self.geometry("900x600")

        # Grid Layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Sidebar
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        
        self.logo_label = ctk.CTkLabel(self.sidebar, text="Expense Tracker", font=("Arial", 20, "bold"))
        self.logo_label.pack(pady=20)

        self.btn_add = ctk.CTkButton(self.sidebar, text="Add Expense", command=self.show_add_expense)
        self.btn_add.pack(pady=10, padx=20)

        self.btn_view = ctk.CTkButton(self.sidebar, text="View History", command=self.show_view_expenses)
        self.btn_view.pack(pady=10, padx=20)

        self.btn_dash = ctk.CTkButton(self.sidebar, text="Dashboard", command=self.show_dashboard)
        self.btn_dash.pack(pady=10, padx=20)

        # Main Content Area
        self.content_frame = ctk.CTkFrame(self, corner_radius=0)
        self.content_frame.grid(row=0, column=1, sticky="nsew")

        # Initialize Frames
        self.add_expense_frame = AddExpenseFrame(self.content_frame, self.db)
        self.view_expenses_frame = ViewExpensesFrame(self.content_frame, self.db)
        self.dashboard_frame = DashboardFrame(self.content_frame, self.db)

        self.show_dashboard()

    def show_add_expense(self):
        self.forget_frames()
        self.add_expense_frame.pack(fill="both", expand=True)

    def show_view_expenses(self):
        self.forget_frames()
        self.view_expenses_frame.load_data()
        self.view_expenses_frame.pack(fill="both", expand=True)

    def show_dashboard(self):
        self.forget_frames()
        self.dashboard_frame.update_chart() # Refresh data
        self.dashboard_frame.pack(fill="both", expand=True)

    def forget_frames(self):
        self.add_expense_frame.pack_forget()
        self.view_expenses_frame.pack_forget()
        self.dashboard_frame.pack_forget()
