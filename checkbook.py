#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 13:41:11 2023

@author: manelson
"""
# Import libraries and define functions
import os
import subprocess

# Open the balance file or create it if it doesn't exist
if 'balances.txt' not in os.listdir():
    balance = 0
else:
    with open('balances.txt','r') as f:
        balance = float(f.readline())


def menu1(bal):
    print('\t\t','*'*10,f'Your current balance is: ${bal:,.2f}')

def menu2(bal):
    while True:
        withdraw = input('Enter the amount you wish to withdraw: ')
        
        try:
            return bal - float(withdraw)
        except:
            print('\t\t', withdraw,'is not a valid amount.')

def menu3(bal):
    while True:
        deposit = input('Enter the amount you wish to deposit: ')
        
        try:
            return bal + float(deposit)
        except:
            print('\t\t', deposit, 'is not a valid amount.')

def menu4(bal):
    with open('balances.txt','w') as f:
        f.write(str(bal))


while True:  
    # Print the menu options
    print("""
          Menu:
              1) View current balance
              2) Submit withdrawal
              3) Submit deposit
              4) Quit
          """)
    menu_option = input('\rEnter a menu option: ')
    
    # Call the option defined
    if menu_option == '1':
        menu1(balance)
    elif menu_option == '2':
        balance = menu2(balance)
    elif menu_option == '3':
        balance = menu3(balance)
    elif menu_option == '4':
        menu4(balance)
        print('Goodbye!')
        break
    # SECRET MENU OPTION
    elif menu_option == '1812':
        print(('='*50).center(100))
        print('WARNING: KILLING BALANCE RECORD'.center(100))
        print(f'ENDING BALANCE: ${balance:,.2f}'.center(100))
        print(('='*50).center(100))
        os.remove('balances.txt')
        break
    else:
        print('Input invalid')