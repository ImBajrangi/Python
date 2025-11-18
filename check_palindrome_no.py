number=int(input("Enter a Number :"))
dummy=number
length=len(str(number))
rev=0
for i in range(length):
    rem=number%10
    rev=rev*10+rem
    number=number//10
if(dummy==rev):
    print("Number is Palindrome")
else:
    print("Number is Not Palindrome")    