def calculate_avg_grades(students):
    sub_grades = {}
    for student in students:
        for subject, grade in student[1].items():
            if subject not in sub_grades:
                sub_grades[subject] = []
            sub_grades[subject].append(grade)
    avg_grades = {}
    for subject, grades in sub_grades.items():
        avg_grades[subject] = sum(grades) / len(grades)
    return avg_grades

def calculate_overall_avg(students):
    overall_avg = {}
    for student in students:
        name = student[0]
        grades = student[1].values()
        overall_avg[name] = sum(grades) / len(grades)
    return overall_avg

def main():
    students = []
    num_students = int(input("Enter the number of students: "))
    for _ in range(num_students):
        name = input("Enter student name: ")
        subjects = {}
        while True:
            subject = input("Enter subject (or type 'done' to finish): ")
            if subject.lower() == 'done':
                break
            grade = float(input(f"Enter grade for {subject}: "))
            subjects[subject] = grade
        students.append([name, subjects])
    avg_grades = calculate_avg_grades(students)
    overall_avg = calculate_overall_avg(students)
    print("\nAverage Grades by Subject:")
    for subject, avg in avg_grades.items():
        print(f"{subject}: {avg:.2f}")
    print("\nOverall average Grade for Each Student:")
    for name, avg in overall_avg.items():
        print(f"{name}: {avg:.2f}")
if __name__ == "__main__":
    main()