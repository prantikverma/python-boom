#GUESS GAME TUTORIAL
print("GUESSING GAME USING PYTHON : ")
guess_num=int(input("ENTER ANY NUMBER OF YOUR CHOICE :"))


import random
jackpot=random.randint(1,100)

while guess_num!=jackpot:

    if guess_num==jackpot:
        print("you won")

    elif guess_num!=jackpot:
        if guess_num>jackpot:
            print("guess smaller")
            guess_num=int(input("ENTER ANY NUMBER OF YOUR CHOICE :"))
            if guess_num==jackpot:
                    print("you won")
        else:
            print("guess larger")
            guess_num=int(input("ENTER ANY NUMBER OF YOUR CHOICE :"))
            if guess_num==jackpot:
                    print("you won")
# new one
jack=random.randint(1,10)
guess=int(input("enter eny number btwn 1 and 10 :"))
counter=1
while guess!=jack:
    if guess<jack:
        print("dream bigg buddy")
    else:
        print("think small number")
    guess=int(input("enter eny number btwn 1 and 10 :"))
    counter+=1
if guess==jack:
     print("your guess is incredible buddy")
print("IN SECOND GAME YOU GUESSES ABOUT",counter,"TIMES")