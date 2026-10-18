# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 21:30:36 2026

@author: Double-Y
"""
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")
def add(a, b):
    return (a + b)

def multi(a, b):
    return (a * b)
    
def sub(a, b):
        if a > b :
            return (a - b)
        elif a < b:
            return (b - a)
            

def div(a, b):
   if a > b :
       return (a / b)
   elif a < b:
       return( b / a)

if operator == "+":
    print("Result:", add(num1, num2))
elif operator == "-":
    print("Result:", sub(num1, num2))
elif operator == "*":
    print("Result:", multi(num1, num2))
elif operator == "/":
    print("Result:", div(num1, num2))
else:
    print("Invalid operator")