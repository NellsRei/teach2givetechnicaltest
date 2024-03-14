#Question 2: Fibonacci Sequence
#Write a program to generate the Fibonacci sequence up to 100.

n = 100
num1 = 0
num2 = 1
next_number = num2
i = 0
list =[]  #list to store the numbers

while i <= n:
    if i == 0:
        list.append(0)
    list.append(next_number)
    next_number = num1 + num2
    i+=1
    i = next_number
    num1, num2 =num2, next_number
print(list)