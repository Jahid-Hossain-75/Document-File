# String---------
# name="Jahid Hossain"
# name2="Bejoy"
# print(name+" "+name2)




# 1+2+3+4+5....+N
# N(N+1)/2
# 10(10+1)/2=55

# N= 10
# sum=0
# for i in range(1,10):
#     sum=sum+i
# print(sum)





# subject = ['Mathematics_3', 'Chemistry', 'Social Science', 'Programming Essentials',
#            'Web Design', 'Graphics', 'IT Support']
#
# name = str(input("Enter Your Name: "))
# class_n = int(input("Enter Your Class: "))
# roll = int(input("Enter Your Roll: "))
#
# print("Enter The Subject Wise Mark")
# marks = []
# grade = []
# point = []
# for x in subject:
#     print(f"{x} marks:")
#     a = float(input())
#     marks.append(a)
#     if (a<=100 and a>=80):
#         grade.append("A+")
#         point.append(5.00)
#     elif (a<=79 and a>=70):
#         grade.append("A")
#         point.append(4.00)
#     elif (a<=69 and a>=60):
#         grade.append("A-")
#         point.append(3.50)
#     elif (a<=59 and a>=50):
#         grade.append("B")
#         point.append(3.00)
#     elif (a<=49 and a>=40):
#         grade.append("C")
#         point.append(2.50)
#     elif (a<=39 and a>=33):
#         grade.append("D")
#         point.append(2.00)
#     else:
#         grade.append("F")
#         point.append(0.00)
#
# total_marks = sum(marks)
# avearge = total_marks/len(subject)
# gpa = sum(point)/len(subject)
#
# # total_grade = []
# # for y in point:
# #     gpa = sum(point) / len(subject)
# #     print(f"{y} point:")
# #     if (point == 5.00):
# #         total_grade.append("A+")
# #     elif (point <= 5.00 and point >= 4.00):
# #         total_grade.append("A")
# #     elif (c <= 4.00 and c >= 3.50):
# #         total_grade.append("A-")
# #     elif (c <= 3.50 and c >= 3.00):
# #         total_grade.append("B")
# #     elif (c <= 3.00 and c >= 2.50):
# #         total_grade.append("C")
# #     elif (c <= 2.50 and c >= 2.00):
# #         total_grade.append("D")
# #     elif (c <= 32):
# #         total_grade.append("Fail")
# #     else:
# #         print("---")




# print()
# print()
# print()
# print(" "*26,"Model Polytechnic Institute, Jashore")
# print(" "*31, "-"*26)
# print(" "*31, "Semester Final Exam Result")
# print(" "*16, "-"*56)
# print(" "*16, "Student Name: "+name+";   Class:",class_n,";   Board Roll:",roll)
# print(" "*16, "-"*56)
# print(" "*17, "Subject", " "*14, "Mark", " "*6, "Grade", " "*6, "Point")
# print(" "*16, "-"*11, " "*9, "-"*8, " "*2, "-"*9, " "*2, "-"*9)
#
# for i in range(len(subject)):
#     print(f"{' '*16} {subject[i].ljust(23)} {str(marks[i]).ljust(13)} {grade[i].ljust(10)} {point[i]}")
#
# print(" "*30, "-"*42)
# print(" "*16, "               Total  :",total_marks, " "*18, f"{round(gpa,2)}")
# print(" "*17, f"            Avearge  : {round(avearge,2)} %")
#
# if (marks[0]<=32) or (marks[1]<=32) or (marks[2]<=32) or (marks[3]<=32) or (marks[4]<=32) or (marks[5]<=32) or (marks[6]<=32):
#     print(" "*31, "Result : Fail")
# else:
#     print(" "*31, "Result : Pass")



# n= 1
# for i in range(0,5):
#     for j in range(0, i+1):
#         print(n, end=" ")
#         n = n+1
#     print()



# red = 7
# blue = 8
#
# blank = red
# red = blue
# blue = blank
#
# print('a:', red ,'b:',blue)


# swap two values without third variable
# red = 7
# blue = 8
#
# red = red + blue
# blue = red - blue
# red = red - blue
#
# print('a:', red ,'b:',blue)








# r = float(input("Enter Volume of Sphere radius: "))
# pai =3.1416
# area=(4/3)*pai*r*r
# area2=4*pai*r*r
# volume=(4/3)*pai*r*r*r
# print("Area: ",area)
# print("Area2: ",area2)
# print("Area: ",volume)
#
#
# print()
# print()
#
# r = int(input("Enter Your Number: "))
# if r%2 == 0:
#     print(r,"is a Even number")
# else:
#     print(r,"is a Odd number")


# f = open('myfile.txt', 'r')
# x = f.read()
# print(x)






# year= int(input("Enter the value of year: "))
#
# if (year%4==0 and year%100!=0) or (year%400==0):
#     print("This is a Leap year")
# else:
#     print("This is not a Leap year")



# নামতা
#
# num = int(input("Please inter the number: "))
# count = 1
# while count <= 10:
#     print(num, 'x', count, '=', num*count)
#     count += 1



# #1+3+5....+10
# def start():
#     i = 1
#     while i <=100:
#         print(i)
#         i = i + 2
#     print("Program End")
# start()



# a = 45
# b = 80
# c = 50
# if (a>b and a>c):
#     largest = a
# elif(b>a and b>c):
#     largest = b
# else:
#     largest = c
# print(largest)



# i = 0
# while i <=50:
#     print(i)
#     i = i + 7
# print("Program End")

# i = 0
# sum = 0
# for i in range(50):
#     print(i)
#     i+=7
# print("Program End")



# # N= 49
# sum=0
# for i in range(1,49):
#     sum+=i
# print(sum)




