countdown=int(input("hom many days are there till your exam:"))
if countdown>=20:
    print("you still have", countdown, "days left, but you can't be careless. study at least 7 hours a day")
elif 10<countdown<20:
    print("oh no man", countdown, "days?then if you don't study atleast 8-9 hours a days, you're in deep trouble")
elif 2<countdown<=10:
    print("just study at least 13 hours day. don't ask why")
else:
    print("study when you're not eating, sleeping and doing your things. thats all i can say")