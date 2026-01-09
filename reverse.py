a=int(input("Please Enter Number: "))
l=[int(i) for i in str(a)]
#print(l)
lis=[]
for i in range(len(l)):
    lis.append(l[len(l)-i-1])
#print(lis)
for i in lis:
    k=''.join(str(i))
print(k)
#-----------------------------------------------------------------------------------#
a=0
ans=0
while(a>0):
    ans=digit%10
    digit=digit*10 +ans//10
    a+=1
print(ans)
