##====================User inputs====================
import pandas as pd

x=pd.Series([int(input("Enter the First set Numbers: "))for i in range(4)])
y=pd.Series([int(input("Enter the Second set Number: "))for i in range(4)])

print("Adding of two numbers are: ")
print(x+y)
print("Subtraction of two numbers are: ")
print(x-y)
print("Multiplication of two numbers are: ")
print(x*y)
print("Division of two numbers are: ")
print(x/y)
print("Modulation of two numbers are: ")
print(x%y)

