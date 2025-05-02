print("Choose the type of equation to solve:")
print("1. Quadratic (Ax² + Bx + C = 0)")
print("2. Cubic (Ax³ + Bx² + Cx + D = 0)")
print("3. Quartic (Ax⁴ + Bx³ + Cx² + Dx + E = 0)")

choice = input("Enter 1, 2, or 3: ")

# Quadratic Solver
if choice == "1":
    A = float(input("Enter A: "))
    B = float(input("Enter B: "))
    C = float(input("Enter C: "))

    D = B * B - 4 * A * C  # Discriminant

    if D > 0:
        x1 = (-B + (D ** 0.5)) / (2 * A)
        x2 = (-B - (D ** 0.5)) / (2 * A)
        print("Roots:", x1, "and", x2)
    elif D == 0:
        x = -B / (2 * A)
        print("One Root:", x)
    else:
        print("No real roots")

# Cubic Solver
elif choice == "2":
    A = float(input("Enter A: "))
    B = float(input("Enter B: "))
    C = float(input("Enter C: "))
    D = float(input("Enter D: "))

    # Step 1: Find a simple root using trial and error
    found = False
    for r in range(-10, 11):
        if A * r**3 + B * r**2 + C * r + D == 0:
            print("One root found:", r)
            found = True
            break

    if found:
        # Step 2: Reduce to a quadratic equation using synthetic division
        B_new = B + (A * r)  # New B
        C_new = C + (B_new * r)  # New C
        D_new = D + (C_new * r)  # New D (should be 0)

        # Step 3: Solve the quadratic equation
        discriminant = B_new**2 - 4 * A * C_new
        if discriminant > 0:
            x1 = (-B_new + (discriminant ** 0.5)) / (2 * A)
            x2 = (-B_new - (discriminant ** 0.5)) / (2 * A)
            print("Other roots:", x1, "and", x2)
        elif discriminant == 0:
            x = -B_new / (2 * A)
            print("Other root:", x)
        else:
            print("Other roots are complex numbers.")
    else:
        print("No simple integer root found")

# Quartic Solver
elif choice == "3":
    A = float(input("Enter A: "))
    B = float(input("Enter B: "))
    C = float(input("Enter C: "))
    D = float(input("Enter D: "))
    E = float(input("Enter E: "))

    # Step 1: Find a simple root using trial and error
    found = False
    for r in range(-10, 11):
        if A * r**4 + B * r**3 + C * r**2 + D * r + E == 0:
            print("One root found:", r)
            found = True
            break

    if found:
        # Step 2: Reduce to a cubic equation using synthetic division
        B_new = B + (A * r)
        C_new = C + (B_new * r)
        D_new = D + (C_new * r)
        E_new = E + (D_new * r)  # Should be 0

        # Step 3: Find another simple root using trial and error
        found_second = False
        for s in range(-10, 11):
            if A * s**3 + B_new * s**2 + C_new * s + D_new == 0:
                print("Second root found:", s)
                found_second = True
                break

        if found_second:
            # Step 4: Reduce to a quadratic equation
            B_final = B_new + (A * s)
            C_final = C_new + (B_final * s)
            D_final = D_new + (C_final * s)  # Should be 0

            # Step 5: Solve the quadratic equation
            discriminant = B_final**2 - 4 * A * C_final
            if discriminant > 0:
                x1 = (-B_final + (discriminant ** 0.5)) / (2 * A)
                x2 = (-B_final - (discriminant ** 0.5)) / (2 * A)
                print("Other roots:", x1, "and", x2)
            elif discriminant == 0:
                x = -B_final / (2 * A)
                print("Other root:", x)
            else:
                print("Other roots are complex numbers.")
        else:
            print("No second simple integer root found")
    else:
        print("No simple integer root found")

else:
    print("Invalid choice! Please enter 1, 2, or 3.")
