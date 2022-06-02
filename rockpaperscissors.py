import random
import time

#this is rock, paper, scissors game

print("There are three difficulties.")
print("Easy (you need 3 point to win)")
print("Normal (you need 5 point to win)")
print("Hard (you need 10 point to win)")
time.sleep(1)
diff = input("Choose your difficulty: ")

easy = "easy"
normal = "normal"
hard = "hard"
rock = "rock"
paper = "paper"
scissors = "scissors"
choises = ['rock', 'paper', 'scissors']
count = 0
op_count = 0
time.sleep(0.5)

while True:
    op_count += 1
    count += 1
    if diff.lower() == easy:
        if count == 4:
            print("You won!")
            time.sleep(3)
            break
        elif op_count == 4:
            print("You lose!")
            time.sleep(3)
            break
        randomer = random.choice(choises)
        user_input = input("Choose rock, paper or scissors: ")
        time.sleep(0.5)
        if user_input.lower() == rock and randomer == paper:
            count = (count - 1)
            print("Computer chose paper.")
            time.sleep(1)
            print(f"You lose this round. you have {count} point. Computer have {op_count} point.")
            time.sleep(0.5)
        elif user_input.lower() == rock and randomer == scissors:
            op_count = (op_count - 1)
            print("Computer chose scissors.")
            time.sleep(1)
            print(f"You won this round. you have {count} point. Computer have {op_count} point.")
            time.sleep(0.5)
        elif user_input.lower() == rock and randomer == rock:
            print("Computer chose rock.")
            time.sleep(1)
            count = (count - 1)
            op_count = (op_count - 1)
            print(f"Its draw. you have {count} point. Computer have {op_count} point.")
            time.sleep(0.5)
        elif user_input.lower() == paper and randomer == paper:
            print("Computer chose paper.")
            time.sleep(1)
            count = (count - 1)
            op_count = (op_count - 1)
            print(f"Its draw. you have {count} point. Computer have {op_count} point.")
            time.sleep(0.5)
        elif user_input.lower() == paper and randomer == rock:
            print("Computer chose rock.")
            time.sleep(1)
            op_count = (op_count - 1)
            print(f"You won this round. you have {count} point. Computer have {op_count} point.")
            time.sleep(0.5)
        elif user_input.lower() == paper and randomer == scissors:
            print("Computer chose scissors.")
            count = (count - 1)
            print(f"You lose this round. you have {count} point. Computer have {op_count} point.")
            time.sleep(0.5)
        elif user_input.lower() == scissors and randomer == scissors:
            print("Computer chose scissors.")
            time.sleep(1)
            count = (count - 1)
            op_count = (op_count - 1)
            print(f"Its draw. you have {count} point. Computer have {op_count} point.")
            time.sleep(0.5)
        elif user_input.lower() == scissors and randomer == paper:
            print("Computer chose paper.")
            time.sleep(1)
            op_count = (op_count - 1)
            print(f"You won this round. you have {count} point. Computer have {op_count} point.")
            time.sleep(0.5)
        elif user_input.lower() == scissors and randomer == rock:
            print("Computer chose rock.")
            count = (count - 1)
            print(f"You lose this round. you have {count} point. Computer have {op_count} point.")
            time.sleep(0.5)
    if diff.lower() == normal:
        if count == 6:
            print("You won!")
            time.sleep(3)
            break
        elif op_count == 6:
            print("You lose!")
            time.sleep(3)
            break
        randomer = random.choice(choises)
        user_input = input("Choose rock, paper or scissors: ")
        time.sleep(0.5)
        if user_input.lower() == rock and randomer == paper:
            count = (count - 1)
            print("Computer chose paper.")
            time.sleep(1)
            print(f"You lose this round. you have {count} point. Computer have {op_count} point.")
            time.sleep(0.5)
        elif user_input.lower() == rock and randomer == scissors:
            op_count = (op_count - 1)
            print("Computer chose scissors.")
            time.sleep(1)
            print(f"You won this round. you have {count} point. Computer have {op_count} point.")
            time.sleep(0.5)
        elif user_input.lower() == rock and randomer == rock:
            print("Computer chose rock.")
            time.sleep(1)
            count = (count - 1)
            op_count = (op_count - 1)
            print(f"Its draw. you have {count} point. Computer have {op_count} point.")
            time.sleep(0.5)
        elif user_input.lower() == paper and randomer == paper:
            print("Computer chose paper.")
            time.sleep(1)
            count = (count - 1)
            op_count = (op_count - 1)
            print(f"Its draw. you have {count} point. Computer have {op_count} point.")
            time.sleep(0.5)
        elif user_input.lower() == paper and randomer == rock:
            print("Computer chose rock.")
            time.sleep(1)
            op_count = (op_count - 1)
            print(f"You won this round. you have {count} point. Computer have {op_count} point.")
            time.sleep(0.5)
        elif user_input.lower() == paper and randomer == scissors:
            print("Computer chose scissors.")
            count = (count - 1)
            print(f"You lose this round. you have {count} point. Computer have {op_count} point.")
            time.sleep(0.5)
        elif user_input.lower() == scissors and randomer == scissors:
            print("Computer chose scissors.")
            time.sleep(1)
            count = (count - 1)
            op_count = (op_count - 1)
            print(f"Its draw. you have {count} point. Computer have {op_count} point.")
            time.sleep(0.5)
        elif user_input.lower() == scissors and randomer == paper:
            print("Computer chose paper.")
            time.sleep(1)
            op_count = (op_count - 1)
            print(f"You won this round. you have {count} point. Computer have {op_count} point.")
            time.sleep(0.5)
        elif user_input.lower() == scissors and randomer == rock:
            print("Computer chose rock.")
            count = (count - 1)
            print(f"You lose this round. you have {count} point. Computer have {op_count} point.")
            time.sleep(0.5)
    if diff.lower() == hard:
        if count == 11:
            print("You won!")
            time.sleep(3)
            break
        elif op_count == 11:
            print("You lose!")
            time.sleep(3)
            break
        randomer = random.choice(choises)
        user_input = input("Choose rock, paper or scissors: ")
        time.sleep(0.5)
        if user_input.lower() == rock and randomer == paper:
            count = (count - 1)
            print("Computer chose paper.")
            time.sleep(1)
            print(f"You lose this round. you have {count} point. Computer have {op_count} point.")
            time.sleep(0.5)
        elif user_input.lower() == rock and randomer == scissors:
            op_count = (op_count - 1)
            print("Computer chose scissors.")
            time.sleep(1)
            print(f"You won this round. you have {count} point. Computer have {op_count} point.")
            time.sleep(0.5)
        elif user_input.lower() == rock and randomer == rock:
            print("Computer chose rock.")
            time.sleep(1)
            count = (count - 1)
            op_count = (op_count - 1)
            print(f"Its draw. you have {count} point. Computer have {op_count} point.")
            time.sleep(0.5)
        elif user_input.lower() == paper and randomer == paper:
            print("Computer chose paper.")
            time.sleep(1)
            count = (count - 1)
            op_count = (op_count - 1)
            print(f"Its draw. you have {count} point. Computer have {op_count} point.")
            time.sleep(0.5)
        elif user_input.lower() == paper and randomer == rock:
            print("Computer chose rock.")
            time.sleep(1)
            op_count = (op_count - 1)
            print(f"You won this round. you have {count} point. Computer have {op_count} point.")
            time.sleep(0.5)
        elif user_input.lower() == paper and randomer == scissors:
            print("Computer chose scissors.")
            count = (count - 1)
            print(f"You lose this round. you have {count} point. Computer have {op_count} point.")
            time.sleep(0.5)
        elif user_input.lower() == scissors and randomer == scissors:
            print("Computer chose scissors.")
            time.sleep(1)
            count = (count - 1)
            op_count = (op_count - 1)
            print(f"Its draw. you have {count} point. Computer have {op_count} point.")
            time.sleep(0.5)
        elif user_input.lower() == scissors and randomer == paper:
            print("Computer chose paper.")
            time.sleep(1)
            op_count = (op_count - 1)
            print(f"You won this round. you have {count} point. Computer have {op_count} point.")
            time.sleep(0.5)
        elif user_input.lower() == scissors and randomer == rock:
            print("Computer chose rock.")
            count = (count - 1)
            print(f"You lose this round. you have {count} point. Computer have {op_count} point.")
            time.sleep(0.5)
