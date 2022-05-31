import random
import time

print("Hello. This is my first ever python project that i made by myself. #chiiglaaa")
print("")
time.sleep(1)
print("G U E S S   T H E   N U M B E R !")
print("")
time.sleep(1)
print("First of all choose your difficulty:")
time.sleep(1)
print("Easy (0-100)")
time.sleep(1)
print("Normal (0-10000)")
time.sleep(1)
print("Hard (0-1000000)")
time.sleep(2)
easy = "easy"
normal = "normal"
hard = "hard"

run = True
diff = ""
num = 0

while run:
    diff = str(input("Enter your difficulty: "))
    if diff.lower() == easy:
        num = random.randint(0, 100)
    elif diff.lower() == normal:
        num = random.randint(0, 10000)
    elif diff.lower() == hard:
        num = random.randint(0, 1000000)
    else:
        print("Error. Try again.")
    print(num)
    run = False
# Game Logic

count = 0

def valid_answer():
    while True:
        try:
            ans = int(input("Enter your guess: "))
        except ValueError:
            print("Wrong Value, Try Again.")
        else:
            return ans


while True:
    ans = valid_answer()
    count += 1
    if ans > num:
        print("Your guess is more than answer.")
    elif ans < num:
        print("Your guess is less than answer.")
    else:
        print(f"You guessed in {count} steps!!!")
        break
