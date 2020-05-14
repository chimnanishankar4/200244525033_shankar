'''
Given a number count the total number of digits in a number
For example: The number is 75869, so the output should be
Reverse the following list using for loop
'''
list1=[10,20,30,40,50]
count=0
for i in range(len(list1)-1,-1,-1):
    count+=1
    print(list1[i])
print("Count is:",count)
