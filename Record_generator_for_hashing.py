# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 13:16:01 2021

@author: sumanthsetty
"""


from random import choice
from string import ascii_lowercase as letters

list_of_domains = ['yaexample.com','goexample.com','example.com']

quotes = [  'Luck is what happens when preparation meets opportunity',
            'All cruelty springs from weakness',
            'Begin at once to live, and count each separate day as a separate life',
            'Throw me to the wolves and I will return leading the pack']

def generate_name(length):
    return ''.join(choice(letters) for i in range(length))

def generate_record(length, list_of_domains, total_records, list_of_quotes):
    with open("data1.txt","w") as to_write:
        for i in range(total_records):
            key = generate_name(length)+"@"+choice(list_of_domains)
            value = choice(quotes)
            to_write.write(key + ":" + value + "\n")
        to_write.write("mashrur@example.com:Don't let me leave Murph\n")
        to_write.write("evgeny@example.com:All I do is win win win no matter what!\n")

generate_record(10, list_of_domains, 1000, quotes)