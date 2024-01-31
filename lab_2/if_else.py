a = 50
b = 10
if a > b:
    print("Hello World")
#Hello World

a = 50
b = 10
if a != b:
    print("Hello World")
#Hello World

a = 50
b = 10
if a == b:
    print("Yes")
else:
    print("No")
#No
    
a = 50
b = 10
if a == b:
    print("1")
elif a > b:
    print("2")
else:
    print("3")
#2

c = 22 #added because we didn't have it before
d = 22
if a == b and c == d:
    print("Hello")
#I added c and d, but the code won't print anything, because we do not have "else"

if a == b or c == d:
    print("Hello")
#the code won't print anything
    
if 5 > 2:
    print("YES")
#Yes

a = 2
b = 5
print("YES") if a == b else print("NO")
#NO

a = 2
b = 50
c = 2
if a == c or b == c:
    print("YES")
#YES