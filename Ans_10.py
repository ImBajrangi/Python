arr=list(map(int,input("Enter numbers separated by space: ").split()))
for i in range(len(arr)//2):
    arr[i],arr[len(arr)-1-i]=arr[len(arr)-1-i],arr[i]
print(arr)    



