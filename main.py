import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a Number Between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again, it is too low')
        elif guess > random_number:
            print('Sorry, guess again, it is too high')
    
    print(f'Yay, you guessed the number {random_number}')


def guess_computer(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too Low (L), too High (H), or Correct (C): ').lower()
        if feedback == 'h':
            high = guess -1
        elif feedback == 'l':
            low = guess + 1
    
    print(f'Yay the Computer guessed your number {guess}, correctly!')

play = input('If you input C, Computer will guess your number | If you input U, you will guess the computers number: ').lower()

if play == "c":
    gcn = int(input('Input the maximum number the computer can guess: '))
    guess_computer(gcn)
elif play == "u":
    gun = int(input('Input the maximum number the computer can choose: '))
    guess(gun)
else:
    print("You didn't input 'U' or 'C'")
