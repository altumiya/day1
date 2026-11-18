# age related 
userage = int(input("enter the age :" ))

if userage > 60:
    print(userage, "is in elderly")
elif userage > 40:
    print("midlife")
elif userage > 20:
    print("adult")
else:
    print("underage")

#movie ticket based on age abd day

age = 25
day = "wednesday"

price = 200  if age >= 20 else 100
if day == "wednesday":
    price = price - 50
    #price -= 50

print("ticket price for you is", price )    