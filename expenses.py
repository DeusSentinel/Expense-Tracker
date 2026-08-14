import csv
from tabulate import tabulate
from datetime import date

T_Amount = 0 
# To Write data collected from user into a CSV file
# "While True (....)" - To create a loop that only exits if there is no ValueError
def create_expense_file():
    headers = ["Date", "Expenses", "Amount"]
    while True:
        try:
            daily_expenses = int(input("Please enter your amount of daily expenses: "))
            if daily_expenses <= 0:
                display_expenses()
            break
        except ValueError:
            print("Invalid input. Please try again.")
    data = []
    for i in range(daily_expenses):
        Date = date.today()
        Expense = input("\nExpense: ")
        while True:
            try:
                Amount = float(input("Amount: "))
                T_Amount = T_Amount + Amount
                break
            except ValueError:
                print("Please enter a valid amount in numeral.")
    data.append(Date, Expense, f"$ {Amount:.2f}")
    with open('expense.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)
  
#TO Open/ Read the Data in the CVS file
# mode = r - to read/open
# encoding = utf-8  - soemthing to do with reading the file as is
# newline='' - to ensure there is no unnesecary space between lines
def display_expenses():
    with open('expense.csv', mode ='r', encoding = 'utf-8', newline='') as file:
        reader = csv.reader(file)
        #
        print(tabulate(reader, headers="firstrow", tablefmt="grid"))

# To display a menu that allows the user to interact with the expense tracker
def display_menu():
    while True:
        try:
            print("1. Add Expense\n2. View All Expenses\n3. View Total Expense\n4. Exit")
            option = int(input("Select an Option: "))
            break
        except ValueError:
            print("Please select one of the displayed options.")
    if option == 1:
        create_expense_file()
    elif option == 2:
        display_expenses()
    elif option == 3:
        print(f"The total expense is {T_Amount:.2f}")
    elif option == 4:
        print("Have a Good Day!")
    else:
        print("Error. Please select from the displayed options.")


display_menu()

