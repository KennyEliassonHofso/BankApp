from optparse import Option
from bank import Bank

b = Bank

def menu():
    # Menu val.    
    print("""\n Pick an Option:
    1. Add new customer
    2. Get customer by pnr
    3. Get all customers
    4. Change name for an existing customer
    5. Remove customer
    6. Add new account
    7. Close an existing account
    8. Use pnr/id to get an account
    9. Deposit or withdraw
    0. Exit.
    """)
    choice = int(input("Pick a number:\n"))
    # Add new customer
    if choice == 1: 
        pnr = input("Type your security number with 10 digits: ")
        if len(pnr) !=10: 
            print("Invalid")
            menu()
        else: 
                first_name = input("Please, Enter your first name: ").capitalize
                last_name = input("Please, Enter your lastname: ").capitalize
                b.add_customer(first_name, last_name, pnr)
                menu()
    # Get customer by PNR. 
    elif choice == 2: 
        pnr = input("Find specifik customer by security number (10 digits): ")
        if len (pnr) != 10:
            print("Invalid security number, try again.")
            pnr = input("Find specifik customer by security number (10 digits):\n")
        else: 
            customer = b.get_customer_by_pnr(pnr)
            print(customer)
            menu()
    # Get all customers. 
    elif choice == 3:
            print("This is the customer list: ")
            print(b.get_all_customers())
            menu()
    # Change name for customer. 
    elif choice == 4: 
        pnr = input("Type customers security number (10 digits): ")
        if len(pnr) != 10:
            print("Invalid security number, please try again.")
        else: 
            first_name = input("Type customers first name:").capitalize
            last_name = input("Type costumers last name:").capitalize
            b.change_customer_name(pnr, first_name,last_name)
            menu()
    # Remove Customer. 
    elif choice == 5:
        pnr = input("Type in the security number for the customer you want to delete")
        if len(pnr) !=10: 
            print("Invalid, try again")
        else:
            remove = b.remove_customer(pnr)
            print(remove)
            menu()
    # Add new account. 
    elif choice == 6:
        pnr = input("Enter customers security number: ")
        if len(pnr) != 10:
            print("Invalid")
        else: 
            b.add_account(pnr)
            menu()
    # close an existing account. 
    elif choice == 7:
        pnr = input("Type customers security number (10 digits): ")     
        if len(pnr) != 10:
            print("Invalid")
        else:
            account_number = input ("Select an account to close")
            b.close_account(pnr, account_number)
            menu()
    # find an account using PNR.
    elif choice == 8:
         pnr = input("Type customers security number (10 digits): ") 
         if len(pnr) != 10:
            print("Invalid")    
         else:
            account_number = input("Select account")
            b.get_account(pnr, account_number)
            menu()
    # Deposit/Withdraw 
    elif choice == 9:
        print("Choose \n1. For Deposit \n2 For Withdraw")
        option = int (input("Press the one you want."))
        # Deposit
        if option == 1:
            pnr = input("Type customers security number (10 digits): ")
            
            if len(pnr) != 10:
                print("Invalid, Type again.")
                
            else:
                account_number = input("Enter your account number")
                amount = int(input("Type In the amount you would like to diposit"))
            
            if amount is not int:
                print("Please try again")
                amount = int(input("Amount: "))
                if amount is not int:
                    menu()

            else: 
                deposit = b.deposit(pnr,account_number,amount)
                print(deposit)
                menu()
            # Withdraw 
    if option == 2:
            pnr = input("Type customers security number (10 digits): ")
            
            if len(pnr) != 10:
                print("Invalid, Type again.")
            else:
                account_number = input("Enter your account number")
                amount = int(input("Type In the amount you would like to withdraw"))
            
                if amount is not int:
                    print("Please try again")
                    amount = input("Amount: ")
                    amount = int(amount)
                else: 
                    withdraw = b.withdraw(pnr,account_number,amount)
                    print(withdraw)
                    menu()
    # Exit. 
    elif choice == 0:
        print("Thank you, please come again")
        
    else:
        menu()
