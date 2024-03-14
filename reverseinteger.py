#Question 5: Reverse Integer
#Write a program that takes an integer as input and returns an integer with reversed digit ordering.

number = input("Enter a number? ")

if int(number) < 0:
    other = int(number) * -1
    other = str(other)[::-1]
    other = int(other) * -1
    print(other)
else:
    other = str(number)[::-1]
    other = int(other)
    print(other)

