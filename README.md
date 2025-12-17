# Expenses-Tracker

## 🌟 Overview

The **Expenses-Tracker** is a simple yet powerful command-line interface (CLI) application built with Python to help users easily track and manage their personal expenses. Designed for efficiency, this tool allows you to log daily expenditures, categorize them, and generate insightful summaries directly from your terminal.

Data is securely saved to a local CSV file, giving you full control and portability over your financial records. Start monitoring your spending habits effectively and gain a clear view of where your money is going.

## 🚀 Features

The Expenses-Tracker provides a streamlined set of functionalities to manage your finances:

* **Add Expenses:** Quickly log new transactions with a date, description, amount, and category.
* **View All Expenses:** Display a list of all recorded expenses in a clean, tabular format.
* **Summarize by Category:** Generate a total summary of spending for each category (e.g., Groceries, Rent, Entertainment).
* **Data Persistence:** All expense data is saved to a local `expenses.csv` file, ensuring your records are safe across sessions.
* **User-Friendly Interface:** A simple, interactive command-line menu for easy navigation.

## 🛠️ Installation

Follow these steps to get the Expenses-Tracker running on your local machine.

### Prerequisites

You need to have **Python 3.x** installed on your system.

### Steps

1.  **Clone the Repository:**
    Use `git` to download the project files to your local machine.
    ```bash
    git clone [https://github.com/raymondoyondi/Expenses-Tracker.git](https://github.com/raymondoyondi/Expenses-Tracker.git)
    cd Expenses-Tracker
    ```

2.  **Install Dependencies:**
    This application requires the `pandas` library for robust data handling and CSV operations (assuming it uses pandas or similar for data processing).
    ```bash
    pip install pandas
    # or if you have a requirements.txt file:
    # pip install -r requirements.txt
    ```

3.  **Run the Application:**
    Execute the main Python script to launch the CLI.
    ```bash
    python expenses_tracker.py
    ```

## 📝 Usage

Once the application is running, you will be presented with a simple menu.

### Main Menu

1. Add new expense

2. View all expenses

3. Summarize expenses by category

4. Exit

### Command Examples

| Menu Option | Action | Example Input |
| :--- | :--- | :--- |
| **1. Add new expense** | Prompts for Date, Description, Amount, and Category. | `Date: 2023-10-27`, `Amount: 45.50`, `Category: Groceries` |
| **2. View all expenses** | Prints a table of all recorded transactions. | (Output a table) |
| **3. Summarize expenses** | Calculates and displays the total spent per category. | `Groceries: $150.25`, `Rent: $1200.00`, etc. |

## 🗄️ Data Persistence

All expense data is stored in the root directory of the project in a file named **`expenses.csv`**.

| Column Name | Description | Example Data |
| :--- | :--- | :--- |
| `Date` | The date the expense was incurred (YYYY-MM-DD). | `2023-10-27` |
| `Amount` | The monetary value of the expense. | `45.50` |
| `Category` | The spending category. | `Food` |
| `Description` | A brief note about the expense. | `Coffee and pastry` |

You can open this CSV file with any spreadsheet application (like Microsoft Excel, Google Sheets, or LibreOffice Calc) for deeper analysis or to backup your data.

## 🤝 Contributing

We welcome contributions to make the Expenses-Tracker even better! If you have suggestions for new features, bug reports, or want to contribute code, please follow these guidelines:

1.  **Fork** the repository.
2.  **Create** a new branch (`git checkout -b feature/AmazingFeature`).
3.  **Commit** your changes (`git commit -m 'Add some AmazingFeature'`).
4.  **Push** to the branch (`git push origin feature/AmazingFeature`).
5.  **Open** a Pull Request.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file (if available) for details.
