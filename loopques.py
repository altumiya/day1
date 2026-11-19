# loop problems

numbers = [1, 2, -3, -4, 5, -1, -6, 7, 8, -9, 10,11]
positivenums = 0
for num in numbers:
    if num > 0 :
        positivenums += 1
print("final count of positive numbers", positivenums)  # 7 

# even numbers

n =15
sumeven = 0
for i in range(1,n+1):
    if i%2 == 0:
        sumeven +=1
print("sum of even numbers is:", sumeven) # 7

#table multiplier with continue method

number = 5
for i in range(1,11):
    if i ==5: 
        continue # skips the given iteration
    print(number, 'x', i, '=', number*i)


# reverse string
string = "python"
print(string[::-1]) #nohtyp

inputstr = "abhishek"
revstr = ""
for char in inputstr:
    revstr = char + revstr
print(revstr)    # kehsihab


# 1st non repeated character

inputstr1 = "teeter"

for char in inputstr1:
    if inputstr1.count(char) == 1:
        print("char is:", char) #r
        break #ends whole loop as when added teeteraabb the loops does not end at the intended character but will show the result

# factorial using while loop

original_number = 5
number = original_number
factorial = 1

while number > 0:
    factorial *= number
    number -= 1

print(f"factorial value of {original_number} is: {factorial}") # 120  

#input validation

while True:
    usernum = int(input("enter input from 1 to 10: "))
    if 1 <= usernum <= 10:
        print("correct number") # if 1 to 10 correct number will be printed
        break
    else:
        print("not a correct number") # if not from 1 to 10 this will be printed

# prime number check

primenum = 28
isprime = True

if primenum > 1:
    for i in range(2, int(primenum**0.5) + 1):
        if (primenum % i ) == 0:
            print(f"{primenum} is not a prime number")
            break
    else:
        print(f"{primenum} is a prime number")  
else:              
    print(f"{primenum} is not a prime number")