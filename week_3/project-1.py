# Step 1: Store student data in lists

# Girls' data
girls = ["Evelyn", "Jessica", "Somto", "Edith", "Liza", "Madonna", "Waje", "Tola", "Aisha", "Latifa"]
girls_age = [17, 16, 17, 18, 16, 18, 17, 20, 19, 17]
girls_height = [5.5, 6.0, 5.4, 5.9, 5.6, 5.5, 5.6, 1.6, 0.5, 7.5]
girls_scores = [80, 85, 70, 60, 76, 66, 87, 95, 50, 49]

# Boys' data
boys = ["Chinedu", "Liam", "Wale", "Gbenga", "Abiola", "Kola", "Kunle", "George", "Thomas", "Wesley"]
boys_age = [19, 16, 18, 17, 20, 19, 16, 18, 17, 19]
boys_height = [5.7, 5.9, 5.8, 6.1, 5.9, 5.5, 6.1, 5.4, 5.8, 5.7]
boys_scores = [74, 87, 75, 68, 66, 78, 87, 98, 54, 60]

# Step 2: Combine both groups into one list
students = girls + boys
ages = girls_age + boys_age
heights = girls_height + boys_height
scores = girls_scores + boys_scores

# Step 3: Print the table header
print("Name       | Age | Height | Score")
print("--------------------------------")

# Step 4: Loop through each student and print their details
for i in range(len(students)):  # Loop through each student by index
    name = students[i]   # Get student name
    age = ages[i]        # Get student age
    height = heights[i]  # Get student height
    score = scores[i]    # Get student score

    # Print the data in a formatted way so that columns align
    print(f"{name:10} | {age:3} | {height:6} | {score:5}")
