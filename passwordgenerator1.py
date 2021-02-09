#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import secrets

"""
Created on Sat Feb  6 11:59:36 2021

@author: wyatt
"""
password = ""
with open('chars.txt') as input_file:
    chars = [line.strip() for line in input_file]

length = int(input("Password Length? "))

if length <= 5:
    print('Not long enough to be secure. Please start program again.')
elif length > 5:
    print("generating...")
    while length > 0:
        password = password + secrets.choice(chars)
        length = length - 1
    print('password successfully generated:' + '\33[32m ' + password + '\033[0m')
print('')
input("ENTER to exit")