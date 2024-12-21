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
print(report_cards)