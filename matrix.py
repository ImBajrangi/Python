a=int(input("Enter the number of rows: "))
b=int(input("Enter the number of columns: "))

matrix = []

for i in range(a):
    row = []
    for j in range(b):
        row.append(int(input(f"Enter element [{i+1}] [{j+1}]: ")))
    matrix.append(row)

print("The matrix is:")

for row in matrix:
    print(row)
