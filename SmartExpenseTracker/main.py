import customtkinter as ctk
from ui.main_window import MainWindow
from database import Database

def main():
    # Initialize Database
    db = Database()
    
    # Setup App
    ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
    ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

    app = MainWindow(db)
    app.mainloop()

if __name__ == "__main__":
    main()
