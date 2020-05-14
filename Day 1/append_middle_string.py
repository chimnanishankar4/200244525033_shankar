#Given 2 strings, s1 and s2, create a new string by appending s2 in the middle of s1
def appendmiddle(s1,s2):
    middleindex=int(len(s1)/2)
    print("Original Strings are:",s1,s2)
    middlethree=s1[:middleindex-1]+s2+s1[middleindex-1:]
    print("After appending new strings in middle:",middlethree)



appendmiddle("Chrisdem","IamNewString")
