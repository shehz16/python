list_of_names = ["Alice", "Bob", "Charlie", "David", "Eve", "shehz"]
print("shehz" in list_of_names)
print("Frank" not in list_of_names)

print("Enter the marks obtained by the student:")
mark1 = int(input("Enter the marks for subject 1: "))
mark2 = int(input("Enter the marks for subject 2: "))
mark3 = int(input("Enter the marks for subject 3: "))
mark4 = int(input("Enter the marks for subject 4: "))

total_marks = mark1 + mark2 + mark3 + mark4
avg_marks = total_marks / 4
print("Total Marks:", total_marks)
print("Average Marks:", avg_marks)

valid_Range = range(0, 101)
if avg_marks not in valid_Range:
    print("Average marks are not within the valid range.")
if avg_marks in range(90, 101):
    print("Average Range are within the valid range.")
    print("Grade: A")
elif avg_marks in range(80, 90):
    print("Average Range are within the valid range.")
    print("Grade: B")
elif avg_marks in range(70, 80):
    print("Average Range are within the valid range.")
    print("Grade: C") 
else:
    print("Average marks are not within the valid range.")
    print("Grade: D")
