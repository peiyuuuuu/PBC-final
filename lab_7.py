"""
string = "New York"
for chr in string:
    print(chr, end=" ")
print()
for index, chr in enumerate(string):
    print(index, chr, end=" ")
print()
for index in range(len(string)):
    print(string[index], end=" ")
"""
# Practice 1
"""
str = input()
for i in range(len(str)):
    if str[i] == 'P' and (str[i+2] == 'B') and (str[i+4] == 'C'):
        print(str[i:i+5])
    else:
        pass
"""

# Practice 2
"""
def myStrip(s, e):
    a = s.strip(e)
    return a
b = myStrip('l-love-coco', 'col')
b = myStrip('dodoro', 'dor')
print(b)
"""

# Practice 3
"""
def myPalindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False
A = input()
print(myPalindrome(A))
"""

# Practice 4
"""
same = []
def LCS(str1, str2):
    for chr in str1:
        if chr in str2:
            same.append(chr)
    return same

A = input()
A = A.split(',')
str1 = A[0]
str2 = A[1]

for i in LCS(str1, str2):
    print(i, end="")
"""

# Practice 5

def nonAdjacent(str1):
    for i in range(len(str1)):
        if str[i] == str[i+1]:
        