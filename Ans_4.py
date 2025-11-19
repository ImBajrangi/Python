arr=list(map(int,input("Enter numbers separated by space: ").split()))
num=int(input("Enter a number want to find the index :"))
for i in range(len(arr)):
    if(num==arr[i]):
        print(num,"index at",i)