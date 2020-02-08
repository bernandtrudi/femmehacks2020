
x = int(input("How much are you planning on putting in your account?"))
y = int(input("What is the rate of interest?"))
z = int(input("What is the amount of money you want to reach?"))
n = 1 

# Balance  =Pe^rt 
# Balance = z P= x e= exponetial function rate= y time = n (years)
while x <= z:
  print(str(x) + "  at year " + str(n))
  x = round((x), 0)
  n += 1
  