#!/usr/bin/python3
from password import generate_password

min_length = int(input("Enter the minimum length:\n"))
has_number = input("Do you want to have numbers (y/n)?\n").lower() == 'y'
has_special = input('''
Do you want to have special characters (y/n)\n
''').lower() == "y"
pwd = generate_password(min_length, has_number, has_special)
print(pwd)
