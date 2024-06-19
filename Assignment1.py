
# Write a program that takes two numbers as input and prints their sum.
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
print("Sum is: ", n1 + n2)

# Write a python program that checks whether a given number is even or
# odd.
num = int(input("Enter num: "))
if num % 2 == 0:
    print("even")
else:
    print("odd")

# Write a python program that calculates the factorial of a given number.
n1 = int(input("Enter number : "))
fact = 1
while n1 > 0:
    fact *= n1
    n1 -= 1
print(n1)

# Write a program that asks the user for their name and then prints a
# greeting message.
name = input("Enter your name: ")
print("Hello, welcome", name)

# Write a program that takes a string input from the user and writes it to a
# text file.