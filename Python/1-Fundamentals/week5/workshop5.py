import random

def guess_random_number(tries,start,stop):
    random_num=random.randint(start,stop)
    while tries != 0:
        print(f"Tries remaining: {tries}")
        guess = input(f"Guess a number between {start} and {stop}: ")
        if int(guess) ==random_num:
            print("You guess the correct number!")
            return
        elif int(guess)<random_num: print("Guess lower!")
        else: print("Guess higher!")
        tries-=1
    print("You failed")
def guess_random_num_linear(tries,start,stop):
    random_num=random.randint(start,stop)
    print(f"The number to guess is: {random_num}")
    while tries > 0:
        guess = start
        print(f"Number of tries left: {tries}")
        print(f"The program is guessing... {guess}")
        if guess == random:
            print("The Program guessed correctly")
        start+=1
        tries-=1

def guess_random_num_binary(tries,start,stop):
    random_num=random.randint(start,stop)
    print(f"The number to find: {random_num}")
    while tries > 0 and stop>=start:
        mid = (start+stop)//2
        guess = mid
        if guess == random_num:
            print(f"Found it! {guess}")
            return
        elif guess < random_num:
            start=mid+1
            print("Guesing Higher")
        else:
            stop=mid-1
            print("Guesing Lower")
        tries-=1
    print("The program failed to find the number")

guess_random_number(5,0,10)
guess_random_num_linear(5,0,10)
guess_random_num_binary(5,0,100)