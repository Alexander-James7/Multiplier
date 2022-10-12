# Created by: Alexander James
# Created on: 2022/10/11
# This program calculates multiplication by looping addition 
print("Let's do multiplication")
x = int(input("What is your first number?: "))
y = int(input("What is your second number?: "))

a = 0

if y < 0 and x < 0:
# This line converts the negative integer to a postive by subtracting a negative with a negative, which means adding
  y2 = y - y - y
  x2 = x - x - x
  for z in range(y2):
    a += x2
    y2 -=1
else:
  for z in range(y):
    a += x
    y -= 1

print("Your final answer is "+str(a))

  