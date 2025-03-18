# Simple Interest Calculation
P = float(input("Enter Principal Amount "))
R = float(input("Enter Interest Rate (%) "))
T = float(input("Enter Time "))

A = P * (1 + (R / 100) * T)
print("\nSimple Interest Amount", A)

# Compound Interest Calculation
n = int(input("\nEnter number of times interest is compounded per year "))

A = P * (1 + R / (n * 100)) ** (n * T)
print("Compound Interest Amount", A)

# Annuity Plan Calculation
PMT = float(input("\nEnter Payment per Period "))

A = PMT * ((1 + R/(n * 100)) ** (n*T) - 1) / (R/(n * 100))
print("Annuity Plan Amount", A)
