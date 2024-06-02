#!/usr/bin/python3
import random
import string


def generate_password(min_length, numbers=True, special_chars=True):
    letters = string.ascii_letters
    digits = string.digits
    special_chs = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_chars:
        characters += special_chs

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special_chs:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_chars:
            meets_criteria = meets_criteria and has_special

    return pwd
