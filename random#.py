import random

number = random.randint(1,100)
number_of_guesses = 0
win = 0
greater = 'N.A'
less = 'N.A'
print(number)
while number_of_guesses < 5 and win == 0:
    ans = input("guess?")
    if int(ans) == number:
        print('correct')
        win = 1
    else:
        if ans == '<' or '>':
            if ans == '<':
                greater = input('greater than?')
                greater = int(greater)
                if greater < number:
                    print('yes')
                else:
                    print('no')
            if ans == '>':
                less = input('less than?')
                less = int(less)
                if less > number:
                    print('yes')
                else:
                    print('no')
        
        else:
            print('incorrect')
            number_of_guesses += 1
if win == 0:
    print('you lose.')
else:
    print('you win!')
            
