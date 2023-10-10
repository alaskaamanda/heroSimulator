 ##printing a welcome message

import random
import time
from time import sleep

print("Hello Hero!")
print("I'm Luna, your guide for today's adventure.")
time.sleep(2)
print("What is your name?")
name = input("> ")
time.sleep(1)
print(f'{name}...Hmmmm...')
time.sleep(2)
print("that sounds like the name of a hero")
time.sleep(1)
print("The city of py is in trouble and it needs a Lucky Hero to help!")
time.sleep(1)
print("Are you in? Yes or No?")
## prompt user for choice
gameStart = input("> ")
beginGame = "YES"
## introduction
if(gameStart.upper() == beginGame):
     print("Wonderful! Let us save the city of Py!")
     time.sleep(1)
     print("*LOUD RUMBLING*")
     time.sleep(3)
     print("Oh wow I think thats our first monster right now!")
     time.sleep(2)
     print("*Serpent like monster appears*")
     time.sleep(2)
     print("Quick! I have 4 chests! a red one, blue one, purple one and white one")
     time.sleep(2)
     print("inside is a mystery item that might help you!")
     time.sleep(2)
     print("Which color chest do you pick?")

 ##will prompt user to pick a colored chest
     firstChest = input("> ")
     serpentSlayer = 'RED'

     if (firstChest.upper() == serpentSlayer):
          print("Red Chest! inside it you will find a magical sword!")
          time.sleep(2)
          print(f'*{name} uses the sword to slay the Serpent*')
          time.sleep(2)
          print('Congratulations! you beat your first monster!!')
          time.sleep(2)
          print('the next challenge is a bit harder...')
          time.sleep(2)
          print('this next challenge is a game of chance!')
          time.sleep(2)
          print('before you is a magical crystal!')
          time.sleep(2)
          print('Upon touching the crystal you will be randomly assigned a weapon with a certain damage rate.')
          time.sleep(2)
          print('**RUMBLE**')
          time.sleep(2)
          print('OH NO!! the dragon is here! quick make a decision')
          time.sleep(2)
          print('do you dare touch the crystal? Yes or no?')
          userChoice = input('>')
          choiceChallenge = "YES"
          ##randomly assigns damage to magical weapon
          if (userChoice.upper() == choiceChallenge):
               Damage = [30, 40, 100, 150, 200, 250]
               dragonHealth = 200
               magicalWeapon = random.choice(Damage)
               slayedDragon = dragonHealth - magicalWeapon
               if (slayedDragon <= dragonHealth):
                    print('your weapon assigned was a scythe!')
                    time.sleep(2)
                    print(f'you did{magicalWeapon} Damage... the dragon has...')
                    time.sleep(2)
                    print(f'{dragonHealth} Health!')
                    time.sleep(2)
                    print(f'{name} you succesfully slayed the dragon!! thank you! for saving us!')  
          else:
               print("You did not touch the crystal....")
               print("you gave up and the land of Py burnt to the ground...")
               print("rip")
               quit()   
     else:
          print(f'{firstChest}.....oh that chest was empty.... oh no.')
          time.sleep(2)
          print('*The monster throws you across the land of Py')
          time.sleep(2)
          print('GAME OVER')
          gameStart == 0
##Exit Message
else:
    print("Good bye!")
    time.sleep(2)
    quit()