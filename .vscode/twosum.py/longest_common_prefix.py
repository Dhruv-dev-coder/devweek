a=int(input("Enter how many elements you want to add?:"))
b=[]
for i in range(a):
    c=str(input("Enter the element:"))
    b.append(c)
for char in b:
    n=0
    while n<=len(char)-1:
        if char[n]==char[n]:
           n=n+1
           print(char[0:n:])
        else:
            print("")
    
   
        