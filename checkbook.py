#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 13:41:11 2023

@author: manelson
"""
# Import libraries and define functions
import os
import subprocess
import json
import datetime as dt

# Open the balance file or create it if it doesn't exist
if 'ledger.json' not in os.listdir():
    balance = 0
    transactions = []
else:
    with open('ledger.json','r') as f:
        transactions = json.load(f)
        balance = sum(list(float(i['amount']) for i in transactions))
            
def save_change(transact):
    with open('ledger.json','w') as f:
        json.dump(transact,f)

def menu1(bal):

    print('\t\t','*'*10,f'Your current balance is: ${bal:,.2f}')

def menu2(bal):

    while True:
        withdraw = input('Enter the amount you wish to withdraw: ')

        try:
            transactions.append({
                'time':f'{dt.datetime.now()}',
                'amount':f'-{withdraw}'
                })
            return bal - float(withdraw)
        except:
            print('\t\t', withdraw,'is not a valid amount.')

def menu3(bal):

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

def menu4(transact):
    save_change(transact)


while True:  
    # Print the menu options
    print("""
          Menu:
              1) View current balance
              2) Submit withdrawal
              3) Submit deposit
              4) Quit
          """)
    menu_option = input('\tEnter a menu option: ')
    
    # Call the option defined
    if menu_option == '1':
        # Check current balance
        menu1(balance)
        
    elif menu_option == '2':
        # Take from balance
        balance = menu2(balance)
        save_change(transactions)
        print('\t\t','*'*10,f'Your new balance is ${balance:,.2f}.')
        
    elif menu_option == '3':
        # Add to balance
        balance = menu3(balance)
        save_change(transactions)
        print('\t\t','*'*10,f'Your new balance is ${balance:,.2f}.')
        
    elif menu_option == '4':
        # Exit program and write balance
        menu4(transactions)
        print('Goodbye!')
        break
    
    # SECRET MENU OPTION
    elif menu_option == '1812':
        print(('='*50).center(100))
        print('WARNING: KILLING BALANCE RECORD'.center(100))
        print(f'ENDING BALANCE: ${balance:,.2f}'.center(100))
        print(('='*50).center(100))
        os.remove('ledger.json')
        break
    
    else:
        print('Input invalid')