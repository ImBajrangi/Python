a=int(input("Enter A's Number: "))
b=int(input("Enter B's Number: "))
c=int(input("Enter C's Number: "))

a=len(str(a))
b=len(str(b))
c=len(str(c))

if(a<b and a<c):
    print("A have Minimum Number Of Elements")
elif(b<a and b<c):
    print("B have Minimum Number Of Elements")
else:
    print("C have Minimum Number Of Elements")