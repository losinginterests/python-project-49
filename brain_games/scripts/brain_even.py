from random import randint

print(f'Answer "yes" if the number is even, otherwise answer "no"')

i = 0
while i < 3:
    value = randint(0, 10)
    print(f'Question {value}')
    print('Your answer:', end = ' ')
    answer = input()
    if value % 2 == 0 and answer == 'yes':
        i += 1
        print('Correct!')
    elif value % 2 == 0 and answer != 'no':
        print('"no" is wrong answer ;(. Correct answer was "yes"')
        print(f"Let's try again")
    elif value % 2 == 1 and answer != 'yes':
        i += 1
        print('Correct!')
    elif value % 2 == 1 and answer == 'yes':
        print('"yes" is wrong answer ;(. Correct answer was "no"')
        print(f"Let's try again")
print(f'Congratulations!')
