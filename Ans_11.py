arr=list(map(int,input("Enter First list :").split()))
arr2=list(map(int,input("Enter First list :").split()))
new_arr=[]
for i in range(len(arr)):
    new_arr.append(arr[i]+arr2[i])
print(new_arr)    
    
