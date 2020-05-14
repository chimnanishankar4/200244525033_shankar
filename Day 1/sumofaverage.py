#Given a string, return the sum and average of the digits that appear in the string, ignoring all other characters
import re
input="English = 78 Science = 83 Math = 68 History = 65"
list1=[int(i) for i in re.findall(r'\b\d+\b',input)]
total_marks=0
for j in list1:
    total_marks+=j
per=total_marks/len(list1)
print("Total marks:",total_marsks)
print("Percentage is:",per)


