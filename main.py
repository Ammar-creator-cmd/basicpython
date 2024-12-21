# More listing methods
'''list_a = [10, 20, 30, 40, 30]
count = list_a.count(30)
print(count)
index = list_a.index(40)
print(index)'''

#Report Card Generator Program
print("### Welcome to Report Card Generator ###\n")
all_subjects = ["Math", "Science", "English", "History", "Geography"]
report_cards = []
n_student = int(input("enter the nummber of students "))
for i in range(n_student):
    student_name = input(f"\n Enter the student {i +1}'s name :")
    marks = []
    print(f"please provide {student_name}'s grades for the following subjects:")
    for subject in all_subjects:
        grade = int(input(f"{subject}:"))
        marks.append(grade)
    student_record = [student_name] + marks
    report_cards.append(student_record)
# display the final report cads for each student
print("\n-----------------------------------")
print("Conratulations to all of the students!")
print("Here are your 1st term Master Report Cards:")

print("\n1st Term Report Cards:")
for student in report_cards:
    print(f"\nStudent Name: {student[0]}")
    for i in range(1, len(student)):
        print(f"{all_subjects[i-1]}: {student[i]}")