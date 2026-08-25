a=int(input("enter your number: "))
d=0
while a>0:
    if a>=10:
        d=d+1
        a=a//10
    elif 1<=a< 10:
        d=d+1
        a=a//10
print("the number of digits in your number is:", d)