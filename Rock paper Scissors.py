user1 = input("Rock, paper or scissors? ")
user2 = input("Rock, paper or scissors? ") 

if (user1 == "Rock" or user1 == "rock") and (user2 == "paper" or user2 == "paper"):
    print("user2 wins")

if (user1 == "Rock" or user1 == "rock") and (user2 == "scissors" or user2 == "scissors"):
    print("user1 wins")

if (user1 == "paper" or user1 == "paper") and (user2 == "rock" or user2 == "rock"):
    print("user1 wins")

if (user1 == "scissors" or user1 == "scissors") and (user2 == "paper" or user2 == "paper"):
    print("user1 wins")

if (user1 == "Paper" or user1 == "paper") and (user2 == "scissors" or user2 == "scissors"):
    print("user2 wins") 

if (user1 == "scissors" or user1 == "scissors") and (user2 == "rock" or user2 == "rock"):
    print("user2 wins")

if (user1 == "rock" or user1 == "rock") and (user2 == "rock" or user2 == "rock"):
    print("its a tie")

if (user1 == "paper" or user1 == "paper") and (user2 == "paper" or user2 == "paper"):
    print("its a tie")

if (user1 == "scissors" or user1 == "scissors") and (user2 == "scissors" or user2 == "scissors"):
    print("its a tie") 

print("play again? ") 