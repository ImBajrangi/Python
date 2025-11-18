number=int(input("Enter a number :"))
list=[]
count=1
while count<=number:
    if(number%count==0):
        list.append(count)
    count+=1    
print(list)    