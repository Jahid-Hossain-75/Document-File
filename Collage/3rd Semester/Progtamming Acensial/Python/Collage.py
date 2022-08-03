subject = ['Mathematics_3', 'Chemistry', 'Social Science', 'Programming Essentials',
           'Web Design', 'Graphics', 'IT Support']

name = str(input("Enter Your Name: "))
class_n = int(input("Enter Your Class: "))
roll = int(input("Enter Your Roll: "))

print("Enter The Subject Wise Mark")
marks = []
grade = []
point = []
for x in subject:
    print(f"{x} marks:")
    a = float(input())
    marks.append(a)
    if (a<=100 and a>=80):
        grade.append("A+")
        point.append(5.00)
    elif (a<=79 and a>=70):
        grade.append("A")
        point.append(4.00)
    elif (a<=69 and a>=60):
        grade.append("A-")
        point.append(3.50)
    elif (a<=59 and a>=50):
        grade.append("B")
        point.append(3.00)
    elif (a<=49 and a>=40):
        grade.append("C")
        point.append(2.50)
    elif (a<=39 and a>=33):
        grade.append("D")
        point.append(2.00)
    else:
        grade.append("F")
        point.append(0.00)

total_marks = sum(marks)
avearge = total_marks/len(subject)
gpa = sum(point)/len(subject)

# total_grade = []
# for y in point:
#     gpa = sum(point) / len(subject)
#     print(f"{y} point:")
#     if (point == 5.00):
#         total_grade.append("A+")
#     elif (point <= 5.00 and point >= 4.00):
#         total_grade.append("A")
#     elif (c <= 4.00 and c >= 3.50):
#         total_grade.append("A-")
#     elif (c <= 3.50 and c >= 3.00):
#         total_grade.append("B")
#     elif (c <= 3.00 and c >= 2.50):
#         total_grade.append("C")
#     elif (c <= 2.50 and c >= 2.00):
#         total_grade.append("D")
#     elif (c <= 32):
#         total_grade.append("Fail")
#     else:
#         print("---")

print()
print()
print()
print(" "*26,"Model Polytechnic Institute, Jashore")
print(" "*31, "-"*26)
print(" "*31, "Semester Final Exam Result")
print(" "*16, "-"*56)
print(" "*16, "Student Name: "+name+";   Class:",class_n,";   Board Roll:",roll)
print(" "*16, "-"*56)
print(" "*17, "Subject", " "*14, "Mark", " "*6, "Grade", " "*6, "Point")
print(" "*16, "-"*11, " "*9, "-"*8, " "*2, "-"*9, " "*2, "-"*9)

for i in range(len(subject)):
    print(f"{' '*16} {subject[i].ljust(23)} {str(marks[i]).ljust(13)} {grade[i].ljust(10)} {point[i]}")

print(" "*30, "-"*42)
print(" "*16, "               Total  :",total_marks, " "*18, f"{round(gpa,2)}")
print(" "*17, f"            Avearge  : {round(avearge,2)} %")

if (marks[0]<=32) or (marks[1]<=32) or (marks[2]<=32) or (marks[3]<=32) or (marks[4]<=32) or (marks[5]<=32) or (marks[6]<=32):
    print(" "*31, "Result : Fail")
else:
    print(" "*31, "Result : Pass")





