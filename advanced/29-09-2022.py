# 1. Write a program to check if a Number is positive,negative or zero
def number(num):
    if num > 0:
        print(num," Positive number ")
    elif num < 0:
        print(num," Negative number ")
    else:
        print(num, " Zero ")

number(-9)


# 2.Write program check if a number is Odd or Even:

def number(num):
   if num % 2 == 0:
        print(num,"Even number")
   else:
        print(num,"Odd number")

number(9)


# 3. Write a Python Program to Check Leap Year?
def leap_year(year):
    if year % 4 == 0:
        if year % 400 == 0:
            if year % 100 ==0:
                print(year,"leap year")
            else:
                print(year,"not leap year")
        else:
            print(year,"leap year")
    else:
        print(year, "not leap year")

year = int(input("enter the year: "))
leap_year(year)


# 4. Write a Python Program to Check Prime Number?
def prime_number(num):
    for i in range(2,num):
        if num % i == 0:
            print("not prime number")
            break
    else:
        print("prime number")

# 1.What does an empty dictionary's code look like?
d = {}
print(type(d))

# 2. What is the value of a dictionary value with the key 'foo' and the value 42?
ans==> 42

# Q1. What is the purpose of Python's OOP?
    In python every thing is an object. by using OOP we can reuse the existing code by "inheritance". we can override methods
by using polymorphism.
