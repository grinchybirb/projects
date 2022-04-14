# run loop over games, check for correctness, and display results
# input values
file_path = 'input.txt'
file_text = open(file_path, "r")

# output values
output_path = 'output.txt'
output_text = open(output_path, "w")

global x_win
x_win=0

global y_win
y_win=0

global i_game

global line_count
line_count=0

global errgap_flg
errgap_flg=False 



def game():
    flag = True
    x_score=0
    y_score=0
    global x_win
    global y_win
    global i_game
    global line_count
    global errgap_flg
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




            x=int(char_list[0])
            y=int(char_list[1])
            print(x,y)
            if x-x_score>=1 and y-y_score>=1:
                print("Error: Both players moved up")
                output_text.writelines("Error at line {}".format(line_count))
                errgap_flg=True
                break
            if x-x_score>1:
                print("Error: X moved up score by more than 1")
                output_text.writelines("Error at line {}".format(line_count))
                errgap_flg=True
                break
            else:
                x_score=x

            if y-y_score>1:
                print("Error: Y moved up score by more than 1")
                output_text.writelines("Error at line {}".format(line_count))
                errgap_flg=True
                break
            else:
                y_score=y

            if x_score==11 and x_score-y_score>=2:
                print("X won game number", i_game+1)
                x_win +=1
                break

            if y_score==11 and y_score-x_score>=2:
                print("Y won game number", i_game+1)             
                y_win +=1
                break    

            if x_score>11 or y_score>11:
                if x_score-y_score>=2:
                    print("X won game number", i_game+1)
                    x_win +=1
                    break

                if  y_score-x_score>=2:
                    print("Y won game number", i_game+1)             
                    y_win +=1
                    break
            
    return


game_limit=5
win_limit=3
# run loop over amount of games played
for i_game in range(game_limit):
    print("\nstarting game:",i_game)
    game()
    if errgap_flg is True:
        break
    print("x has won:",x_win,"games", "y has won:",y_win,"games")
    
# post status
if errgap_flg is False:
    if x_win+y_win==game_limit:
        if x_win==win_limit:
            print("X has won by winning", x_win)
        if y_win==win_limit:
            print("Y has won by winning", y_win)
        output_text.writelines("Correct")
    else:
        output_text.writelines("Incomplete")

output_text.close()
file_text.close()