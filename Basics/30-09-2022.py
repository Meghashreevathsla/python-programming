# ////QUESTION 1:.  Make a function that encrypts a given input with these steps:
# Input: "apple"
# Step 1: Reverse the input: "elppa"
# Step 2: Replace all vowels using the following chart:
# a => 0
# e => 1
# i => 2
# o => 2
# u => 3
# # "1lpp0"
# Step 3: Add "aca" to the end of the word: "1lpp0aca"
# Output: "1lpp0aca"////

# def encrypt(word):
#     y=[]
#     rev = word[::-1]
#     for i in rev:
#         if i == 'a':
#             y.append('0')
#         elif i == 'e':
#             y.append('1')
#         elif i == 'i' or i == 'o':
#             y.append('2')
#         elif i == 'u':
#             y.append('3')
#         else:
#             y.append(i)
#     a=''.join(y)
#     print(a+'aca')
#
# encrypt('apple')

# ///QUESTION 2: Given a list of words in the singular form, return a set of those words in the plural form
# if they appear more than once in the list.
# pluralize(["cow", "pig", "cow", "cow"]) ➞ { "cows", "pig" }

# pluralize = ["cow", "pig", "cow", "cow"]
# z=[]
# for i in pluralize:
#     y=pluralize.count(i)
#     if y >= 2:
#         z.append(i+'s')
#     else:
#         z.append(i)
# print(set(z))


# /// QUESTION 3: Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?///////

# for num in range(1,10000):
#     if num >=1:
#         for i in range(2,num):
#             if num % i == 0:
#                 break
#         else:
#             print(num ,end=' ')

# /// QUESTION 4: Write a Python Program to Find the Factorial of a Number?/////
# num = 8
# n = 1
# while num >= 1:
#     n = n * num
#     num -= 1
# print(n)

#///////// QUESTION 5: Write a Python Program to Display the multiplication Table?//////
# num = 2
# n = 1
# while n <= 10:
#     print(num*n, end=" ")
#     n += 1

# ///// QUESTION 6: Write a Python Program to Find the Sum of Natural Numbers? ////////
# num = 10
# y = 0
# while num >= 0:
#     y = num + y
#     num = num - 1
# print(y)


# QUESTION 7: What is the most significant distinction between a dictionary and a list?
#  Dict:
# unordered container of key,value pair, The elements are accessed via key-values.
#  List: unordered container of different objects. The elements are accessed via indexing

# //////Q8. How do you distinguish between a class object and an instance object?////
# class object declared at the class level and instance object defining at init level. we use instance method when objects
# has different character. when object has same character we use class method.

# /////Q9. What is the purpose of the __init__ method?
#   __init__ method is a constructor use to initialize the objects


