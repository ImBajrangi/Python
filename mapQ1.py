# Q1
arr=input()
A=list(map(int,arr.split()))
sum=0
for i in range(0,len(arr)+1):
    sum+=i
print("Sum is :",sum)    

#Q2
arr=input()
A=list(map(int,arr.split()))
max=0
for i in range(0,len(arr)+1):
    num=i%10
    if(num>max):
        max=i
print("Max Value is :",max)


