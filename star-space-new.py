# 12345
# 1234*
# 123**
# 12***
# 1****
# *****

n = 5

for i in range(n + 1):
    for j in range(1, n - i + 1):
        print(j, end="")
    for k in range(i):
        print("*", end="")
    print()