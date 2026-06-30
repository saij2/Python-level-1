import random
import os
import time

words = [
    "apple", "banana", "orange", "grape", "mango",
    "car", "house", "phone", "computer", "school"
]

print("""
Difficulty:
1. Easy - 4 words
2. Medium - 5 words
3. Hard - 6 words
""")

choice = int(input("Choose Difficulty (1-3): "))

if choice == 3:
    n = 6
    difficulty = "Hard"
elif choice == 2:
    n = 5
    difficulty = "Medium"
else:
    n = 4
    difficulty = "Easy"


selected_words = random.sample(words, n)
# selected_words = ["cat","dog","tree","rock"]

time.sleep(1)
os.system("clear")


for word in selected_words:
    print(word)
    time.sleep(1)
    os.system("clear")

print("Memory Tester")
print("Difficulty:", difficulty)


guesses = input("Enter the words separated by commas: ").lower().split(",")


'''guesses = [word.strip() for word in guesses]'''


correct = 0
# 4,4
# range(start,end)
# range(1,11) start parameter is optional if you 
# dont provide it will start the sequence from 0 
# range(10) 0 to 9 
for i in range(len(guesses)):
    if guesses[i] == selected_words[i]:
        correct += 1


score = (correct / n) * 100
# print(guesses)
# print(selected_words)
'''
print("\nOriginal sequence:")
print(", ".join(selected_words))

print("\nYour answers:")
print(", ".join(guesses))
'''

print(f"Score: {score:.0f}%")
