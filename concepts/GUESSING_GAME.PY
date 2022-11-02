#Number Guessing Game Objectives:
import random
Art=""""
  \      \ |    |   \/     \\______   \_   _____/\______   \  /  _____/|    |   \_   _____//   _____//   _____/|   |\      \  /  _____/  
 /   |   \|    |   /  \ /  \|    |  _/|    __)_  |       _/ /   \  ___|    |   /|    __)_ \_____  \ \_____  \ |   |/   |   \/   \  ___  
/    |    \    |  /    Y    \    |   \|        \ |    |   \ \    \_\  \    |  / |        \/        \/        \|   /    |    \    \_\  \ 
\____|__  /______/\____|__  /______  /_______  / |____|_  /  \______  /______/ /_______  /_______  /_______  /|___\____|__  /\______  / 
        \/                \/       \/        \/         \/          \/                 \/        \/        \/             \/        \/       """                                                                                                                   

print(Art)
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

print("Welcme to the number guessing game")
difficulty=input("Enter the difficult you want enter E for easy and H for hard")
if difficulty=='E':
  CHANCES=10
else:
  CHANCES=6

chosen_no=random.randint(1,101)

guess=-1
while guess!=chosen_no or CHANCES!=0:
  guess=int(input("Enter your guess: "))
  if guess==chosen_no:
    print("Your guess is correct ,You Won !!")
  elif guess-chosen_no>15:
    print("Your guess is too high !!")
    CHANCES-=1
  elif guess-chosen_no<-15:
    print("Your guess if too low !!")
    CHANCES-=1
  if guess-chosen_no<15:
    print("Your guess was high try again !!")
    CHANCES-=1
  if guess-chosen_no>-15:
    print("Your guess was low try again !!")
    CHANCES-=1


