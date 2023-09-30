a=int(input("enter the current year:"))
b=int(input("enter the final year:"))

if a<b:
    print("list of leap year between",a,"to",b,"is:")
while a<b:
    if(a%4==0)&(a%100!=0):
        print(a)
    if(a%100==0)&(a%400==0):
        print(a)
    a=a+1
if a>=b:
    print("check your year input again")
