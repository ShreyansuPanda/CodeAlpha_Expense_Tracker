# Code Alpha Task 2: Expense Tracker

An expense tracker application built with Python and Tkinter for the GUI, and SQLite3 for the database. This application allows users to track their expenses, update and delete records, and view the total balance.

## Features

- Add expense records with item name, price, and purchase date.
- Update existing expense records.
- Delete individual expense records or all records.
- View total expenses and remaining balance.
- User-friendly graphical interface using Tkinter.

## Requirements

- Python 3.x
- Tkinter (usually included with Python)
- SQLite3 (usually included with Python)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/expense-tracker.git
    cd expense-tracker
    ```

2. Install required packages (if any). Since Tkinter and SQLite3 are part of the standard Python library, no additional packages should be required.

## Usage

1. Run the application:
    ```sh
    python main.py
    ```

2. The main window of the application will appear. Here are the available functionalities:

    - **Add Record:** Enter the item name, item price, and purchase date, then click "Save Record" to add it to the database.
    - **Update Record:** Select a record from the list, modify the details, and click "Update" to save the changes.
    - **Delete Record:** Select a record from the list and click "Delete" to remove it from the database.
    - **Delete All Records:** Click "Delete All" to remove all records from the database.
    - **View Total Balance:** Click "Total Balance" to view the total expenses and remaining balance.

## Code Structure

- `mydb.py`: Contains the `Database` class which handles all database operations (insert, fetch, update, delete).
- `main.py`: Contains the Tkinter GUI implementation and connects GUI actions to database operations.

## Database Schema

The SQLite database contains a single table `expense_record` with the following columns:

- `item_name`: Text, name of the expense item.
- `item_price`: Float, price of the expense item.
- `purchase_date`: Date, date of purchase.

## Functions

### mydb.py

- `__init__(self, db)`: Initializes the database connection and creates the table if it does not exist.
- `fetchrecord(self, query)`: Executes a fetch query and returns all rows.
- `insertrecords(self, item_name, item_price, purchase_date)`: Inserts a new record into the database.
- `removerecord(self, rwid)`: Deletes a record with the specified row ID.
- `updaterecord(self, item_name, item_price, purchase_date, rid)`: Updates a record with the specified row ID.
- `delete_all_records(self)`: Deletes all records from the database.

### main.py

- `ask_total_balance()`: Prompts the user to enter their total balance at startup.
- `saverecord()`: Inserts a new record into the database and refreshes the data in the GUI.
- `setdate()`: Sets the purchase date to the current date.
- `clearentries()`: Clears the input fields.
- `fetch_records()`: Fetches all records from the database and displays them in the GUI.
- `select_record(event)`: Selects a record from the list for updating or deleting.
- `update_record()`: Updates the selected record in the database and refreshes the data in the GUI.
- `deleteRow()`: Deletes the selected record from the database and refreshes the data in the GUI.
- `delete_all_records()`: Deletes all records from the database and refreshes the data in the GUI.
- `totalbalance()`: Calculates and displays the total expenses and remaining balance.
- `refreshData()`: Refreshes the data displayed in the GUI.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

