# Maintaining records of card details
card_records = [
    {
        'card_number': 1111,
        'pin': 1234,
        'balance': 1000
    },
    {
        'card_number': 2222,
        'pin': 4321,
        'balance': 2000
    }
]

# Setting limit on withdrawal amounts
limit = 600

# Set-up loop to continuously prompt for account access
while True:
    # Prompt user for input
    card_number = input("Please enter your card number: ")
    pin_input = input("Please enter your PIN: ")
    
    # Iterate over the record to find a match for the entered card details
    for item in card_records:
        if (card_number == item['card_number'] and pin_input == item['pin']):
            while True:
                amount = input("Please enter the amount you wish to withdraw: ")
            
                # Validate user input
                if (amount == ""):
                    print("Input cannot be empty.")
                elif (int(amount) > limit):
                    print("Withdrawal amount exceeded the limit, please try again.")
                else:
                    break
            
            # Validate the account 
            if (int(amount) > item['balance']):
                print("You do not have enough funds to withdraw that amount")
            
            # Dispense money
            else:
                item['balance'] = item['balance'] - int(amount)
                currency_denomination = int(amount / 20)
                twenty = currency_denomination * 20
                print(f"Dispensing {currency_denomination} - $20 notes: ${twenty}")
                balance_str = str(item['balance']).split('.')[0]
                print(f"Remaining balance: ${balance_str}")
    
    # Check to see if card details were correct