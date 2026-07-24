'''
Challenge 3: The Mini-ATM Simulator
- Build a continuous loop that displays a menu: 1. Check Balance | 2. Deposit | 3. Withdraw | 4. Exit.
- Create a variable outside the loop to track the balance (start at $1000).
- Prompt the user to choose an option (1, 2, 3, or 4).
- Write a separate function for deposit(amount, current_balance) and withdraw(amount, current_balance).
- Validation: Prevent the user from depositing a negative number, and prevent them from withdrawing more money than they have.
If they select 4, break the loop and say goodbye.
'''
# IMPORTING LIBRARIES
import random as rd # importing the library with an alias

# INITIALIZING VARIABLES
# 1. Variables that will be used inside the ATM
user_selection: int = None # It starts from None
user_error: int = 3 # User has 3 chances, after that the ATM will shut down
user_deposit: float = 0 # Start from -1, because if the user type a negative number ther's a while loop
user_withdraw: float = 0

#2. Variables that will be used for the user
user_balance: float = rd.uniform(0,9999) # Tha user's balance will start by a random float

# OUTTER FUNCTION
def withdraw_money(current_balance: float, withdraw_value: float) -> float:
    new_balance: float = 0 # Initialize the variable
    if withdraw_value > current_balance:
        print("You don't have enough money to withdraw!")
        raise ValueError
    else:
        new_balance = current_balance - withdraw_value
    return new_balance

def deposit_money(current_balance: float, deposit_value: float) -> float:
    new_balance: float = 0
    if deposit_value < 0:
        print("You can't deposit a negative value!")
        raise ValueError
    else:
        new_balance = current_balance + deposit_value
    return new_balance

# CONTINUOS LOOP
while True: # This will state a continuos loop
    try:
        # Error handling, user can type a different entry
        user_selection = int(input("\nSelect your operation by typing the corresponding number:\n [1] Check Balance | [2] Deposit | [3] Withdraw | [4] Exit \n Type your choice: "))
    except (ValueError, TypeError) as e:
        print("\nPlease insert a valid entry! ")
        user_error -= 1
    
    # STARTING THE MENU FUNCTIONS
    if user_selection == 1: # First Operation - Balance Checking
        print(f"\nYour balance is: ${user_balance:.2f}")
    if user_selection == 2: # Second operation - Deposit
        try:
            # Error Handling
            user_deposit = float(input("\nType how much money do you want to deposit into your account: "))
            user_balance = deposit_money(user_balance, user_deposit) # Allocating the function into the variable
        except (ValueError, TypeError) as e:
            print("\nPlease type a valid enter!")
            user_error -= 1
        print(f"\nYour balance is: ${user_balance:.2f}")
    if user_selection == 3: # Withdraw the user money
        try:
            user_withdraw = float(input("\n Type how much money do you want to withdraw: "))
            user_balance = withdraw_money(user_balance, user_withdraw)
        except (ValueError, TypeError) as e:
            print("Please type a valid enter!")
            user_error -= 1
    elif (user_selection == 4) or (user_error == 0):
        print("\nGoodbye, have a good day! ")
        break