a= int(input("Enter 1st No. : "))
b= int(input("Enter 2nd No. : "))
c= int(input("Enter 3rd No. : "))

if((a>b) and (b>c)):
    print("A is Max")
elif((b>a) and (a>c)):
    print("B is Max")
else:
    print("C is Max")

if((a<b) and (a<c)):
    print("A is Smallest")
elif((b<a) and (b<c)):
    print("B is Smallest")
else:
    print("C is Smallest")
