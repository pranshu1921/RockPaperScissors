# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 17:25:10 2020

@author: Pranshu Kumar
"""

from random import randint

#creating play options list
t = ['Rock', 'Paper', 'Scissors']

#assigning random play to computer
computer = t[randint(0,2)]

#player set to False
player = False

while player == False:
    player = input("Rock, Paper, Scissors ?")
    if player == computer:
        print("Tie!")
    elif player == 'Rock':
        if computer == 'Paper':
            print("Oops! You lose", computer, 'covered', player)
        else:
            print("You win !", player)
    elif player == 'Paper':
        if computer == 'Scissors':
            print("You lose !", computer, 'cut you.')
        else:
            print('you win', player)
    elif player == 'Scissors':
        if computer == 'Rock':
            print("you lose")
        else:
            print("you win")
    else:
        print("Invalid play. Check spelling !")
        
    player = False
    computer = t[randint(0,2)]
            
