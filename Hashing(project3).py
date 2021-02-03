# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 13:16:48 2021

@author: sumanthsetty
"""


class HashTable:
    
    def __init__(self,size):
        self.size = size
        self.hash_table = self.create_buckets()
        
    
    def create_buckets(self):
        return [[] for _ in range(self.size)]
    
    def set_val(self,key,value):
        hashed_key = hash(key)%self.size
        bucket = self.hash_table[hashed_key]
        found = False
        for index, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                found=True
                break
        if found:
            bucket[index] = (key, value)
        else:
            bucket.append((key, value))
        
    def get_val(self,key):
        hashed_key = hash(key)%self.size
        bucket = self.hash_table[hashed_key]
        found = False
        for index, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                found=True
                break
        if found:
            return(record_value)
        else:
            return "No record found with that email"
    
    def del_val(self,key):
        hashed_key = hash(key)%self.size
        bucket = self.hash_table[hashed_key]
        found = False
        for index, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                found=True
                break
        if found:
            l = list((bucket[index]))
            l.remove(record_value)
            bucket[index] = l
            return(f"Removed value is {record_value}")
        else:
            return "No record found with that email"
        
        
        
        
    def __str__(self):
        return "".join(str(item) for item in self.hash_table)

hash_table = HashTable(1000)
print(hash_table)  
with open("data1.txt","r") as f:
    for line in f:    
        key, value = line.split(":")
        hash_table.set_val(key, value)
print(hash_table)
print(hash_table.get_val("mashrur@example.com"))

