# #Hello i am sasidhar. Namaste 

# print("Hello World")

# a = -34

# b = 56.8
# c = 12/3

# v = 34j

# print(type(v))


# st = '122313`241423 asdadDsdF FGADFGAV'

# print(type(st))

# b = True

# t = False

# print(type(t))
 

# """Strings"""

# a = 65

# print(chr(a))

# a = "SHER"

# print(a[-2])

# a = 13

# if a > 10:
#     print("I will do task A")

# else:
#     print("I will do task B")

# money = int(input("Please provide me money!"))

# if money == 10:
#     print(" I will have a Chocobar Icecream")

# elif money == 20:
#     print("I will have a MangoDolly Icecream")

# elif money == 30:
#     print("I will have a Frosty Icecream")

# else:
#     print("I will have a Cone Icecream")


# a = int(input("Enter number A: "))
# b = int(input("Enter number B: "))

# if a > b:
#     print(f"The largest number is A = {a}")

# else:
#     print(f"The largest number is B = {b}")

# gender = input("Enter your gender as M or F: ")

# if gender == "M" or gender == "m":
#     print("Good Morning Sir!")

# elif gender == "F" or gender == "f":
#     print("Good Morning Mam!")

# else:
#     print("Invalid Gender")

# a = int(input("Enter a number: "))

# if a%2 == 0:
#     print(f"{a} is an Even Number")

# else:
#     print(f"{a} is an Odd Number")

# a = input("Enter your name: ")
# b = int(input("Enter age: "))

# if b >= 18:
#     print(f"Hey {a} you are a valid voter.")

# else:
#     print(f"Hey {a} you are not a valid voter. You can be a valid voter in {18-b} years")

# year = int(input("Enter the year: "))

# if year % 4 == 0:
#     if (year % 100 != 0) or (year % 400 == 0):
#         print(f"{year} is a Leap Year!")
#     else:
#         print(f"{year} is Not a Leap Year.")

# else:
#     print(f"The year {year} is not a leap year")

# a = range(1,21,1)

# for i in range(20,51):
#     print(i)

# for i in range(16,0,-1):
#     print(i)

# for i in range(-5,-16,-1):
#     print(i)

#lets print a table of 5

# for i in range(5,51,5):
#     print(i)

# for i in range(5,51,5):
#     print(f"5 x {i/5} = {i}")

# n = int(input("Which table you want to print: "))

# for i in range(n, (n*10)+1, n):
#     print(f"{n} x {int(i/n)} = {i}")

# a = "SHERIYANS TEACHES INDUSTRY THINGS"
# print(len(a))
# for i in range(0,len(a),1):
#     print(a[i])

# a = "SHERIYANS IS COOL"

# for i in a:
#     print(i)

# a = 1

# while a <= 30:
#     print(a)
#     a += 1

# def sum(a,b=45):
#     print(f"The sum of your numbers is {a+b}")

# sum(12)
# sum(45)

# def hello(name, age):
#     print(f"Your name is {name} and your age is {age}")

# hello(age = 22, name = "akarsh")

# def palindrome(st):
#     rev = ""
#     for i in range(len(st)-1, -1, -1):
#         rev = rev + st[i]
    
#     if rev == st:
#         print(f"{st} is a palindrome")
#     else:
#         print(f"{st} is a not a paplindrome")

# palindrome("NAMAN")
# palindrome("CURSOR")

# def hello():
#     return "hello how are you"

# hello()
# print(hello()) 

# a = [12,13,14,15,16,18,19]

# print(a[1:5:1])

# for i in range(len(a)):
#     print(a[i])

# for i in a:
#     print(i)

# a.append(19)
# a.append(20)
# a.insert(5,17)
# a.extend([21,22,23,24])
# a.remove(19)
# print(a)

a = {1,2,3,4,5}
b = {4,5,6,7,8}

s = a.union(b)
d1 = a.difference(b)
d2 = b.difference(a)
i = a.intersection(b)
sd = a.symmetric_difference(b)

print(s)
print(d1)
print(d2)
print(i)
print(sd)