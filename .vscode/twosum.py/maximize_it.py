n=int(input("Enter the number of lists you want to create:"))
b=int(input("Enter the number you want to divide with:"))
a=[]
for _ in range(n):
    a.append([])
i=0
while i<n:
    g=int(input("Enter the element:"))
    a[i].append(g)
    c=input("Do you want to add more elements(y/n):")
    if c == "y":
        pass
    if c == "n":
        i=i+1
l=[]
char=0
while char<len(a):
    m=max(a[char])
    l.append(m)
    char=char+1
p=0
for f in l:
    f=f**2
    p=p+f
q=p%b
print(q)