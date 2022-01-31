import account

class Customer:
    

    def __init__(self, first_name, last_name, pnr, customer_id) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.pnr = str(pnr)
        self.accounts = []
        if customer_id:
            self.customer_id = customer_id
        else: 
            self.customer_id = next(self.customer_id)
            self.customer_id = 1001 + self.customer_id

        def __str__(self):

            account_list = []
            for x in self.accounts:
                account_list.append(x.account_number)
                account_list.append(x.account_type)
                account_list.append(x.balance)
                return f"Customer ID: {self.customer_id},\n Name: {self.first_name} {self.last_name}\n Security number: " \
                    f"{self.pnr}, \n Accounts: {account_list}"

        
    def show_customer(self):
        
        account_detail = []
        
        for account in self.accounts:
            details = account.account_number, account.balance, account.account_type
            account_detail.append(details)
        return self.customer_id, self.pnr, self.first_name, self.last_name, account_detail

    def add_account(self):

        acc = account.Account()
        self.accounts.append(acc)
        print("Done, your new account has been created!")
        return f"Account number: {acc.account_number}, \nAccount type: {acc.account_type},\n Balance: {acc.balance}"

    def close_account(self, account_number):
        for x in self.accounts: 
            if account_number == x.account_number:
                account = self.accounts.index(x)
                self.accounts.pop(account)
                break