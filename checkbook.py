#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 13:41:11 2023

@author: manelson
"""
# Import libraries and define functions
import os
# import subprocess
import json
import datetime as dt

# Open the ledger file if it exists
# Initialize new transaction variables if it doesn't
if 'ledger.json' not in os.listdir():
    balance = 0
    transactions = []
else:
    with open('ledger.json','r') as f:
        transactions = json.load(f)
        balance = sum(list(float(i['amount']) for i in transactions))


# Function to save changes to file
def save_change(transact):
    with open('ledger.json','w') as f:
        json.dump(transact,f)

# Menu 1 displays current balance
def menu1(bal):
    print('\t\t','*'*10,f'Your current balance is: ${bal:,.2f}')

# Menu2 displays transactions
def menu2(transact):
    # print(transact) # test that list is passed correctly
    print('\nDate posted\t\tAmount')
    for i in transact:
        print(i['time'][:10],end='\t\t')  # Get only the date of transaction
        print(f'${float(i["amount"]):,.2f}')  # Convert i['amount'] to float then format it nice and neat

# menu3 is withdrawal
def menu3(bal):
    
    # While loop repeatedly asks for valid inpu
    while True:
        withdraw = input('Enter the amount you wish to withdraw: ')
        
        # Try..Except works best
        # float raises error if wrong input is sent in, causing except to be
        # executed and while loop to reiterate
        try:
            transactions.append({
                'time':f'{dt.datetime.now()}',
                'amount':f'-{withdraw}'
                })
            return bal - float(withdraw)
        except:
            print('\t\t', withdraw,'is not a valid amount.')

# menu4 is deposit
def menu4(bal):

    # Menu 3 is identical to menu3, except it adds instead of subtracts
    while True:
        deposit = input('Enter the amount you wish to deposit: ')
        
        try:
            transactions.append({
                'time':f'{dt.datetime.now()}',
                'amount':f'{deposit}'
                })
            return bal + float(deposit)
        except:
            print('\t\t', deposit, 'is not a valid amount.')

# menu5 is quit
def menu5(transact):
    # Makes sure that the changes are saved
    save_change(transact)


print('Welcome to Generic Ledger Software!')
while True:  
    # Print the menu options
    print("""
          Menu:
              1) View current balance
              2) Print previous transactions
              3) Submit withdrawal
              4) Submit deposit
              5) Quit
          """)
    menu_option = input('\tEnter a menu option: ')
    
    # Call the option defined
    if menu_option == '1':
        # Check current balance
        # Returns nothing
        menu1(balance)
    
    elif menu_option == '2':
        # Returns nothing
        # Displays all current transactions
        menu2(transactions)
        
    elif menu_option == '3':
        
        # Take from balance and then save changes to the ledger
        balance = menu3(balance)
        save_change(transactions)
        print('\t\t','*'*10,f'Your new balance is ${balance:,.2f}.')
        
    elif menu_option == '4':
        
        # Add to balance and then save changes to the ledger
        balance = menu4(balance)
        save_change(transactions)
        print('\t\t','*'*10,f'Your new balance is ${balance:,.2f}.')
        
    elif menu_option == '5':
        
        # Exit program and write balance
        menu5(transactions)
        print('Goodbye!')
        break
    
    # SECRET MENU OPTION
    # Developer option to wipe balance and check for proper file read/write execution
    # Also exits the program!!
    elif menu_option.lower() == 'thanatos':
        print(('='*50).center(100))
        print('WARNING: KILLING BALANCE RECORD'.center(100))
        print(f'ENDING BALANCE: ${balance:,.2f}'.center(100))
        print(('='*50).center(100))
        os.remove('ledger.json')
        break
    
    else:
        print('Input invalid')