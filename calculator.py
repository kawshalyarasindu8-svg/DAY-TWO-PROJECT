# Grade Calculator

# Ask for student's name
name = input("Enter student's name: ")

# Ask for 3 subject marks
mark1 = float(input("Enter mark for subject 1: "))
mark2 = float(input("Enter mark for subject 2: "))
mark3 = float(input("Enter mark for subject 3: "))

# Calculate average
average = (mark1 + mark2 + mark3) / 3

# Show average
print("Student Name:", name)
print("Average:", average)

# Check pass or fail
if average >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")