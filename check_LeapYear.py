#WAP to check whether a year is a leap year or not

a=int(input("Enter Year: "))
if(a%4==0 and not(a%100==0) or a%400==0):
    print("Year Is Leap Year.")
else:
    print("Yes is not Leap Year.")
