# Problem-1: N is the sum of the numbers

# n = int(input("Enter a number: "))
# if n < 0:
#     print("Enter a positive number")
# else:
#     sum = 0
#
#     while(n > 0):
#         sum += n
#         n -= 1
#     print("The sum is = ",sum)



# Problem-2: Celsius conversion program to Fahrenheit

# celsius = float(input("Please enter the celsius Temperature: "))
# fahrenheit = (celsius * 1.8)+32
# print('%0.1f degree Celsius is = %0.1f degree Fahrenheit' %(celsius,fahrenheit))



# Problem-3: Circle Area Determination Program

# import math
# radius = float(input("Please entert the radius of a circle: "))
# Area = math.pi * radius * radius
# print("Area of circle is = %.2f" %Area)



# Problem-4: The smallest of the two numbers is the diagnostic program

# num1 = float(input("Please enter the 1st number: "))
# num2 = float(input("Please enter the 2nd number: "))
# if (num1<num2):
#     print("Smallest number is = ",num1)
# else:
#     print("Smallest number is = ", num2)



# Problem-5: The largest of the three numbers is the diagnostic program

# num1 = float(input("Please enter the 1st number: "))
# num2 = float(input("Please enter the 2nd number: "))
# num3 = float(input("Please enter the 3rd number: "))
# if (num1 >= num2) and (num1 >= num3):
#     largest = num1
# elif (num2 >= num1) and (num2 >= num3):
#     largest = num2
# else:
#     largest = num3
# print("The largest number among", num1, ",",num2, ",",num3,"is =",largest)



# Problem-6: A program to determine whether an English year is a leap year with value input

# year = int(input("Please enter the value of year: "))
# if ((year%4==0 and year%100!=0) or (year%400==0)):
#     print("This is a leap year")
# else:
#     print("This is not a leap year")



# Problem-7: A program to determine whether a number is prime.

# def prime(n):
#     if n > 1:
#         for i in range(2, n):
#             if (n % i) == 0:
#                 print(n, "is not a prime number")
#                 print("Because", i, "times", n // i, "is", n)
#                 break
#         else:
#             print(n, "is a prime number")
#     else:
#         print(n, "is not a prime number")
# num = int(input("Enter a number: "))
# prime(num)



# Problem-8: The following is the beating program

# n = 1
# for i in range(0, 5):
#     for j in range(0, i+1):
#         print(n, end=" ")
#         n = n+1
#     print()
