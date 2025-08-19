# Write a program to input two numbers(A & B) from the user and print the maximum element among A & B.

a = int(input("Enter A's Number: "))
b = int(input("Enter B's Number: "))

a= str(a)
b= str(b)
if(len(a)>len(b)):
    print("A's Number Of Elements Is Greater Than B's elements")
else:
    print("B's Number Of Elements Is Greater Than A's elements")
