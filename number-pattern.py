# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4

for i in range(5):
    for j in range(5):
        if(j<i):
            print(j+1,end=" ")
    print()