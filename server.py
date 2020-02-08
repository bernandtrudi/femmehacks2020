x = int(input("How much are you planning on putting in your account?"))
y = int(input("What is the rate of interest?"))
n = int(input("What is the amount of "))
while x <= y:
  print(str(x) + "  at day" + str(n))
  x = round((x), 0)
  n += 1
  x += x*0.10