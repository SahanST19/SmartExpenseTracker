# Smart Expense Tracker 💰

A modern, easy-to-use desktop application for tracking personal expenses. Built with Python, CustomTkinter, and SQLite.

## � Project Structure

The project is organized professionally, suitable for a GitHub repository:

- 🐍 **`main.py`**: The entry point of the application.
- 🐍 **`database.py`**: Handles all SQLite database operations.
- 📂 **`ui/`**: Contains all the user interface components.
    - 🐍 **`main_window.py`**: The main container.
    - 🐍 **`add_expense.py`**: Form for adding expenses.
    - 🐍 **`view_expenses.py`**: List view of history.
    - 🐍 **`dashboard.py`**: Visual charts.
- 📄 **`requirements.txt`**: List of dependencies.
- 📘 **`README.md`**: Documentation for the project.

## 🚀 Features Implemented

1. **Database Integration**: Automatically creates `expenses.db` to save your data.
2. **Add Expense**: A clean form to input date, category, amount, and description.
3. **View History**: A table view to see all past records.
4. **Dashboard**: A pie chart showing where your money goes (using Matplotlib).
5. **Modern UI**: Used `customtkinter` for a sleek, modern look.

## 🛠️ How to Run

1. **Open your terminal** in VS Code.
2. **Install the required libraries**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the app**:
   ```bash
   python main.py
   ```

## 📸 Screenshots
*(Add screenshots here after running the app)*

## 💻 Technologies Used
- **Python 3**
- **CustomTkinter**
- **SQLite**
- **Matplotlib**

## 🤝 Contributing
Feel free to fork this project and submit pull requests. Suggestions are welcome!

## 📄 License
This project is open source and available under the [MIT License](LICENSE).
