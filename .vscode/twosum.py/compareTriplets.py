def compareTriplets(a, b):
    # Write your code here
    c=0
    d=0
    i=0
    while i<len(a):
        if a[i]<b[i]:
            c=c+1
        if a[i]==b[i]:
            continue
        if a[i]>b[i]:
            d=d+1
        i=i+1
    e=[c,d]
    return e
                
a = list(map(int, input().rstrip().split()))

b = list(map(int, input().rstrip().split()))

result = compareTriplets(a, b)