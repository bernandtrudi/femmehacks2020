
import os
import math
from flask import Flask, request, render_template, jsonify

# Support for gomix's 'front-end' and 'back-end' UI.
app = Flask(__name__, static_folder='public', template_folder='views')



x = int(input("How much are you planning on putting in your account?"))
y = float(input("What is the rate of interest?(Input your rate in decimal form.)"))
z = int(input("What is the amount of money you want to reach?"))
n = 1 

# Balance  =Pe^rt 
# Balance = z P= x e= exponetial function rate= y time = n (years)

import math
x.append(1 - math.exp( -0.5 * (value1*value2)**2))

while x <= z:
  print(str(x) + "  at year " + str(n))
  x = round((x), 0)
  n += 1
  x == x* 2.7182818284590452353602874713527 ** y*n