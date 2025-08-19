a2= int(input("Enter 1st Number : "))
b2= int(input("Enter 2nd Number : "))
c2= int(input("Enter 3rd Number : "))
d2= int(input("Enter 4th Number : "))
e2= int(input("Enter 5th Number : "))
print(list((a2,b2,c2,d2,e2)))
lis = list((a2,b2,c2,d2,e2))
leng = len(lis)
sum_me = 0
for i in lis:
    sum_me+=i
avg = sum_me/leng
print(f"Average Is: {avg}")