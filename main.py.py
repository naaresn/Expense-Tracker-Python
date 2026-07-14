import re
from expense import Expense

def main():
    print("====== WELCOME TO YOUT PERSONAL EXPENSE TRACKER ======")
    print("[1] Input expense")
    print("[2] Load expense")
    user_input = input("Enter your choice: ")
    
    path = "data\expense_file.csv"
    
    if user_input == "1":
        expense = user_expense()        
        get_expense(expense, path)
    elif user_input == "2":
        load_expense(path)
    else:
        print("please enter the right number")


def user_expense():
    print("====== INPUT EXPENSE =====")    
    while True: 
        expense_name = input("Enter your expense name: ")
        if re.fullmatch(r'[a-zA-z0-9\s]+', expense_name):
            break
        else:
            print("Not valid. Please check your input")
    
    
    while True:
        try:
            amount_input = input("Enter expense amount: ")
            amount_input2 = amount_input.replace(".", "")
            expense_amount = float(amount_input2)
            
            if expense_amount<= 0:        
                print("Amount must be greater than 0")
                continue
            break
        except ValueError:
            print("Please check your input")    
           
        
    while True:
        category_list = ["Food", "Groceries", "Life Style", "Fun", "Work"]
        print("Select category: ")
        for i, item in enumerate(category_list):
            print(f"({i+1}) {item}")
        
        value_range = f"[1 - {len(category_list)}]"
        choice = int(input(f"Select category number {value_range}: ")) -1
        
        try:
            if choice in range(len(category_list)):
                selected_category = category_list[choice]
                new_expense = Expense(name=expense_name, category=selected_category, amount= expense_amount )
                return new_expense
            else:
                print("Error! Please check your input")
        except ValueError:
            print("Error! Please check your input")

def get_expense(expense: Expense, path):
    print(f"Saving your expense: {expense} to {path}")
    with open(path, "a") as f:
        f.write(f"{expense.name}, {expense.category}, {expense.amount}\n")    

def load_expense(path):
    expenses = []
    with open(path, "r") as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_category, expense_amount = line.strip().split(", ")
            
            expense_amount = float(expense_amount)
            expenses_line = Expense(name= expense_name, category= expense_category, amount= expense_amount)
            print(expenses_line)
            expenses.append(expenses_line)
            
    
    sum_percategory = {}
    for expense in expenses:
        key = expense.category
        if key in sum_percategory:
            sum_percategory[key] += expense_amount
        else:
            sum_percategory[key] = expense_amount
    for key, amount in sum_percategory.items():
        print(f"{key}: Rp {amount:,.0f}".replace(",", "."))
    
    total = sum([expen.amount for expen in expenses]) 
    print(f"Total spent = Rp {total:,.0f}".replace(",", "."))
    

    
    

    
            
if __name__ == "__main__":
    main()