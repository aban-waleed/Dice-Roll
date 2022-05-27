class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
import random

print(bcolors.WARNING + bcolors.BOLD + bcolors.UNDERLINE + "Dice Roller" + bcolors.ENDC)

#############################################################Functions
def standard_role():
  dices = []
  diceNum = 0
  
  number_of_dice = int(input(bcolors.BOLD + '\nEnter the dice amount:' + bcolors.ENDC))

  for values in range (1,number_of_dice +1):
    roll = random.randint(1,6)
    dices.append(roll)
    diceNum = diceNum + 1
    print (f"\nDice {diceNum} rolled {roll}")

  print(f"\n\nFor a total of: {sum(dices)}")

def guess_role():
  roll = random.randint(1,6)
  guess = int(input('\nWhats your Guess: 6/'))

  def guess_output():
    if guess == roll :
      print(f'Your guess {guess}, was correct!')
    else:
      print(f'\nDice rolled {roll}, your guess was wrong')


  if guess <= 6:
    guess_output()
  else:
    print(bcolors.FAIL + "\n\n[ERROR] PROGRAM TERMINATING")
    
def coop_role():
  roll = random.randint(1,2)

  user_one_guess = int(input("User 1, enter your guess:"))
  user_two_guess = int(input("User 2, enter your guess:"))

  print (f"\nDice rolled {roll}")


  if user_one_guess == roll:
    print (f"\n\nUser 1 guessed {user_one_guess} which was correct!")
  else:
    print (f"\n\nUser 1 guessed {user_one_guess}, which was incorrect!!")

  if user_two_guess == roll:
    print (f"\n\nUser 2 guessed {user_two_guess} which was correct!")
  else:
    print (f"\n\nUser 2 guessed {user_two_guess}, which was incorrect!")
  
######################################################################

option = int(input("\nSelect Option:\n[1] to start 'Roll Dice' program\n[2] to play 'Guess the Number'\n[3] to play 'Coop Number Guesser' \n\n"))

if option == 1:
  standard_role()
if option == 2:
  guess_role()
if option == 3:
  coop_role()
