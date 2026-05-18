# Variable to count students
count = 0

# Variables for first and last student
first_student = ""
last_student = ""

# Read file line by line
for line in file:

    # Check if student ID ends with 8 or 9
    if line[-2] == "8" or line[-2] == "9":

        # Display student record
        print(line)

        # Store record in output file
        output.write(line)

        # Count total students
        count = count + 1

        # Store first student
        if count == 1:
            first_student = line

        # Store last student
        last_student = line