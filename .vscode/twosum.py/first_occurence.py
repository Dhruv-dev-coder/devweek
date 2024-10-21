haystack=str(input("Enter a string:"))
needle=str(input("Enter another string:"))
i=0
j=0
a=len(haystack)
b=len(needle)
while i<=a:
    while j <=b:
        if i>j:
            if haystack[j]==needle[j]:
                i=i+1
                j=j+1
        if j>i:
            if haystack[i]==needle[i]:
                i=i+1
                j=j+1
        if i==j:
            if haystack == needle:
                i=i+1
                j=j+1
        if i>j:
            if haystack[j]!=needle[j]:
                print("-1")
        if j>i:
            if haystack[i]!=needle[i]:
                print("-1")
        if i==j:
            if haystack != needle:
                print("-1")

print(haystack[0:i])                       