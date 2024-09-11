#input num from user until the num is positive
# while the user gave input of a negative num -- input again


# x: int = int(input("enter positive number: "))
#
# while  x <= 0:
#     print("this number is not positive")
#     x = int(input("enter a num"))
# print("finish")


# x: int = -1
#
# while  x <= 0:
#     print("this number is not positive")
#     x = int(input("enter a num"))
# print("finish")
# counter: int = 1
# x: int = int(input("enter a positive num"))
#
# if x <= 0:
#     counter = 2
#     x = int(input("enter pos num"))
# if x <= 0:
#     counter = 3
#     x = int(input("enter pos num"))
# if x <= 0 and counter < 3:
#     x = int(input("enter pos num"))

    #short way


# counter: int = 1
# x: int = int(input("enter a positive num"))
#
# while x <= 0 and counter < 3:
#     counter += 1
#     x = int(input("enter pos num"))
#
# if counter == 3:
#     print("too many failures..")
# else:
#     print(f"you did it! the num is {x}")

# counter: int = 1
# grade: int = int(input("enter your grade:"))
#
# while grade <= 55 and counter < 3:
#     counter += 1
#     print("take a course again")
#     grade = int(input("enter your grade"))
#
#     if grade <= 55:
#          print(" go home")
#     else:
#         print("you passed the course")



grade = -1
while grade < 0 or grade > 100:

        grade = int(input("Enter a grade (0-100): "))

print(f"Valid grade entered: {grade}")




