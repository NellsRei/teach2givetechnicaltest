#Question 6: Count Vowels
#Write a program that counts the number of vowels in a sentence.

vowels = ["a","e","i","o","u","A","E","I","O","U"]
vowel_count = 0

text = input("Enter the text: ")
for char in text:
    if char in vowels:
        vowel_count +=1

print(vowel_count) 
