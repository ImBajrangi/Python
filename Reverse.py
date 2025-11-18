list=[1,2,3,4,5,6]
n=len(list)
for i in range(0,n//2):
    list[i],list[n-1-i]=list[n-1-i],list[i]

print(list)    



