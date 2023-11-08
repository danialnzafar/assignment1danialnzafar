# Task 1: Shape Classification and Calculating Perimeter and Area

python
Copy code
# Prompt the user to input the length and breadth of the shape
length = float(input("Enter the length of the shape: "))
breadth = float(input("Enter the breadth of the shape: "))

# Check if it's a square or rectangle
if length == breadth:
    shape_name = "Square"
else:
    shape_name = "Rectangle"

# Calculate area and perimeter
if shape_name == "Square":
    side = length  # Since it's a square, length equals breadth
    area = side * side
    perimeter = 4 * side
else:
    area = length * breadth
    perimeter = 2 * (length + breadth)

# Display the results
print(f"This shape is {shape_name}")
print(f"The {shape_name} has Perimeter: {perimeter} and Area: {area}")

# Task 2: Cofounders List


# List of faculty members
faculty = ["Uzair", "Ali", "Samad", "Usman", "Saifullah"]

# Create an empty list for cofounders
cofounders = []

# Iterate through the faculty list to move "Usman" and "Saifullah" to cofounders
for name in faculty:
    if name == "Usman" or name == "Saifullah":
        cofounders.append(name)

# Remove "Usman" and "Saifullah" from the faculty list
faculty = [name for name in faculty if name not in cofounders]

# Display the results
print("Cofounders list:", cofounders)
print("Updated faculty list:", faculty)