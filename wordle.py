#!/bin/env python

import random

def getw():
    number = random.randrange(8915)
    f = open("wordle", "r")

    lines = f.readlines()

    palabra = lines[number][0:5]

    f.close()
    return palabra

def word(palabra):
    hp = 5
    while hp != 0:
        print('Enter a 5-letter word: ')
        guess = input()
        guess = guess.lower()
        if len(guess) != 5:
            print('That word has ' + str(len(guess)) + ' letters instead of 5!\n')
            continue
        else:
            for x in guess:
                if x not in palabra:
                    guess = guess.replace(x, '_')
            i = 0 
            if guess == palabra:
                print('\nU won!\n\n')
                break
            while i != 5:
                if guess[i] == palabra[i]:
                    guess = guess[:i] + guess[i].upper() + guess[i+1:]
                i += 1
            print(guess)
            hp -= 1
    if hp == 0:
        print('u lost! the word was ' + palabra + ' :(')
hint = '_ _ _ _ _'
print('\n' + hint + '\n\n')
    
palabra = getw()
word(palabra)
