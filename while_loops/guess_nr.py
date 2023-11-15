print('Guessing game!')
# Guess the correct number in 3 guesses. If you don't get it right after 3 guesses you lose the game
# Give user input box; 1 to capture guesses,
# print(and input boxes)
# 1. If user wins
# 2. If user loses
# Tip: remember you won't see print statements during execution, so if you want to see prints - print to the input box

#num = 12
#guess = 1
#guess_limit=3
#guess_nr = 0
#while guess_nr < guess_limit:
#    guess = int(input(f'Guess #{guess_nr+1} a number 1-20: last guess: {guess} '))
#    if guess == num:
#        print(f'You win! You guessed it: {guess}')
#        break
#    else:
#        print(f'No, not {guess}!')
#        guess_nr += 1
#if guess != num:
#   print(f'You lose! It was {num}')

# Modification 1: number 1-100, tell user if guess is too high/low, and let them have 5-10 guesses.
# Tip: remember you won't see print statements during execution, so if you want to see prints - print to the input box

num = 76
guess = 0
guess_limit=5
guess_nr = 0
guess = int(input(f'Guess a number 1-100: '))
guess_nr +=1
while guess_nr < guess_limit:

    if guess != num:
        guess_nr +=1
        if guess > num:
            guess = int(input(f'{guess} Too High! Try with a lower number 1-100!: '))
        else:
            guess = int(input(f'{guess} Too Low! Try with a higher number 1-100!: '))
    if guess == num:
        print(f'You win! You guessed it: {guess}')
        break

if guess != num:
    print(f'You lose! It was {num}')