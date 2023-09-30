year=int(input("Enter year to be chechked:"))
if(year %4 == 0 and year % 100 == 0 or year % 400 ==0 ):
  print("The year is leap year!")
else:
    print("The yaer isn't a leap year")
