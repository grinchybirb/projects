class match_class:
    def __init__(self):
        print("new match")
class player_class:
    def __init__(self):
        print("new player")

match_list=[]
player_list=[]

def print_match(match_list):
    for match in match_list:
        print(match.name1,match.name2,match.s1,match.s2)

def print_players(player_list):
    for player in player_list:
        print(player.name,player.high_score)

# find each players final score
def final_score():
    for player in player_list:
        for match in match_list:
            if player.name==match.name1:
                player.high_score=match.s1
            if player.name==match.name2:
                player.high_score=match.s2
    

# add player object to player list
def player_add(player_list,name):
    player=None
    for i_player in player_list:
        if name==i_player.name:
            player=i_player
            break
    if player==None:
        player=player_class()
        player.name=name
        player_list.append(player)

def player_add2(player_list,name,high_score):
    player=None
    for i_player in player_list:
        if name==i_player.name:
            player=i_player
            break
    if player==None:
        # new player inserted
        player=player_class()
        player.name=name 
        player.high_score=high_score
        player_list.append(player)
    else:
        # existing player updated with latest score
        player.high_score=high_score  

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

            # check if player is in player_list and add if not present
            player_add2(player_list,match.name1,match.s1)
            player_add2(player_list,match.name2,match.s2)

build_match_list()
print_match(match_list)
# final_score()
print_players(player_list)
