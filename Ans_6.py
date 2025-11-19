arr=list(map(int,input("Enter numbers separated by space: ").split()))
sum_odd=0
sum_even=0
for i in range(len(arr)):
    if(arr[i]%2==0):
        sum_even=sum_even+arr[i]
    else:
        sum_odd=sum_odd+arr[i]    
print("Difference of Odd and Even Number is :",sum_odd-sum_even)