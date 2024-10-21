n=int(input("Enter the length of your password:"))
password=input("Enter your password:")

if n<6:
        print(6-n)

for i in password:
    if "abcdefghijklmnopqrstuvwxyz" != i:
            print("a")
    if "ABCDEFGHIJKLMNOPQRSTUVWXYZ" !=i:
            print("A")
    if  "0123456789" !=i:
            print("1")
    if "!@#$%^&*()-+" != i:
            print("!")
                