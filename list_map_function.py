#Q1
list2=list(map(int,input("number of elements want to add in a list :").split()))
print(list2)
max=0
for i in list2:
    if i>max:
        max=i
print("Max Number is :",max)    


#Q2
list3=list(map(int,input("Enter a Elements :").split()))
target=int(input("Enter a Number :"))
count=0
print(list3)
for i in list3:
    if i==target:
        count+=1
print(target ,"comes in ",count,"times")      

#Q4
list4=list(map(int,input("Enter Elements :").split()))
print(list4)

for i in list4:
    if(i%2!=0):
        list4.pop(i)
print(list4)        


     





