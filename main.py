import random


while True:
   Options=('ROCK','PAPER','SCISSOR')
   computer=random.choice(Options)
   player=input("Enter your option (ROCK, PAPER, SCISSOR): ").upper()

   if player not in Options:
     print("Invalid choice! Please enter ROCK, PAPER, or SCISSOR.")
     continue
   
   print(f"Computer chose: {computer}")

   if computer==player:
     print("It's a tie!")
   elif player=="ROCK" and computer=="SCISSOR":
    print("You win!")
   elif player=="PAPER" and computer=="ROCK":
    print("You win!")
   elif player=="SCISSOR" and computer=="PAPER":
    print("You win!")
   else:print("You lose!")

   play=input("Play again? (y/n): ").lower()
   if play!="y":
     break