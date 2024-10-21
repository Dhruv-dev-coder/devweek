a=int(input("Enter an integer:"))
x=str(a)
b=list(x)
c=b[::-1]
if b == c:
    print("true")
else:
    print("false")