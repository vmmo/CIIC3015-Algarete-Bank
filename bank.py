def accountNumber(num):
    """Convert integer to account number"""
    num += 1 # Utilizing this I keep track of the accounts that are added
    acc = str(num) # Utilizing this Im making the final result a str and be able to print along with the rest of the information of the accounts
    while len(acc) < 10: # Utilizing this loop it creates 0's in the empty spaces which do not have digits inserted
        acc = "0" + acc # Counts the accounts added
    return acc 

def printAccount(bankAccount, order):
    """Print line containing account information for a given account"""
    columnSize = 20
    if order == "name": # Identifies if in the first column its meant to start in alphabetical order
        dollars = '${:,.2f}'.format(bankAccount[2]) # Utilized so the end product appears with a $ and not in the .txt file
        print("|" + bankAccount[0] + " "*(columnSize - len(bankAccount[0]))
        + "|" + bankAccount[1] + " "*(columnSize - len(bankAccount[1]))
        + "|" + dollars + " "*(columnSize - len(dollars)) 
        + "|") # Prints the columns including the account information for each account
        
    if order == "account": # Identifies if in the first column its meant to start in order of account number
        dollars = '${:,.2f}'.format(bankAccount[2]) # Utilized so the end product appears with a $ and not in the .txt file
        print("|" + bankAccount[1] + " "*(columnSize - len(bankAccount[1]))
        + "|" + bankAccount[0] + " "*(columnSize - len(bankAccount[0]))
        + "|" + dollars + " "*(columnSize - len(dollars)) 
        + "|") # Prints the columns including the account information for each account
    

file = open('alghistorical.txt', 'r')
transactions = file.readlines()
"""Read file and execute all transactions"""
bank = [] # Empty list for the sublists
earnings = 0 # Utilizing this it keeps track of the final earnings for the Total Bank Gross Earnings of the bank
totalBonus = 0 # Utilizing this it adds the bonus together for the Total Bonus Paid of each client
for transaction in transactions: # Utilized to iterate through every transaction and identify them
    content = transaction.split(", ") # Utilized to split the sublist into different indexes
    if(content[0] == "B"):
        for bankAccount in bank: # Utilized to iterate through the previous accounts added and add the bonus accordingly
            bonus = bankAccount[2] * float(content[1])/100 # Utilized as the equation for how much the bonus is
            bankAccount[2] += bonus #Utilized to add the bonus to the account
            totalBonus += bonus # Utilized to report the Total Bonus Paid
    else:
        amount = float(content[2]) # Utilized to identify the second index in the sublist to mathimatically alter as transactions occur and convert make sure it is a float
        fee = amount*0.05 # Utilized to apply he fee of 5% which occurs whenever there is any interaction with the bank system
        earnings += fee # Utilized to maintain the earnings the bank gets from every transaction
        if(content[0] == "O"): # Utilized in the case that the zero index is O, creating a new bank account that includes account number, name, and money in the account
            bankAccount = [] #Sublist
            bankAccount.append(content[1]) # Utilizing the first index to insert the name of the account owner
            bankAccount.append(accountNumber(len(bank))) # Utilized to create new bank account number so that they do not repeat
            bankAccount.append(amount - fee) # Utilized to remove the fee to the amount deposited within the new account
            bank.append(bankAccount) # Utilized to add the new account to the list
        if(content[0] == "W"): # Utilized in the case that the zero index is W, withdrawing the amount requested by the client
            accountIndex = int(content[1]) - 1 # Utilized to identify the sublist from the list within which will be altered
            bankAccount = bank[accountIndex] 
            bankAccount[2] = bankAccount[2] - amount # Removes from the second index of the sublist the amount withdrawn
        if(content[0] == "D"): # Utilized in the case that the zero index is D, depositing the amount requested by the client
            accountIndex = int(content[1]) - 1 # Utilized to identify the sublist from the list within which will be altered
            bankAccount = bank[accountIndex]
            bankAccount[2] = bankAccount[2] + amount - fee # An Addition to the second index of the sublist the amount to deposit
file.close()

# Console Outputs
alphaBank = bank.copy() #Utilized to make a seconnd file later in the code displayed as an alphabetical copy
alphaBank.sort() # Utilized to sort the names alphabetically and numerically



file2 = open('algcustomers', 'w')
"""Sort bankAccounts by name and write results into new file"""
for bankAccount in alphaBank: # Utilized to iterate though the list and convert it into a new file in alphabetical order
    bankAccount[2] = '{:.2f}'.format(bankAccount[2]) # Utilized so the end product appears with a $ and not in the .txt file
    file2.write(", ".join(bankAccount) + "\n")
file2.close()


