#Write a Python program that accepts a word from the user and reverse it.

word = input("Input a word to reverse: ")

for char in range(len(word) - 1, -1, -1):       #using for loop
  print(word[char], end="")
