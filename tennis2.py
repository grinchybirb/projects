class match_class:
    def __init__(self):
        print("new match")
        self.winner=None
class player_class:
    def __init__(self):
        print("new player")
        self.name=None
        self.games_won=None
        self.games_played=None
        self.last_match=None

match_list=[]
player_list=[]

def print_match(match_list):
    for match in match_list:
        print(match.name1,match.name2,match.s1,match.s2)

def print_players(player_list):
    for player in player_list:
        print(player.name,"games won",player.games_won,"games played",player.games_played)

# assume total number of players is n (each person plays n-1 games),
# assuming 2 matches are not played
#  leading to 2 possible final outcomes:
# case 1. 3 players (a,b,c), with n-3,n-2,n-2 games 
# case 2. 4 players (x,y,z,q), each with n-2 games
# also assuming each player has played at least one game, so the player_list is complete
def missing_games(player_list):
    case=2
    n_players=len(player_list)
    for player in player_list:
        if player.games_played==n_players-3:
            player_a=player
            case=1
        
    print("case",case)

def find_player(player_list,name):
    for player in player_list:
        if player==player.name:
            return player
    return None    

def player_update(player_list,name,games_won,last_match):
    player=None
    for i_player in player_list:
        if name==i_player.name:
            player=i_player        
            break
    if player==None:
        # new player inserted
        player=player_class()
        player.name=name 
        player.games_won=games_won
        player_list.append(player)
        player.games_played=1
    else:
        # existing player updated with latest score
        player.games_won=games_won  
        player.games_played +=1
    player.last_match=last_match

def build_match_list():
    file_path="input.txt"
    file_text=open(file_path,"r")

    line_count=0
    flag=True
    while flag:
        file_line = file_text.readline()
        line_count +=1
        if not file_line:
            print("End Of File")
            flag = False
        else:
            # print(file_line)
            str_line=str(file_line)
            if str_line[0]=="#":
                continue
            char_list=str_line.split(" ")
            # create new match object
            match=match_class()
            match.name1=char_list[0]
            match.name2=char_list[1]
            match.s1=int(char_list[2])
            match.s2=int(char_list[3])
            match_list.append(match)
            player1=find_player(player_list,match.name1)
            player2=find_player(player_list,match.name2)
            if player1==None:
                last_won_1=0
            else:
                last_won_1=player1.games_won
            if player1==None and player2==None:
                if match.s1==1:
                    match.winner=player1
                else:
                    match.winner=player2

            # check if player is in player_list and add if not present
            player_update(player_list,match.name1,match.s1,match)
            player_update(player_list,match.name2,match.s2,match)

build_match_list()
print_match(match_list)
print_players(player_list)
missing_games(player_list)