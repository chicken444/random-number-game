import random
number = random.randint(1,100)
number_of_guesses = 0
win = 0
greater = 'N.A'
less = 'N.A'
while number_of_guesses < 5 and win == 0:
    ans = input("guess a number?")
    if ans == '<':
            greater = input('greater than?')
            greater = int(greater)
            if greater < number:
                print('yes')
                number_of_guesses += 1
            else:
                print('no')
                number_of_guesses += 1
    elif ans == '>':
            less = input('less than?')
            less = int(less)
            if less > number:
                print('yes')
                number_of_guesses += 1
            else:
                print('no')
                number_of_guesses += 1
    elif int(ans) == number:
        print('correct')
        win = 1
    else:
        print('incorrect')
        number_of_guesses += 1
if win == 0:
    print('you lose.')
else:
    print('you win!')
