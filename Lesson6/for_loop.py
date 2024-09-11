
#when we know the range
#1..10
# -100 ..1000
# 0 .. 200 jumps 5

# x: int = 10
# while x <= 20:
#     print(x, end=" ")
#     x += 1
#
# i: int = 10
# while i <= 20:
#     print(i, end=" ")
#     i += 1

            #start, end, gap
# for i in range(10, 20 + 1, 1):
#     print(i, end=" ")

#write a for loop for all odd number between 7 and 39, same line

for x in range(7, 39 + 1, 2):
    print(x, end=" ")

print()

for y in range(50, 200 + 1, 10):
    print(y, end=" ")

print()

z: int = int(input("enter a number "))

for z in range(1, z + 1): # short way for z in range(z + 1)
    print(z, end=" ")

print()

n: int = int(input("enter a number"))
for n in range(0, n):
    print(float(n), end=" ")
    n += 0.5
    print(float(n), end=" ")

print()

num: int = int(input("enter a number"))
for i in range(0, num):
    print(float(i)+ 0.5, end=" ")

print()

for i in range(0, num * 2 + 1, 1):
    print(float(i / 2), end=" ")

