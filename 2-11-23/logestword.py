def longestLength(a):
    max1 = len(a[0])
    temp = a[0]

    for i in a:
        if(len(i) > max1):
 
            max1 = len(i)
            temp = i
 
    print("The word with the longest length is:", temp,
          " and length is ", max1)


a = []
n=int(input("enter the size:"))
for i in range(0,n):
    b=input("enter the words:")
    a.append(b)
longestLength(a)
