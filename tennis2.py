# scan matches 
# built list of match object
# build list of player objects
# build a ranked list
# ToDo: 
# Error in line "x"
# Inconsistent matches
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

def compare_players(player_1,player_2,match_list):
   
    # compares games_won 
    if player_1.games_won>player_2.games_won:
        result=1
    elif player_1.games_won<player_2.games_won:
        result=-1
    else:
        #  in case of equal games_won look for specific match to get a correct placement
        found=False
        for match in match_list:
            if (match.name1==player_1 and match.name2==player_2) or (match.name2==player_1 and match.name1==player_2):
                if match.winner==player_1:
                    result=1
                else:
                    result=-1
                found=True
                break
        if found is False:
            # in case of not finding a match between the two players, default to first player
            result=1
    print(player_1.name,player_1.games_won,player_2.name,player_2.games_won,result)
    return result



def rankings(match_list,player_list):
    ranked_list=[]
    # create ranked list by adding from player_list
    for player in player_list:
        print("inserting",player.name)
        if len(ranked_list)==0:
            ranked_list.append(player)
        else: 
            
            # new player has more wins than everybody on the list
            if compare_players(player,ranked_list[0],match_list)==1:
                ranked_list.insert(0,player)
                continue
            if compare_players(player,ranked_list[-1],match_list)==-1:
                ranked_list.append(player)
                continue
            # start a loop and look for insertion point
            for i in range(len(ranked_list)):      
                player_ranked=ranked_list[i]        
                if i+1<len(ranked_list):
                    player_ranked_next=ranked_list[i+1] 
                
                # insert player if score is in between the scores of other 2 players
                if compare_players(player,player_ranked,match_list)==-1 and compare_players(player,player_ranked_next,match_list)==1:
                    ranked_list.insert(i+1,player)
                    break
               
        
    return ranked_list

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
            

            
# main 
build_match_list()
print_match(match_list)
print("original list")
print_players(player_list)

ranking_list=rankings(match_list,player_list)
print("ranked list")
print_players(ranking_list)

output_path = 'output.txt'
output_text = open(output_path, "w")
for player in ranking_list:
    output_text.writelines(player.name+" ")
output_text.close()
