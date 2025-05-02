# Step 1: Get user input for experience and age
experience = int(input("Enter years of experience: "))
age = int(input("Enter age: "))

# Step 2: Determine the ATR using if-elif conditions
if experience > 25 and age >= 55:
    atr = 5600000  # ATR for experience > 25 years and age >= 55
elif experience > 20 and age >= 45:
    atr = 4480000  # ATR for experience > 20 years and age >= 45
elif experience > 10 and age >= 35:
    atr = 1500000  # ATR for experience > 10 years and age >= 35
else:
    atr = 550000  # ATR for experience < 10 years and age < 35

# Step 3: Print the ATR result
print("Annual Tax Revenue (ATR) is: N", atr)
