#This program replicate the rock-paper-scissor game 
import random

cpu_count=0
user_count=0
tie_count=0
game_played=0
while True: # game continue as long as user choose yes
    choices=["rock","paper","scissor"]
    cpu_choice=random.choice(choices)
    user=None
    while user not in choices:
        user=input("Please enter Rock, Paper, or Scissor: ").lower()
    print("\nComputer chose: "+ cpu_choice)
    print("You chose     : "+user)
    if cpu_choice==user:
        tie_count+=1
        print("Tie!")
        print("\n\nComputer wins: ",cpu_count)
        print("User wins     : ",user_count)
        print("Ties          : ",tie_count)
    elif cpu_choice=='rock':
        if user =='paper':
            user_count +=1
            print("You win!")
            print("\n\nComputer wins: ",cpu_count)
            print("User wins     : ",user_count)
            print("Ties          : ",tie_count)
        else:
            cpu_count+=1
            print("You lose!")
            print("\n\nComputer wins: ",cpu_count)
            print("User wins     : ",user_count)
            print("Ties          : ",tie_count)
    elif cpu_choice=='paper':
        if user == 'rock':
            cpu_count+=1
            print("You lose!")
            print("\n\nComputer wins: ",cpu_count)
            print("User wins     : ",user_count)
            print("Ties          : ",tie_count)
        else :
            user_count +=1
            print("You win!")
            print("\n\nComputer wins: ",cpu_count)
            print("User wins     : ",user_count)
            print("Ties          : ",tie_count)
    else:
        if user=='rock':
            user_count +=1
            print("You win!")
            print("\n\nComputer wins: ",cpu_count)
            print("User wins     : ",user_count)
            print("Ties          : ",tie_count)
        else:
            cpu_count+=1
            print("You lose!")
            print("\n\nComputer wins: ",cpu_count)
            print("User wins     : ",user_count)
            print("Ties          : ",tie_count)
    game_played+=1
    print("Game played  : ",game_played)
    continue_game= input("\nWould you like to continue(Y/N)").lower()
    
    if (continue_game!= "y" and continue_game!= "yes"):
        break
   
   
    
print("\n\t\t\tGood Game!\n")