arr = list(map(int, input("Enter numbers separated by space: ").split()))
max_num = arr[0]
min_num = arr[0]
for i in arr:
    if i > max_num:
        max_num = i
for i in arr:
    if i < min_num:
        min_num = i
print("The maximum number is:", max_num)
print("The minimum number is:",min_num)