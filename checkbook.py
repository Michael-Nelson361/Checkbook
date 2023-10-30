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
    f = open('balances.txt','w')
    f.write('0')
    f.close()
    balance = 0
else:
    with open('balances.txt','r') as f:
        balance = f.readline()


def menu1():
    print('Option 1 not yet available.')

def menu2():
    print('Option 2 not yet available.')

def menu3():
    print('Option 3 not yet available.')

def menu4():
    print('Option 4 not yet available.')
    
# Print the menu options
print("""
      Menu:
          1) View current balance
          2) Submit withdrawal
          3) Submit deposit
          4) Quit
      """)