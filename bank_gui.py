import tkinter as tk
from tkinter import messagebox

# BankAccount class to represent a bank account
class BankAccount:
    def __init__(self, account_number, name, initial_balance, account_type):
        self.account_number = account_number
        self.name = name
        self.balance = initial_balance
        self.account_type = account_type

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.account_type == "Savings" and amount > 5000:
            messagebox.showerror("Error", "Withdrawal limit exceeded for Savings account!")
        elif self.balance >= amount:
            self.balance -= amount
        else:
            messagebox.showerror("Error", "Insufficient balance!")

    def __str__(self):
        return f"Account Number: {self.account_number}\nName: {self.name}\nBalance: {self.balance}\nAccount Type: {self.account_type}"


# Bank class to manage bank accounts
class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, name, initial_balance, account_type):
        if account_number in self.accounts:
            messagebox.showerror("Error", "Account already exists!")
            return False
        self.accounts[account_number] = BankAccount(
            account_number, name, initial_balance, account_type
        )
        messagebox.showinfo("Success", "Account created successfully!")
        return True

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number].deposit(amount)
            messagebox.showinfo("Success", "Amount deposited successfully!")
        else:
            messagebox.showerror("Error", "Account not found!")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number].withdraw(amount)
            messagebox.showinfo("Success", "Amount withdrawn successfully!")
        else:
            messagebox.showerror("Error", "Account not found!")

    def check_balance(self, account_number):
        if account_number in self.accounts:
            account = self.accounts[account_number]
            messagebox.showinfo("Balance", str(account))
        else:
            messagebox.showerror("Error", "Account not found!")


# BankApp class to create the GUI
class BankApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Bank App")
        self.geometry("400x400")

        self.bank = Bank()

        self.create_widgets()

    def create_widgets(self):
        self.label_account_number = tk.Label(self, text="Account Number")
        self.label_account_number.pack()

        self.entry_account_number = tk.Entry(self)
        self.entry_account_number.pack()

        self.label_name = tk.Label(self, text="Name")
        self.label_name.pack()

        self.entry_name = tk.Entry(self)
        self.entry_name.pack()

        self.label_initial_balance = tk.Label(self, text="Initial Balance")
        self.label_initial_balance.pack()

        self.entry_initial_balance = tk.Entry(self)
        self.entry_initial_balance.pack()

        self.label_account_type = tk.Label(self, text="Account Type")
        self.label_account_type.pack()

        self.account_type_var = tk.StringVar(value="Savings")

        self.radiobutton_savings = tk.Radiobutton(
            self,
            text="Savings",
            variable=self.account_type_var,
            value="Savings",
        )
        self.radiobutton_savings.pack()

        self.radiobutton_current = tk.Radiobutton(
            self,
            text="Current",
            variable=self.account_type_var,
            value="Current",
        )
        self.radiobutton_current.pack()

        self.button_create_account = tk.Button(
            self, text="Create Account", command=self.create_account
        )
        self.button_create_account.pack()

        self.label_amount = tk.Label(self, text="Amount")
        self.label_amount.pack()

        self.entry_amount = tk.Entry(self)
        self.entry_amount.pack()

        self.button_deposit = tk.Button(self, text="Deposit", command=self.deposit)
        self.button_deposit.pack()

        self.button_withdraw = tk.Button(
            self, text="Withdraw", command=self.withdraw
        )
        self.button_withdraw.pack()

        self.button_check_balance = tk.Button(
            self, text="Check Balance", command=self.check_balance
        )
        self.button_check_balance.pack()

    def create_account(self):
        account_number = self.entry_account_number.get()
        name = self.entry_name.get()
        initial_balance = float(self.entry_initial_balance.get())
        account_type = self.account_type_var.get()

        self.bank.create_account(account_number, name, initial_balance, account_type)

    def deposit(self):
        account_number = self.entry_account_number.get()
        amount = float(self.entry_amount.get())

        self.bank.deposit(account_number, amount)

    def withdraw(self):
        account_number = self.entry_account_number.get()
        amount = float(self.entry_amount.get())

        self.bank.withdraw(account_number, amount)

    def check_balance(self):
        account_number = self.entry_account_number.get()

        self.bank.check_balance(account_number)


# Create an instance of the BankApp class
app = BankApp()

# Start the main event loop
app.mainloop()
