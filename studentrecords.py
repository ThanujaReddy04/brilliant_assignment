import csv
# Function to read the CSV file and return student records
def read_csv(file_path):
    students = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            students.append({"name": row["name"], "age": int(row["age"]), "grade": float(row["grade"])})
    return students
# Function to calculate the average grade
def calculate_average_grade(students):
    total_grades = sum(student["grade"] for student in students)
    return total_grades / len(students)
# Function to find the student with the highest grade
def find_top_student(students):
    top_student = max(students, key=lambda student: student["grade"])
    return top_student
# Main function to execute the program
if __name__ == "__main__":
    file_path = 'students.csv'  # Path to the CSV file
    students = read_csv(file_path)
    
    if students:
        avg_grade = calculate_average_grade(students)
        top_student = find_top_student(students)
        
        print(f"Average grade of all students: {avg_grade:.2f}")
        print(f"Top student: {top_student['name']}, Grade: {top_student['grade']:.2f}")
    else:
        print("No student data found.")
