d fgd dgf import random

def roll():
    min_value=1
    max_value=6

    roll=random.randint(min_value,max_value)
    return roll
def players():
    num_players=int(input("Enter the number of players :"))
    player_names=[]nfnfn

    for i in range(num_players):
        name=input(f"Enter the name of player{i+1} :")
        player_names.append(name)
        
    return player_names;dfgdsg
        
    
print(players())

