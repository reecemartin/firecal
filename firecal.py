# Long Term Budget Calculator

def display_accounts(accounts):
    for account in accounts:
         print("Account Name: " + account[0] + " Account Value: " + str(account[1]) + " Account Return Rate: " + str(account[2] * 100 - 100) + "%\n")

def get_accounts():
        
    entry_title = ""
    entry_account_value = ""
    entry_return_rate = ""
    accounts = []

    while entry_title != "quit" and entry_account_value != "quit" and entry_return_rate != "quit":
            entry_title = input("Account Name:\n")
            if entry_title == "quit":
                break
            entry_account_value = float(input("Account Value:\n"))
            entry_return_rate = float(input("Expected Annual Multiplier:\n"))
            accounts.append([entry_title, entry_account_value, entry_return_rate])

    return accounts

def main():
     
    print("Running...")

    display_accounts(get_accounts())

    # Flow

    # Get Existing Accounts
        
    # Print Existing Accounts

    # Print Current Safe Recurring Earning Potential

    # Find Monthly Savings Post Tax

    # Find Number of Months Forward to Project

    # Project Total Assets and Safe Recurring Earning Potential as Well As Current Growth Rate

if __name__ == "__main__":
    main()
