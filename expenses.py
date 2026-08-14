import csv
from tabulate import tabulate
from datetime import date

T_Amount = 0 
# To Write data collected from user into a CSV file
# "While True (....)" - To create a loop that only exits if the input is < 0 or there is a ValueError
def create_expense_file():
    global T_Amount
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
        data.append([Date, Expense, f"$ {Amount:.2f}"])
    with open('expense.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)

    return_menu("Do you wish to return to menu? 'Yes' or 'No'")
    
  
#TO Open/ Read the Data in the CVS file
# mode = r - to read/open
# encoding = utf-8  - soemthing to do with reading the file as is
# newline='' - to ensure there is no unnesecary space between lines
def display_expenses():
    with open('expense.csv', mode ='r', encoding = 'utf-8', newline='') as file:
        reader = csv.reader(file)
        #
        print(tabulate(reader, headers="firstrow", tablefmt="grid"))
    return_menu("Do you wish to return to menu? 'Yes' or 'No'")

# To display a menu that allows the user to interact with the expense tracker
def display_menu():
    while True:
        try:
            print("1. Add Expense\n2. View All Expenses\n3. View Total Expense\n4. Exit")
            option = int(input("Select an Option: "))
            break
        except ValueError:
            print("Please select one of the displayed options.")
    while True:
        if option == 1:
            create_expense_file()
            break
        elif option == 2:
            display_expenses()
            break
        elif option == 3:
            print(f"The total expense is {T_Amount:.2f}")
            return_menu("Do you wish to return to menu? 'Yes' or 'No'") 
            break
        elif option == 4:
            print("Have a Good Day!")
            break
        else:
            print("Error. Please select from the displayed options.")
            display_menu()

def return_menu(prompt_message):
    while True:
        command = (input(prompt_message))
        if command in ["Yes", "No"]:
            break
        else:
            print("Please select 'Yes' or 'No'")
    if command == "Yes":
        display_menu()
    else:
        print("Have a good day!")

        



display_menu()

