# from brain_games import name
from random import randint

def main():
    print(f'Answer "yes" if the number is even, otherwise answer "no"')

    i = 0 # Инициируем переменную, которая будет считать количество правильных ответов
    while i < 3:
        value = randint(0, 10) # Переменной присваивается случайное значение в виде целого числа, которое является вопросом для игрока.
        print(f'Question {value}')
        print('Your answer:', end = ' ')
        answer = input()
        if value % 2 == 0 and answer == 'yes':
            i += 1 # Т.к. ответ принят за верный, прибавляем к переменной i единицу.
            print('Correct!')
        elif value % 2 == 0 and answer == 'no':
            print('"no" is wrong answer ;(. Correct answer was "yes"')
            # print(f"Let's try again, {name}")
            print(f"Let's try again")
            i = 0 # Т.к. ответ не верный, обнуляем значение переменной i.
        elif value % 2 == 1 and answer == 'no':
            i += 1
            print('Correct!')
        elif value % 2 == 1 and answer == 'yes':
            print('"yes" is wrong answer ;(. Correct answer was "no"')
            # print(f"Let's try again, {name}")
            print(f"Let's try again")
            i = 0
    # print(f'Congratulations, {name}!')
    print(f'Congratulations!')


# print(f'Answer "yes" if the number is even, otherwise answer "no"')

# i = 0 # Инициируем переменную, которая будет считать количество правильных ответов
# while i < 3:
#     value = randint(0, 10) # Переменной присваивается случайное значение в виде целого числа, которое является вопросом для игрока.
#     print(f'Question {value}')
#     print('Your answer:', end = ' ')
#     answer = input()
#     if value % 2 == 0 and answer == 'yes':
#         i += 1 # Т.к. ответ принят за верный, прибавляем к переменной i единицу.
#         print('Correct!')
#     elif value % 2 == 0 and answer == 'no':
#         print('"no" is wrong answer ;(. Correct answer was "yes"')
#         # print(f"Let's try again, {name}")
#         print(f"Let's try again")
#         i = 0 # Т.к. ответ не верный, обнуляем значение переменной i.
#     elif value % 2 == 1 and answer == 'no':
#         i += 1
#         print('Correct!')
#     elif value % 2 == 1 and answer == 'yes':
#         print('"yes" is wrong answer ;(. Correct answer was "no"')
#         # print(f"Let's try again, {name}")
#         print(f"Let's try again")
#         i = 0
#     # print(f'Congratulations, {name}!')
# print(f'Congratulations!')
