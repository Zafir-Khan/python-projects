import random

#Rolling function
def roll():
    min_value = 1
    max_value = 6 
    roll = random.randint(min_value,max_value)

    return roll 

while True:
    players =input('Enter the number of players (2-4): ')
    if players.isdigit():
        players=int(players)
        if 2<= players <=4 :
            break
        else:
            print(" Must be between 2 - 4 players ! ")
    else:
        print("invalid input , try again :( ")

print(players)

max_score = 50
player_scores = [0 for _ in range(players)]

print(player_scores)

while max(player_scores ) < max_score:

    for players_index in range(players):
        print("\nPlayer number ",players_index + 1 , "turn has just started ! Please roll \n")
        print("your total score is ",player_scores[players_index],"\n")
        current_score  = 0 

        while True:
            should_roll= input("would you like to roll (y)? ")
            if should_roll.lower() != "y" :
                break

            value = roll()
            if value == 1:
                print("you rolled a 1 ! Your turn is done ! ")
                current_score = 0 
                break
            else :
                current_score += value 
                print("you have rolled a -> " , value )

            print("Your score is -> ", current_score )

        player_scores[players_index] += current_score
        print(" your total score is -> ", player_scores[players_index])

max_score=max(player_scores)
winning_index = player_scores.index(max_score)
print("Player number " ,winning_index + 1 , "is the winner with a score of -> " , max_score , "!") 