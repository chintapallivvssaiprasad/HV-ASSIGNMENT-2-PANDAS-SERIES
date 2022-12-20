##=================Default inputs================
import pandas as pd

set1 = pd.Series([5,2,9,7,10])
set2 = pd.Series([9,8,7,6,5,])

add = (set1+set2)
sub = (set1-set2)
mul = (set1*set2)
div = (set1/set2)
mod = (set1%set2)

print("Addition of two numbers: ")
print(add)
print("subtraction of two numbers: ")
print(sub)
print("Multiplication of two numbers: ")
print(mul)
print("Division of two numbers: ")
print(div)
print("Modulation of two numbers: ")
print(mod)







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

