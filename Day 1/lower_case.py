#Arrange String characters such that lowercase letters should come first
str="PyNaTive"
lower_case=[]
upper_case=[]
for i in str:
    if i.islower():
        lower_case.append(i)
    else:
        upper_case.append(i)
sort_string=''.join(lower_case + upper_case)
print("Arranging characters in lower case:")
print(sort_string)
