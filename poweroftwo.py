#Question 3: Power of Two
#Write a program that takes an integer as input and returns true if the input is a power of two.

while True:
    try:    #checks whethher the input is a number
        number = int(input("Enter the integer? "))
    except ValueError:
        print("Invalid number. Enter a number")

    while number % 2 == 0 : 
        number = number/2
    if number == 1:
        print("True")
        break
    elif number !=1:
        print("False")
        break
