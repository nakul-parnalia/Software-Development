# Python program to take attendance with user input

# Step 1: Create an empty list to store student names
student_list = []

# Step 2: Ask the user how many students are in the class
num_students = int(input("Enter the number of students: "))

# Step 3: Input student names
for i in range(num_students):
    name = input(f"Enter the name of student {i + 1}: ")
    student_list.append(name)

# Step 4: Take attendance
attendance = {}  # Dictionary to store attendance status

for student in student_list:
    status = input(f"Is {student} present? (yes/no): ").strip().lower()
    if status == "yes":
        attendance[student] = "Present"
    else:
        attendance[student] = "Absent"

# Step 5: Display the attendance
print("\nAttendance Report:")
for student, status in attendance.items():
    print(f"{student}: {status}")
