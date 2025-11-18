str=input("Enter a String : ")
result_str=""
str2=str+str
for i in str2:
    if 'A'<= i <= 'Z':
        continue 
    elif i in 'aeiou':
        result_str+='#'
    else:
        result_str+=i    
print(result_str)        


