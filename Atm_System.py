# Autore: Ars3ツ
#Simulation of an ATM
#(This is just a simulation.) Any unlawful act committed with this code does not concern the creator.)


import json  # to save and load user data from a file
from datetime import datetime  # to log dates and times of operations

# Define the file where we will save user data
DATA_FILE = 'users.json'

# Function to load user data from the JSON file
def load_data():
    try:
        with open(DATA_FILE, 'r') as file:
            data = json.load(file)
            # Ensure that data is in the correct format
            if not all('pin' in user and 'balance' in user for user in data.values()):
                raise ValueError("Invalid user data.")
            return data
    except (FileNotFoundError, ValueError) as e:
        print(f"Error loading data: {e}")
        return {}

# Function to save updated data to the JSON file
def save_data(data):
    try:
        with open(DATA_FILE, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        print(f"Error saving data: {e}")

# Function to save log of each user operation
def save_log(user, message):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log = f"[{timestamp}] {message}\n"
    try:
        with open(f"{user}_log.txt", 'a') as file:
            file.write(log)
    except IOError as e:
        print(f"Error writing log: {e}")

# Function to ask for a valid amount
def ask_amount(operation):
    while True:
        try:
            amount = float(input(f"Enter the amount to {operation}: "))
            if amount <= 0:
                raise ValueError("The amount must be positive.")
            return amount
        except ValueError as e:
            print(f"Error: {e}. Please try again.")

# Main ATM class that represents the ATM for each user
class ATM:
    def __init__(self, user, data):
        self.user = user
        self.data = data

    def save(self):
        save_data(self.data)

    def withdraw(self, amount):
        if amount > self.data[self.user]["balance"]:
            print("Insufficient balance.")
            save_log(self.user, f"Failed withdraw: Insufficient balance {amount}")
        else:
            self.data[self.user]["balance"] -= amount
            self.save()
            print(f"Withdrawn €{amount:.2f}. Balance: €{self.data[self.user]['balance']:.2f}")
            save_log(self.user, f"Withdrew €{amount:.2f}")

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount.")
            save_log(self.user, f"Failed deposit: Invalid amount {amount}")
        else:
            self.data[self.user]["balance"] += amount
            self.save()
            print(f"Deposited €{amount:.2f}. Balance: €{self.data[self.user]['balance']:.2f}")
            save_log(self.user, f"Deposited €{amount:.2f}")

    def check_balance(self):
        balance = self.data[self.user]["balance"]
        print(f"Current balance: €{balance:.2f}")
        save_log(self.user, "Checked balance")

    def change_pin(self, new_pin):
        if len(new_pin) == 4 and new_pin.isdigit():
            self.data[self.user]["pin"] = new_pin
            self.save()
            print("PIN changed successfully.")
            save_log(self.user, "PIN changed")
        else:
            print("The PIN must be 4 numeric digits.")
            save_log(self.user, "Failed PIN change: Invalid PIN format")

# Function to create a new user
def create_user(data):
    username = input("Choose a username: ")
    if username in data:
        print("User already exists.")
        return None

    while True:
        pin = input("Set a 4-digit PIN: ")
        if len(pin) == 4 and pin.isdigit():
            break
        else:
            print("The PIN must be 4 numeric digits.")
               
    data[username] = {"pin": pin, "balance": 1000.0}
    save_data(data)
    print(f"User '{username}' created successfully! Initial balance: €1000.00")
    save_log(username, "User created")
    return username

# Function to log in to an existing account
def login(data):
    username = input("Username: ")
    if username not in data:
        print("User not found.")
        save_log(username, "Failed login: User not found")
        return None

    for attempts in range(3, 0, -1):
        pin = input("Enter your PIN: ")
        if pin == data[username]["pin"]:
            print("Access granted.")
            save_log(username, "Login successful")
            return username
        else:
            print(f"Incorrect PIN. Attempts remaining: {attempts - 1}")
            save_log(username, f"Failed login: Incorrect PIN, attempts left {attempts - 1}")

    print("Too many failed attempts. Access blocked.")
    save_log(username, "Access blocked after failed attempts")
    return None

# Main menu function
def main_menu():
    data = load_data()  # Load user data

    while True:
        print("\n=== Welcome to the ATM ===")
        print("1. Create new user")
        print("2. Log in")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            create_user(data)

        elif choice == "2":
            user = login(data)
            if user:
                atm = ATM(user, data)
                while True:
                    print("\nAvailable operations:")
                    print("1. Withdraw")
                    print("2. Deposit")
                    print("3. Check balance")
                    print("4. Change PIN")
                    print("5. Exit")

                    operation = input("Choose an option: ")

                    if operation == "1":
                        amount = ask_amount("withdraw")
                        atm.withdraw(amount)

                    elif operation == "2":
                        amount = ask_amount("deposit")
                        atm.deposit(amount)

                    elif operation == "3":
                        atm.check_balance()

                    elif operation == "4":
                        new_pin = input("Enter new 4-digit PIN: ")
                        atm.change_pin(new_pin)

                    elif operation == "5":
                        print("Logging out...")
                        save_log(user, "User logged out")
                        break

                    else:
                        print("Invalid option.")

        elif choice == "3":
            print("Thank you for using our ATM!")
            break

        else:
            print("Invalid choice. Please try again.")

# Entry point of the program
if __name__ == "__main__":
    main_menu()
