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
    print("list of matches")
    for match in match_list:
        print(match.name1,match.name2,match.games_won1,match.games_won2,"winner",match.winner.name)

def print_players(player_list):
    print("list of players")
    for player in player_list:
        print(player.name,"games won",player.games_won,"games played",player.games_played)

def rankings(match_list,player_list):
    ranked_list=[]
    
    for player in player_list:
        if len(ranked_list)==0:
            ranked_list.append(player)
        else:
                
            for i in range(len(ranked_list)):
                
                games_won_new=player.games_won
                games_won_ranked=ranked_list[i].games_won
                if i+1<len(ranked_list):
                    games_won_ranked_next=ranked_list[i+1].games_won
                else:
                    games_won_ranked_next=0
                if games_won_new<=games_won_ranked and games_won_new>=games_won_ranked_next:
                    ranked_list.insert(i+1,player)
                    break
                   
        
    return ranked_list
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
        if name==player.name:
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
    return player

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
            match.games_won1=int(char_list[2])
            match.games_won2=int(char_list[3])
            match_list.append(match)
            player1=find_player(player_list,match.name1)
            ranked_player=find_player(player_list,match.name2)
            if player1==None:
                last_won1=0
            else:
                last_won1=player1.games_won
            if ranked_player==None:
                last_won2=0
            else:
                last_won2=ranked_player.games_won

            # check if player is in player_list and add if not present
            player1=player_update(player_list,match.name1,match.games_won1,match)
            ranked_player=player_update(player_list,match.name2,match.games_won2,match)

            if last_won1<match.games_won1:
                match.winner=player1
            else:
                match.winner=ranked_player
            

            

build_match_list()
print_match(match_list)
print("original list")
print_players(player_list)
ranking_list=rankings(match_list,player_list)
print("ranked list")
print_players(ranking_list)
# missing_games(player_list)