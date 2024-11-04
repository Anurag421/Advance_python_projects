'''5. Expense Tracker
Problem Statement: Build an expense tracker that categorizes and analyzes expenses.
Steps:
Define Expense and ExpenseManager classes with attributes like category, amount, and date.
Implement methods to add, view, and summarize expenses by category or date.
Integrate basic statistics for monthly or weekly spending.'''

from datetime import datetime, timedelta
from collections import defaultdict

class Expense:
    def __init__(self, amount, category, date):
        self.amount = amount
        self.category = category
        self.date = datetime.strptime(date, "%Y-%m-%d")


class ExpenseManager:
    def __init__(self):
        self.expenses = [] #created list to store all expenses

    def add_expense(self, amount, category, date):
        '''Adding expenses to the tracker.'''
        new_expense = Expense(amount, category, date)
        self.expenses.append(new_expense)
        print(f"Added expense: ${amount} for {category} on {date}.")

    def view_expenses(self):
        '''Viewing all expenses details.'''
        if not self.expenses:
            print("No expense to show.")
        for expense in self.expenses:
            print(f"Amount: ${expense.amount}, Category: {expense.category}, Date: {expense.date.strftime('%Y-%m-%d')}")
    
    def summarize_by_category(self):
        '''Summarize total expenses by category.'''
        category_totals = defaultdict(float)
        for expense in self.expenses:
            category_totals[expense.category] += expense.amount
        print("\nExpense Summary by category:")
        for category, total in category_totals.items():
            print(f"{category}: ${total}")
    
    def summarize_by_month(self):
        '''Summarizing expenses by month.'''
        monthly_totals = defaultdict(float)
        for expense in self.expenses:
            month = expense.date.strftime("%Y-%m")
            monthly_totals[month] += expense.amount

        print("\nExpense Summary by Month:")
        for month, total in monthly_totals.items():
            print(f"{month}: ${total}")

    
    def weekly_statistics(self):
        '''Calculate and display total weekly expenses.'''
        weekly_totals = defaultdict(float)
        for expense in self.expenses:
            week_start = expense.date - timedelta(days=expense.date.weekday())
            weekly_totals[week_start.strftime("%Y-%m-%d")] +=expense.amount
        print("\nweekly Expense Statistics:")
        for week_start, total in weekly_totals.items():
            print(f"week starting {week_start}: ${total}")


manager = ExpenseManager()
manager.add_expense(50, "Groceries", "2024-10-01")
manager.add_expense(20, "Transport", "2024-10-02")
manager.add_expense(15, "Groceries", "2024-10-08")
manager.add_expense(100, "Entertainment", "2024-10-15")
manager.view_expenses()
manager.summarize_by_category()
manager.summarize_by_month()
manager.weekly_statistics()
