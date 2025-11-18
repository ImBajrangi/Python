# for i in range(1,5):
#     print(chr(64+i)*i)

#  q1 reverse the order of the words
# q2 reverse the each word of the string

# sol1
st="py pr"
new_str=st.split()
new_str.reverse()
result=" ".join(new_str)
print(result)

#sol2
st="py pr"
print(st[::-1])

# q3 Check if given strings are anagrams or not 
# anagrams are words that contains the same characters but in different order 
s1="listen"
s2="silent"
if(sorted(s1)==sorted(s2)):
    print("Anagram")
else:
    print("Not Anagram")


    