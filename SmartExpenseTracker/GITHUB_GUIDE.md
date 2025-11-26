# How to Upload to GitHub 🚀

Follow these simple steps to upload your **Smart Expense Tracker** to GitHub.

## Step 1: Create a Repository on GitHub
1.  Log in to your [GitHub account](https://github.com/).
2.  Click the **+** icon in the top right and select **New repository**.
3.  Name it `SmartExpenseTracker`.
4.  **Description** (Optional): Copy and paste one of these:
    > "A modern Smart Expense Tracker built with Python, CustomTkinter, and SQLite."
    > "Desktop application to track daily expenses with data visualization."
5.  **Do not** check "Add a README file" (we already have one).
6.  Click **Create repository**.

## Step 2: Open Terminal
1.  In VS Code, make sure you are in the `SmartExpenseTracker` folder.
2.  Open the terminal (`Ctrl + ` ` `).

## Step 3: Run these Commands
Copy and paste these commands one by one into the terminal:

1.  **Initialize Git**:
    ```bash
    git init
    ```

2.  **Add all files**:
    ```bash
    git add .
    ```

3.  **Commit changes**:
    ```bash
    git commit -m "Initial commit - Smart Expense Tracker App"
    ```

4.  **Rename branch to main**:
    ```bash
    git branch -M main
    ```

5.  **Connect to GitHub**:
    ```bash
    git remote add origin https://github.com/SahanST19/SmartExpenseTracker.git
    ```

6.  **Upload (Push)**:
    ```bash
    git push -u origin main
    ```

## 🎉 Done!
Refresh your GitHub page, and you will see your code there.
