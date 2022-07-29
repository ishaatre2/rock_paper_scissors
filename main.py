rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

choice = int(input("Type 0 for rock, 1 for paper, and 2 for scissors."))

if choice == 0:
    print(rock)
if choice == 1:
    print(paper)
if choice == 2:
    print(scissors)

computer_choice = random.randint(0, 2)
print(f"Computer Chooses: {computer_choice}")
if computer_choice == 0:
    print(rock)
if computer_choice == 1:
    print(paper)
if computer_choice == 2:
    print(scissors)

#comparison
if choice == computer_choice:
    print("It's a draw")
if choice == 0:
  if computer_choice == 1:
    print("You win")
  if computer_choice == 2:
    print("Computer Wins")
elif choice == 1:
  if computer_choice == 2:
    print("You win")
  if computer_choice == 0:
    print("Computer Wins")
else:
  if computer_choice == 0:
    print("You win")
  if computer_choice == 1:
    print("Computer Wins")
  
  
  


