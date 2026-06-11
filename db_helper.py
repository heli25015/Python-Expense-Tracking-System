import mysql.connector
from contextlib import contextmanager
from logging_setup import setup_logger

logger = setup_logger("db_helper")

@contextmanager
def get_db_cursor(commit = False):
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "JulieHeli",
        database = "expense_manager"
    )

    if connection.is_connected():
        print("Connection Successful")
    else:
        print("Connection failed")

    cursor = connection.cursor(dictionary=True)
    yield cursor

    if commit:
        connection.commit()
    cursor.close()
    connection.close()



def fetch_expenses_for_date(expense_date):
    logger.info(f"fetch_expenses_for_date called with {expense_date}")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date = %s", (expense_date,))
        expenses = cursor.fetchall()
        for expense in expenses:
            print(expense)

        return expenses

def insert_expense(expense_date, amount, category, notes):
    logger.info(f"insert_expense called with date: {expense_date}, amount: {amount}, category: {category}, notes: {notes}")
    with get_db_cursor(commit= True) as cursor:
        cursor.execute(
            "INSERT INTO expenses (expense_date, amount, category, notes) VALUES (%s, %s, %s, %s)",
            (expense_date, amount, category, notes)
        )

def delete_expenses_for_date(expense_date):
    logger.info(f"delete_expenses_for_date called with {expense_date}")
    with get_db_cursor(commit = True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date = %s", (expense_date,))



# to make the graph grouped by category
def fetch_expense_summary(start_date, end_date):
    logger.info(f"fetch_expenses_summary called with {start_date} and {end_date}")

    with get_db_cursor() as cursor:
        cursor.execute(
            '''
            SELECT category, SUM(amount) as total 
            FROM expenses WHERE expense_date 
            BETWEEN %s and %s
            GROUP BY category;
            ''', (start_date, end_date)
        )
        data = cursor.fetchall()
        return data

#monthly analysis
def fetch_monthly_expense_summary():
    logger.info(f"fetch_monthly_expenses_summary")
    with get_db_cursor() as cursor:
        cursor.execute(
            '''
            SELECT
            MONTH(expense_date) AS month_number,
            MONTHNAME(expense_date) AS month_name,
            SUM(amount) AS total
            FROM expenses
            GROUP BY month_number, month_name
            ORDER BY month_number;
            '''
        )
        data = cursor.fetchall()
        return data


if __name__ == "__main__":

    expense = fetch_expenses_for_date("2024-08-01")
    print(expense)
    summary = fetch_expense_summary("2024-08-01", "2024-08-05")
    for record in summary:
       print(record)