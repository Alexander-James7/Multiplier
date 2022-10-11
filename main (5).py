# Created by: Alexander James
# Created on: 2022/10/11
# This program calculates multiplication by looping addition 
print("Let's do multiplication")
x = int(input("What is your first number?: "))
y = int(input("What is your second number?: "))

a = 0

while y > 0:
  a += x 
  y -= 1
print("The final answer is "+str(a))


  

