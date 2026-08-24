a=int(input(""))
b=int(input(""))
tool=input("choose what u want(+,-,*,/): ")
if tool=="+":
    ans=a+b
elif tool=="-":
    ans=a-b
elif tool=="*":
    ans=a*b
elif tool=="/":
    ans=a/b
else:
    ans="error"
print(ans)