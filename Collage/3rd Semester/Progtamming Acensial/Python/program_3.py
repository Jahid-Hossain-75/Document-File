#variable
"""
name = "masud"
age = 19
gpa = 3.5
print("my name is "+name)
print("my name is "+name)
print("my age ",+age)
print("my ssc result ",+gpa)
"""

# +-*/ Oparators
"""
print(12 + 22)
print(12 - 22)
print(12 * 22)
print(12 / 22)
"""

# Backslash tag
"""
print("backspece \bline")
print("New \n line")
print("carriage \r reture")
print("may name \t is jahid")
print("backslash \\")
print("Single \' quote")
print("Dubole \" quote")
"""

#print("Alarm or \a beep")  #vul
#print("form \f feed")   #vul
#print("vartical \v tab")    #vul
#print("Question mark \?")   #vul
#print("octal \000 number")  #vul
#print("hexadecimal \xhh number ")   #vul
#print("Nul \0") #vul

# octal number
#x=0123
#print('Value is : ',+x)

# hexadecimal number
#x=0x25
#print('Value is :'+x)




# if else statement
"""
mark = 20

if mark >= 33:
    print("Pass")
else:
    print("Fail")
    
num1 = 15
num2 = 18

if num1>num2:
    print(num1)
else:
    print(num2)

num3 = 7

if num3%2 == 0:
    print("Even")
else:
    print("Odd")
"""


#elif statement.
"""
mark = 69

if mark>=80:
    print("A+")

elif mark>=70:
    print("A")

elif mark>=60:
    print("A-")

elif mark>=50:
    print("B")

elif mark>=40:
    print("C")

elif mark>=33:
    print("D")

else:
    print("Fail")
"""


#Inner If Statement
"""
if 7>8:
    if 7>2:
        print("Right")

    else:
        print("worng")
else:
    print("worng_2")
"""


#Ternary Oparetors
"""
num1 = 50
num2 = 10

max = num1 if num1>num2 else num2
print(max)
"""


#Logical Oparetors
"""
num1 = 60
num2 = 70
num3 = 40

if num2>num1 and num3>num1:
    print(num1)
elif num1>num2 and num3>num2:
    print(num2)
else:
    print(num3)
"""


#vowel - a,e,i,o,u
"""
ch = 'c'

if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
    print("Vowel")
else:
    print("Consonant")
"""


# While Loop
"""
i = 1
while i <=10:
    print(i)
    i = i + 1
print("Program End")

#+2
i = 2
while i <=20:
    print(i)
    i = i + 2
print("Program End")
"""



# Sum of numbers
#   1+2+3+.....+n
"""
sum = 0
i = 1
while i <= 10:
    sum = sum + i
    i = i + 1
print(sum)
"""

"""
#And    1+3+5+.....+n
sum = 0
i = 1
while i <= 10:
    sum = sum + i
    i = i + 2
print(sum)
"""


"""
#And    2+4+6+.....+n
sum = 0
i = 2
while i <= 10:
    sum = sum + i
    i = i + 2
print(sum)
"""


"""
#input sum of number
n = int(input("Enter the last Number : "))
sum = 0
i = 1
while i <= n:
    sum = sum + i
    i = i + 1
print(sum)
"""



#break and continue
"""
i = 1
while i <= 100:
    if i == 20:
        break
    print(i)
    i = i + 1
print("End")
"""


"""
i = 1
while i <= 100:
    print(i)
    i = i + 1
    if i == 20:
        break
print("End")
"""


"""
i = 1
while i <= 100:
    if i == 20:
        continue
    print(i)
    i = i + 1
print("End")
"""



"""
i=1
while i <= 100:
    print(i)
    i=i+1
    if i==20:
        continue
print("End")
"""


