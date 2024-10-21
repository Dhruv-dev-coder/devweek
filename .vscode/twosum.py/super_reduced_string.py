
#baab=bb=empty
#aaabccddd=abd
#aa=empty
s=str(input("Enter a string:"))

for i in s:
    if s.count(i) == 2:
        s.replace(i,'')
print(s)