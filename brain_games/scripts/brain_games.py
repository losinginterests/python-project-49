#!/usr/bin/env python3

def main():
    print('Welcome to the Brain Games!')
main()

def welcome_user():
    global name
    name = ''
    while name == '':
        print(f'May I have your name?', end = ' ')
        name = input()
        print(f'Hello, {name}!')
welcome_user()
