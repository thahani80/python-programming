a=7
a=int(input("Enter a number:"))
factorial=1
if a<0:
  print("factorial doesn't exist for negative numbers:")
elif a==0:
  print("the factorial is 0 is 1")
else:
  for i in range(1,a+1):
      factorial=factorial*i
print("the factorial of",a,"is",factorial)
