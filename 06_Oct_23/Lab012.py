# take input from user create calculator
#num1+num2
#num1-num2
#num1/num2
#num1*num2

'''
num1=input("Enter number 1\n")
num2=input("Enter number 2\n")
print(num1+num2)
# output is (23+12) output is 2312 why becoz it considerd 'input' function as string only hence it concanitate two nubers as string
print(type(num1))
# it will show type of num1 here is str
'''

num1=int(input("Enter number 1\n"))
num2=input("Enter number 2\n")
num2=int(num2)

print(num1+num2)
# now converted num1, num2 to type integer using function int() all calculation possible
print(num1-num2)
print(num1*num2)
print(num1/num2) # division always give Floating number in Python



