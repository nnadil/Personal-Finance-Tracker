import json#To save the details
import datetime#To take current date
# Global list to store transactions
transactions = []

# File handling functions
def load_transactions():
    global transactions
    try:
        with open("Transactions.json","r")as file:
            transactions=json.load(file)#Loading file details to the transactions variable
    except FileNotFoundError:
        print("File Not Found")
        transactions=[]
    except json.JSONDecodeError:
        print("Error decoding JSON. Starting with an empty transaction list")
        

def save_transactions():
    with open("Transactions.json","w")as file:
        file.write("[")
        file.write("\n")
        for i in transactions:
            file.write("\t")
            json.dump(i,file)#dump() convert python object into JSON objects
            file.write("\n")
        file.write("]")
# Feature implementations
def add_transaction():
    try:
        amount=float(input("Enter amount: "))
        category=input("Enter catagory: ")
        while True:#while transaction type is satisfy
            transaction_type=input("Enter type(Income/Expense): ").capitalize()
            if transaction_type in ['Income','Expense']:
                break
            else:
                print("Invalid transaction type")
        current_date=datetime.date.today()#Takeing current date and time
        while True:#while date is satisfy
            date=input("Enter date(YYYY-MM-DD): ")
            if len(date)!=10:
                print("Invalid date")
                continue
            year,month,day=date.split("-")
            if len(date)==10 and int(month)<=12 and int(day)<=31:
                input_date=datetime.date(int(year),int(month),int(day))#Formatting the input date 
                if input_date<=current_date:#Checking the input date below the current date
                    break
                else:
                    print("The date you entered in future")
            
            else:
                print("Invalid date")
        transactions.append([amount,category,transaction_type,date])#Entering the data to the list
        save_transactions()
        print("Transaction added successfully")
    except ValueError:
        print("Invalid amount, Please enter a valid amount")
def view_transactions():
    if len(transactions)==0:
        print("No transactions available")

    else:
        for transaction in transactions:#To print the sublist in nested list
            print(transaction)

def update_transaction():
    view_transactions()
    try:
        index=int(input("Enter index of transaction to update: "))
        if index>=0 and index<=len(transactions):
            new_amount=float(input("Enter new amount: "))
            new_catagory=input("Enter new catagory: ")
            
            while True: #while transaction type is satisfy
                new_trans_type=input("Enter new transaction type(Income/Expense): ").capitalize()
                if new_trans_type in ['Income','Expense']:
                    break
                else:
                    print("Invalid transaction type")
            current_date=datetime.date.today()#Taking current date
            
            while True:#while date is satisfy
                new_date=input("Enter new Date(YYYY-MM-DD): ")
                if len(new_date)!=10:#If the length of new_date not equals to 10
                    print("Inavlid date")
                    continue
                
                year,month,day=new_date.split("-")
                if len(new_date)==10 and int(month)<=12 and int(day)<=31:
                    new_input_date=datetime.date(int(year),int(month),int(day))
                    if new_input_date<=current_date:
                        break
                    else:
                        print("The date you entered in future")
                else:
                    print("Ïnvalid date")
            transactions[index-1]=[new_amount,new_catagory,new_trans_type,new_date]
            save_transactions()#To save updated transactions
            print("Transaction updated successfully")
        else:
            print("Invalid index, Please enter a valid index")
    except ValueError:
            print("Invalid amount, Please enter a valid amount")
   

def delete_transaction():
    view_transactions()
    try:
        index=int(input("Enter index of transaction to delete: "))
        if index>=0 and index<=len(transactions):
            del transactions[index-1]
            save_transactions()#To save the deleted transactions
            print("Transaction deleted successfully")
        else:
            print("Invalid index, please enter a valid index")
    except ValueError:
        print("Invalid index. Please eneter a valid index")

def display_summary():
    Total_income=0#intializing variables
    Total_expense=0
    if not transactions:#If transaction list is empty
        print("No transactions record yet")
    for sublist in transactions:
        if sublist[2]=="Income":
            Total_income+=sublist[0]
        elif sublist[2]=="Expense":
            Total_expense+=sublist[0]
    balance=Total_income-Total_expense
    print("Total income is: ",Total_income)
    print("Total expense is: ",Total_expense)
    print("Profit is: ",balance)

def main_menu():
    load_transactions()  # Load transactions at the start
    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Update Transaction")
        print("4. Delete Transaction")
        print("5. Display Summary")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_transaction()
        elif choice == '2':
            view_transactions()
        elif choice == '3':
            update_transaction()
        elif choice == '4':
            delete_transaction()
        elif choice == '5':
            display_summary()
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()

# if you are paid to do this assignment please delete this line of comment

