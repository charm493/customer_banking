# Import the create_cd_account and create_savings_account functions
from savings_account import create_savings_account
from cd_account import create_cd_account

# checking if user's input value is a float number and larger than 0
def is_valid_float(input_value):
    try:
        float(input_value) and float(input_value) > 0
        return True
    except ValueError:
        print("Your input is not a positive number, please input again!")
        return False

# checking if user's input value is a int number and larger than 0
def is_valid_int(input_value):
    if(input_value.isdigit() and int(input_value) >= 0):
        return True
    else:
        print("Your input is not a positive integer number, please input again!")
        return False
    
# geting input value from user and checking if the value is valid
def get_input_value(input_name):
    is_input_correct = False
    while is_input_correct == False:
        value = input(f"Please input the {input_name} (it must be number)")
        if(input_name == "months"):
            is_input_correct = is_valid_int(value)
            if is_input_correct:
                return int(value) 
        else:
            is_input_correct = is_valid_float(value)
            if is_input_correct:
                return float(value)

# print out account infor      
def print_result(balance, interest):
    print("-" * 50)
    print(f"Your current account balance is {balance:.2f}")
    print(f"Your current account interest is {interest:.2f}")
    print("-" * 50)


# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = 0
    savings_interest = 0
    savings_maturity = 0

    savings_balance = get_input_value("saving balance")
    savings_interest = get_input_value("saving interest")
    savings_maturity = get_input_value("months")

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print_result(updated_savings_balance, interest_earned)

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = 0
    cd_interest = 0
    cd_maturity = 0

    cd_balance = get_input_value("CD balance")
    cd_interest = get_input_value("CD interest")
    cd_maturity = get_input_value("months")

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print_result(updated_cd_balance, interest_earned)


if __name__ == "__main__":
    main()


