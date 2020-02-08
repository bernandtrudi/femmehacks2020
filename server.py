
import os
import math
from flask import Flask, request, render_template, jsonify

# Support for gomix's 'front-end' and 'back-end' UI.
app = Flask(__name__, static_folder='public', template_folder='views')


P = int(input("Enter starting principle please. $"))
n = int(input("Enter number of compounding periods per year. "))
r = float(input("Enter annual interest rate. e.g. 15 for 15% "))
y = int(input("Enter the amount of years. "))

FV = P * (((1 + ((r/100.0)/n)) ** (n*y)))

FV = round((FV), 2)


print("The final amount after", y, "years is $", FV)

#This is to calculate years

P = int(input("Enter starting principle please. $"))
n = int(input("Enter number of compounding periods per year. "))
r = float(input("Enter annual interest rate. e.g. 15 for 15% "))
FV = int(input("Enter final amount wanted."))

a = FV/P

b = 1 + (r/100)/n

#y = log(a)/(log(b) * n)


print("It would take you", y, "years to get $", FV)