# +
# -
# *
# /
# %
# **
# //
# +=
# -=
# *=
# /=
# a= 7
# a/=7
# a=a*7

# print(a)
# keyword= if, else, for, while....
# variable dec= [A-Za-z_]

# A =+ 7
# else= 7;



# a = 1
# b= 1.12
# c = "asjdhasdhgasd"

# print(type(c))

# assignment operator
# box = 12

# e =f=g= 4

# h,i,j = 7,8,"rafi"

# # print(j)



# a = 7 # Number
# b = "I wanna become a pythonista" #String

# c =['java', 'python','C', 'C++'] #list

# d = ('java', 'python',7) #tuple

# f = {"Rafiq": 80,"Robin":100} # Dictionary


# print(f['Rafiq'])

# print(str(7.12))


# num = 12
# print(num)

# num2 = 2.2
# print((num2))

# name= "Python"
# print((name))

# C/5 = F-32/9
# F = C*1.8+32

# celcius to Farenheit
# celcius = float(input("please enter the celcius temperature: "))
# farenheit = celcius*1.8 + 32
# print(f"{farenheit} F")

# Farenheit to Celcius
# f = float(input("please enter the Farenheit temperature: "))
# c = (f-32)/1.8
# print(f"{c} C")

# Chapter 4
# name = "Rabiul Alam Rafi"
# name1 = "Rafiq"
# print(name+" "+name1)

# Q: Write a python program,
# where a user can input his/her name
# and print the output as "Hi! Rafi. Good Morning"

# name = input("Enter your name: ")

# print(f"Hi {name}! Good Morning. ;)")
# print("_"*20)

# membership operator

# student = ['jahid', 'tahia', 'adfad', 'adfaad']

# if("jahid" in student):
#     print("is a student")
# else:
#     print("Not a Student")





# Lenght

# name = "Rabiul Alam Rafi"

# for i in range(len(name)):
#     print(name[i])

#Join function

# student = ['jahid', 'tahia', 'asiq', 'faizul']

# print(",".join(student))



# name = "Rafikul slam"
# student = ['jahid', 'tahia', 'asiq', 'faizul']

# print(len(name))

# print(student)
# print('\n'.join(student))

# #Replace
# print(name.replace(' ',''))

# #Strip
# name1 = name.strip("R")
# print(name.strip("R"))
# print(name1)


# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name.swapcase())


# name3 = "Rabiul Alam Rafi"

# print(name3.count('a'))

# print(name3.index('a',10))





# """Amr sadhfkajshdf
# adshfakjshdfjas"""


# # nationalAnthem = """
# #                     Amar sonar bangla
# #                     Ami tomay valobasi
# #                     Chirodin e tmr akash
# #                     tmr batash, amr pran
# #                     bajay basi.
# #                     """

# # print(nationalAnthem)
# #
# # for i in range(0,256):
# #     print(f"{i}--{chr(i)}")

# # tamil = u"இன்று அத்தியாவசிய வகுப்பை முன்னேற்றுகிறது"
# #
# # print(tamil)

# #GPA CALCULATOR

# # subject = ['python','web design', 'graphics Design', 'Math','Chemistry','IT Support','Social Science']
# #
# # print("Enter the corresponding subject wise grade: ")
# # grade=[]
# # for x in subject:
# #     print(f"{x} grade: ")
# #     a = float(input())
# #     grade.append(a)

# # gpa = float(sum(grade)/len(subject))

# # print(f"Your GPA is: {round(gpa,2)}")

# #FUNCTION

# # # assigning strings to the variables
# # left_alignment = "Left Text"
# # center_alignment = "Centered Text"
# # right_alignment = "Right Text"
# #
# # # printing out aligned text
# # print(f"{left_alignment : <20}{center_alignment : ^15}{right_alignment : >20}")

# # Python program to demonstrate
# # writing to file

# # Opening a file
# file1 = open('myfile.txt', 'w')
# L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
# s = "Hello\n"

# # Writing a string to file
# file1.write(s)

# # Writing multiple strings
# # at a time
# file1.writelines(L)

# # Closing file
# file1.close()

# # Checking if the data is
# # written to file or not
# file1 = open('myfile.txt', 'r')
# print(file1.read())
# file1.close()



# def add(x,y):
#     c = x+y
#     print(c)

# def sub(x,y):
#     c= x-y
#     print(c)
# add(5,6)
# sub(9,7)

# def addition(x):
#     c = sum(x)
#     print(c)

# x= [1,2,3,4,5,6,7,8,9]
# addition(x)


import time

# localtime = time.localtime()
# print(localtime)

# d = datetime.datetime.now()
# day= datetime.datetime.now()+timedelta(days=10)

# print(day)


#Find the area of a rectangle



# def Area(x,y):
#     area = .5*x*y
#     print(area)

# land = 10
# height = 8
# Area(land,height)



