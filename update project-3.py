# Grade Calculator with Continuous Execution

while True:
    name = input("\nEnter student's name (or type 'Exit' to stop): ")

    # Check if user wants to exit
    if name.lower() == "exit":
        print("Program stopped.")
        break

    # Ask for 3 subject marks
    mark1 = float(input("Enter mark for subject 1: "))
    mark2 = float(input("Enter mark for subject 2: "))
    mark3 = float(input("Enter mark for subject 3: "))

    # Calculate average
    average = (mark1 + mark2 + mark3) / 3

    print("Student Name:", name)
    print("Average:", average)

    # Assign grade
    if average >= 75:
        print("Grade: A")
    elif average >= 60:
        print("Grade: B")
    elif average >= 40:
        print("Grade: C")
    else:
        print("Result: Fail")