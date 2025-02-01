# Input and Output

# print("This is a print state")
## Data Types

## String - Text - "" / ''
name = "Anjar"
# print(name)
## Integer - Number Decimal
age = 20000
# print(age)
## Float
pi = 3.14
# print(pi)
## Boolean - True / False
is_student = True
# print(is_student)


# numbers is a list []
numbers = [1,2,3,4,5]
list2 = ["A", "B", "C", "Anjar", 80, 3.14, True]
# print(numbers)
# print(list2)
## Tuple ()
numbers = (1,2,3,4,5)
## Dictionary - Map

# Key - Value

student1 = {
    "name" : "Anjar",
    "Roll" : 5,
    "CGPA" : 3.50,
    "is_graduated": True
}

students = [
    {
        "name" : "Anjar",
        "Roll" : 5,
        "CGPA" : 3.50,
        "is_graduated": True
    },
    {
        "name" : "Anjar2",
        "Roll" : 5,
        "CGPA" : 3.502,
        "is_graduated": True
    },
    {
        "name" : "Anjar2",
        "Roll" : 5,
        "CGPA" : 3.503,
        "is_graduated": True
    }
]

## Input

# name = input("Enter your name: ")
# print(name)


## Data Types
## String - Text

name = "Anjar" # 0 -> A, 1 -> n, 2 -> j, 3 -> a, 4 -> r || -5 -> A, -4 -> n, -3 -> j, -2 -> a, -1 -> r : index -> value
# print(name[4])
# print(name[1:])
# print(len(name))

## Variable Naming Conventions
# snake_case
# CamelCase

name_of_student = "Anjar"
# nameOfStudentTwo = "Anjar"

name = "                      aNjAr KhAn             "
# name = name.strip(" ").lower()

# print(name)

# print(name.isnumeric())
first_name = "Anjar"
last_name = "Khan"

full_name = first_name + " " + last_name

# print(f"My first name is {first_name}\nLast name is {last_name}\nFull name is {full_name}")

# print(type(students))

## Integer, Float - numerical

roll = 5.02
# print(roll)
# print(type(roll))

## Boolean

is_student = True
# print(is_student)
# print(type(is_student))

## List, Tuple

numbers = [2,1,4,5,3]
# numbers_tuple = (1,2,3,4,5)
#
# print(numbers_tuple[-1])
# print(numbers_tuple[1:4])

# numbers_tuple[1] = 1
# numbers_tuple[-1] = 4
# print(numbers)

numbers.insert(1,5)
# print(numbers)


## Operators + , - , * , // , / , %

first_number = 5
second_number = 6

# print(f"The sum is: {first_number + second_number}")
# print(f"The summation is: {first_number - second_number}")
# print(f"The * is: {first_number * second_number}")
# print(f"The / is: {(first_number / second_number)}")
# print(f"The // is: {first_number // second_number}")
# print(f"The % is: {first_number % second_number}")

## Conditionals

# number = int(input("Enter a number: ")) # 5
#
# # if the number is less than 10 print less otherwise print more
# if number < 10: ## < , > , ==, <= , >=
#     print("Less")
# elif number == 5:
#     print("The number is 5")
# else:
#     print("More")

## Write a python program to evaluate grade

math_grade = int(input("Enter the mark you got:"))

if math_grade >= 80 or math_grade <= 90:
    print("You got A")
elif math_grade >= 70:
    print("You got B")
elif math_grade >= 60:
    print("You got C")
elif math_grade >= 50:
    print("You got D")
elif math_grade >= 40:
    print("You got E")
else:
    print("You failed")

## For loop While loop














