#File Handling in python
#Group 4-Student IDs ending with 8 or 9
#Open students.txt file
file=open("std.txt","r")
#create output file
output=open("group_4.txt","w")
print("Selected Students:")
# Variable to count students
count = 0

# Variables for first and last student
first_student = ""
last_student = ""
<<<<<<< Updated upstream

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
=======
# Display total students
print("Total number of students:", count)

print()

# Display first student
print("First Student according to Student ID:")
print(first_student)

# Display last student
print("Last Student according to Student ID:")
print(last_student)

# Close files
file.close()
output.close()

print("group_4.txt file created successfully.")
>>>>>>> Stashed changes
