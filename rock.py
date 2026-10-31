
import os
import random
choice = ["rock","paper","scissors"]
player = input("Enter rock,paper,scissors:").lower()
computer = random.choice(choice)
print ("Computer choice:",computer)

if player == computer:
    print("It's a Draw!")
    
elif player == "rock":
     if computer == "scissors":
         print("Woww...You win!")
     else:
        print("Hmm... You lose!")
         
elif player == "paper":
    if computer == "rock":
        print("Woww...You win!")
    else:
        print("Hmm... You lose!")
                  
elif player == "scissors":
    if computer == "paper":
         print("Woww...You win!")
    else:
         print("Hmm... You lose!")
            
else:
    print("Invalid choice!")
        
folder_path =  r"C:\Users\Double-Y\desktop\python"

file_path = os.path.join(folder_path)

print("Save to :",folder_path)
            