arr=list(map(int,input("Enter numbers separated by space: ").split()))
for i in range(len(arr)):
    if(arr[i]<0):
        print(arr[i])