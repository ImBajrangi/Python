def call():
    a3 = float(input("Input Daal De : "))
    if(a3>100):
        print("Not Valid")
    if(100>=a3>=90):
        print("A Grade")
    elif(90>a3>=80):
        print("B Grade")
    elif(80>a3>=70):
        print("C Grade")
    else:
        print("Fail Hego Tumharo Chhora")

for i in range(10):
    call()