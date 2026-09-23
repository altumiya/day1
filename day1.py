# 1. Define the correct credentials
correct_username = "admin"
correct_password = "password123"

# 2. Take all inputs from the user
entered_username = input("Enter username: ")
entered_password = input("Enter password: ")
age = int(input("Enter age: "))
salary = float(input("Enter salary: "))

# 3. The Mega Nested IF-ELSE structure
if entered_username == correct_username:
    
    if entered_password == correct_password:
        
        if age >= 18:
            
            if salary > 50000:
                print("Account verified. Full access granted!")
            
            else:
                print("Rejected: Salary must be greater than 50,000.")
        
        else:
            print("Rejected: You must be 18 or older.")
            
    else:
        print("Rejected: Incorrect password.")

else:
    print("Rejected: Incorrect username.")