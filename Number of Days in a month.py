month=int(input("Enter the month"))
year=int(input("Enter the year"))
if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
   print("Number of days are 31")
elif month==2 and year%4==0 or year%100==0 and year%400==0 :
       print("Number of days are 29")
elif month==2:
           print("Number of days are 28")
else:
    print("Number of days 30")
