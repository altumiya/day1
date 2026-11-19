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