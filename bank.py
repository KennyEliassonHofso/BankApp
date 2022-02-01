from http import client
import customer

class Bank:

    def __init__(self):
        self.customers = []
    # This Method should get me the information from the text file. 
    def _load(self):

            for line in open("My_customer.txt").readlines():
                customer = line.strip().split(":")
                for x in self.customers:
                    if customer[3] !=x.pnr:
                        if int(customer[0]) != int(x.customer_id):
                            client = customer.Customer(customer[1], customer[2], customer[3], customer[0])
                            self.customers.append(client)
                            break
                        else: 
                            client = customer.Customer(customer[1], customer[2], customer[3])
                            self.customers.append(client)
                        break
                    else: 
                        print("This customer does already exist")
                    return self.customers
    # Use this to get all the customers in the bank. 
    def get_all_customers(self):
                all_customers = []

                for customer in self.customers:
                    details = customer.pnr, customer.first_name, customer.last_name
                    all_customers.append(details)
                return all_customers
    # Adding an customer to the bank and the customer list. 
    def add_customer(self, first_name, last_name, pnr):

            client = customer.Customer(first_name, last_name, pnr)
            check = True
            if self.customers == []:
                self.customers.append(client)
            print(f"{client.customer_id}: {client.first_name} {client.last_name} is now a new customer. ") 
            
            for x in self.customers:
                    if x.ssn != client.pnr:
                        self.customers.append(client)
                    print(f"{client.customer_id}: {client.first_name} {client.last_name} is now a new customer.")
                    break
            else:
                check = False
                print("The PNR is already in use for a customer.")
                
            
            return check
                    
                    
    def get_customer_by_pnr(self, pnr):
        # If you need to get information about a customer using the PNR. 
                if self.customers == []:
                    print(f"Cant find any customer with PNR: {pnr}")
                else:
                    for x in self.customers:
                        if pnr == x.pnr:
                            return x.show_customer()
                        else:
                            print("Cant find any customer")
                            break
        # Changing the name for an existing customer. 
    def change_customer_name(self, pnr, first_name, last_name):
                
                if self.customers == []:
                    for x in self.customers:
                        if pnr == x.pnr:
                            x.first_name = first_name
                            x.last_name = last_name
                            print(f"{x.first_name} {last_name} has changed name!")
                            return True
                        else: 
                            print (f"The person with PNR {pnr} is not a customer here")
                    return False
        # Removing an existing customer. 
    def remove_customer(self, pnr):
            
        return_balance = 0
        customer = []
        for x in self.customers:
            if x.pnr == client.pnr:
                customer = self.customers.index(x)
                self.customers.pop(customer)
            
            for y in x.accounts:
                return_balance = y.balance
                return (f"{x.first_name} {x.last_name} is deleted/n" 
                f"Returned balance: {return_balance}")
        else:
                f"Customer with: {pnr} dosnt exist"
        # Adding an account to an existing customer. 
    def add_account(self, pnr):

        if self.customers == []:
            print (f"Cant find an Customer with {pnr}")
        else:
            for x in self.customers:
                if pnr == x.pnr:
                    print(x.add_account())
                    break
        # Finding an existing account for a existing customer. 
    def get_account(self, pnr, account_id):
        for customer in self.customers:
            if customer in self.customers:
                print(customer.accounts[0])
                for x in customer.accounts[0]:
                    if x.account_id == account_id:
                        return x.show_account()
                    break
            else:
                return("Error")
        # Puts money into an account. 
    def deposit(self, pnr, account_number, amount):

        for x in self.customers:
            if x.pnr == pnr:
                for y in x.accounts:
                    if y.account_number == account_number:
                        y.deposit(amount)
                        return True
                    else:
                        print(f"{account_number} cant be found")
                        return False
        # Takes money from an account.
    def withdraw(self, pnr, account_number, amount):
        for x in self.customers:
            if x.pnr == pnr:
                for y in x.accounts:
                    if account_number == y.account_number:
                        y.withdraw(amount)
                        return True
                    else:
                        print(f"{account_number} cant be found")
                        return False
        # Closing an existing account for a customer. 
    def close_account(self, pnr, account_number):
        for x in self.customers:
            if x.pnr == pnr:
                for y in x.accounts:
                    if y.account_number == account_number:
                        x.close_account(account_number)
                        return (f"{account_number} is closed, funds back: {y.balance}")
                    else:
                        return (f"{account_number} cant be found")



            