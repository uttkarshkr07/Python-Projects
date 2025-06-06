import random

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


print("Welcome to the Rock Paper Scissors Game!\n")
your_turn = int(input("Press 0 for Rock, 1 for Paper and 2 for Scissors\n"))
turn = [rock, paper, scissors]
computer_turn = random.randint(0,2)
print("Your choice :\n" + turn[your_turn] + "\nComputer's choice :\n" + turn[computer_turn])
if turn[your_turn] == turn[computer_turn - 1]:
    print("You Lose")
elif turn[computer_turn] ==  turn[your_turn - 1]:
    print("You Win")
else:
    print("Draw")