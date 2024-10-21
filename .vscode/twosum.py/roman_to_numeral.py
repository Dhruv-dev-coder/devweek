a=str(input("Enter roman numeral:"))
num=0
if "IV" in a:
    a=a.replace("IV","IIII")
if "IX" in a:  
    a=a.replace("IX","VIIII")
if "XL" in a:
    a=a.replace("XL","XXXX")
if "XC" in a:
    a=a.replace("XC","LXXXX")
if "CD" in a:
    a=a.replace("CD","CCCC")
if "CM" in a:
    a=a.replace("CM","DCCCC")


for i in a:
    if i == "M":
        num =num+1000
    if i == "D":
        num=num+500
    if i == "C":
        num=num+100
    if i == "L":
        num=num+50
    if i == "X":
        num=num+10
    if i == "V":
        num=num+5
    if i == "I":
        num=num+1
print(num)

     

