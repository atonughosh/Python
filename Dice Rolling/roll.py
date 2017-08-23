'''
Program to simulate dice rolling.
Each roll generates a random number from 1 to 6.
Each number represents the sides of the dice.
'''
import random   #import random module

def roll():     #define the function to generate random number between 1 & 6
    print("Dice rolled : " + str(random.randint(1,6)) + " showed up.")

roll()
again = str(input("Roll again? (Y/N) \n"))     #check whether to roll again, take input and store in variable 'again'

#roll dice again if the uer enters Yes or yes or YES or Y or y else exit
while (again == "Y" or again == "y" or again == "yes" or again == "Yes" or again == "YES"):
    roll()
    again = str(input("Roll again? (Y/N) \n"))         #roll dice again if the uer enters Yes or yes or YES or Y or y
                                                    # else exit.

