n=int(input("How many numbers you want to add?:"))
nums=[]
for i in range(n):
    a=int(input("Enter the number"))
    nums.append(a)

target=int(input("Enter the sum you want:"))
for i in range(len(nums)):
    for j in range(len(nums)):
        if i != j:
            if nums[i]+nums[j] == target:
                x=[i,j]
print(x)