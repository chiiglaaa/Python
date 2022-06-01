#this is guess the number game but computer will choose the number and he will also try to found the number
#by using binary search algorithm.
import random
import time
time.sleep(0.5)
print("This is guess the number game but its fully automated. #chiiglaaa")

#computer will choose random number between 0-100

num = random.randint(0, 101)
print(f"So computer Choose {num}!")
#algorithm

count = 0
min_guess = 0
max_guess = 100
guess = 50
time.sleep(0.3)
print(guess)

while True:
    count += 1
    if guess == num:
        print(f"Computer found the number in {count} tries.")
        break
    elif guess > num:
        max_guess = guess - 1
        guess = (min_guess + max_guess) // 2
        print("Computer number is greater than the actual number.")
        print(guess)
        time.sleep(0.5)
    elif guess < num:
        min_guess = guess + 1
        guess = (min_guess + max_guess) // 2
        print("Computer number is lower than the actual number.")
        print(guess)
        time.sleep(0.5)
