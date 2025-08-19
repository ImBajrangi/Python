a=int(input("Please Input Angle 1: "))
b=int(input("Please Input Angle 2: "))
c=int(input("Please Input Angle 3: "))

check_right=False
check_acute=False
check_obtuse=False
lis = [a,b,c]

for i in lis:
    if(i==90):
        check_right=True
    elif(i>90):
        check_obtuse=True
    elif(i<90):
        check_acute=True

if(check_right):
    print("Triangle Is Right Angled triangle")
elif(check_acute):
    print("Triangle Is Acute Angled triangle")
elif(check_obtuse):
    print("Triangle Is Obtuse Angled triangle")