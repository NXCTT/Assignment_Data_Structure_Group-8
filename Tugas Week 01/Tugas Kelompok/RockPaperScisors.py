import random

Win_Score = int(input("Winning Score : "))
player_score = 0 
computer_score = 0

while player_score < Win_Score:
    print(f"Player({player_score}) : Computer({computer_score})")
    while True:
        try:
            player_input = int(input("Your Choise (1 = Rock, 2 = Paper, 3 = Scissor) : "))
            if player_input <= 3 and player_input >= 1:
                break
            else :
                print("Retry")
        except:
            print("Input Number 1-3")
            
    choise = ["Rock","Paper","Scissor"]

    player_choise = choise[player_input-1]
    computer_choise = choise[random.randint(0,2)]

    if player_choise == "Rock" and computer_choise == "Scissor":
        print("You Win!")
        print(f"Computer Choise : {computer_choise}")
        player_score += 1
    elif player_choise == "Scissor" and computer_choise == "Rock":
        print("You Lose!")
        print(f"Computer Choise : {computer_choise}")
        computer_score += 1
    elif player_choise == "Rock" and computer_choise == "Paper":
        print("You Lose!")
        print(f"Computer Choise : {computer_choise}")
        computer_score += 1
    elif player_choise == "Paper" and computer_choise == "Rock":
        print("You Win!")
        print(f"Computer Choise : {computer_choise}")
        player_score += 1    
    elif player_choise == "Scissor" and computer_choise == "Paper":
        print("You Win!")
        print(f"Computer Choise : {computer_choise}")
        player_score += 1
    elif player_choise == "Paper" and computer_choise == "Scissor":
        print("You Lose!")
        print(f"Computer Choise : {computer_choise}")
        computer_score += 1
    elif player_choise == computer_choise:
        print("Draw!")
        print(f"Computer Choise : {computer_choise}")
    
    if player_score == Win_Score:
        print("Congrats")

