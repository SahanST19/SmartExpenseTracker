import customtkinter as ctk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class DashboardFrame(ctk.CTkFrame):
    def __init__(self, master, db):
        super().__init__(master)
        self.db = db
        
        self.label = ctk.CTkLabel(self, text="Dashboard", font=("Arial", 24))
        self.label.pack(pady=10)

        self.chart_frame = ctk.CTkFrame(self)
        self.chart_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        self.update_chart()

    def update_chart(self):
        # Clear previous chart if any
        for widget in self.chart_frame.winfo_children():
            widget.destroy()

        data = self.db.get_summary_by_category()
        
        if not data:
            ctk.CTkLabel(self.chart_frame, text="No data available").pack(pady=50)
            return

        categories = [row[0] for row in data]
        amounts = [row[1] for row in data]

        # Create Matplotlib Figure
        fig = Figure(figsize=(6, 4), dpi=100)
        ax = fig.add_subplot(111)
        
        # Pie Chart
        ax.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=90)
        ax.set_title("Expenses by Category")

        # Embed in Tkinter
        canvas = FigureCanvasTkAgg(fig, master=self.chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)
