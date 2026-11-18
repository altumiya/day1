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

#movie ticket based on age and day

age = 25
day = "wednesday"

price = 200  if age >= 20 else 100
if day == "wednesday":
    price = price - 50
    #price -= 50

print("ticket price for you is", price )    

#score cards with exit()

score = 92
if score >= 101:
    print("score should be less than 101")
    exit()
if score >=90:
    grade = "A" 
elif score >=70:
    grade = "B"
elif score >=40:
    grade = "C"      
else:
    grade = "Fail"

print("Grade:", grade)      

#fruit ripening nested ifelse

fruit = ""
color ="yellow"

if fruit =="banana":
    if color == "yellow":
        print("ripened")
    elif color == "green":
        print("unriped")
    elif color == "brown":
        print("overripe")
    else:
        print("no fruits")  
else:
    print("no fruit is there")    

# coffee order  with concatanation
 
ordersize = "medium"
extra = False
if extra :
    coffee = ordersize + " coffee with extra hit"
else:
    coffee = ordersize + " coffee"
print("order :", coffee)

#password with len classmethod

password = "secure@13"

if len(password) < 6:
    strength = "weak and less than 6 characters"
elif len(password) >= 10:
    strength = "strong and bold"
else:
    strength = "medium"   

print("password strength is :" ,strength)

#leap year with operators

year = 2026

if(year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year , "is leap year")
else :
    print(year ,"not a leap year")    

# prax for last

species = "cat"
age = 4

if species == "dog":
    if age <=2:
        print("puppy food") 
    else:
        print("dog food")
elif species == "cat":
    if age > 5:
        print("senior cat food")
    else:
        print("kitten food")
else:
    print("no species found") 
