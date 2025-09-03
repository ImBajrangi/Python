# 1
# 1*3*
# 1*3*5
# 1*3*5*

for i in range(10):
    for j in range(i):
        if(j%2==0):
            print("*",end=" ")
        else:
            print(j,end=" ")
    print("")