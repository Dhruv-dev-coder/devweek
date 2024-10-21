queries=['ab','aba','bc']
stringList=['aba','aba','ab']
i=0
b=len(queries)
while i<b:
    a=0
    for j in stringList:
        if queries[i]== j:
            a=a+1
    print(a)
    i=i+1
        