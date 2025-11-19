arr=list(map(int,input("Enter numbers separated by space: ").split()))
new_arr=[]
for i in arr:
    new_arr.append(pow(i,3))
print(new_arr)   