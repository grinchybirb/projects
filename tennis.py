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

global err_flg
err_flg=False 



def game():
    flag = True
    x_score=0
    y_score=0
    global x_win
    global y_win
    global i_game
    global line_count
    global err_flg
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
            if x-x_score>1:
                print("Error: X moved up score by more than 1")
                output_text.writelines("Error at line {}".format(line_count))
                err_flg=True
                break
            else:
                x_score=x

            if y-y_score>1:
                print("Error: Y moved up score by more than 1")
                output_text.writelines("Error at line {}".format(line_count))
                err_flg=True
                break
            else:
                y_score=y

            if x==11 and x-y>2:
                print("X won game number", i_game+1)
                x_win +=1
                break

            if y==11 and y-x>2:
                print("Y won game number", i_game+1)             
                y_win +=1
                break
    return


game_limit=5
win_limit=2
for i_game in range(1,game_limit+1):
    print("\nstarting game:",i_game)
    game()
    if err_flg is True:
        break
    print("x has won:",x_win, "y has won:",y_win)
    
    if x_win==win_limit:
        print("X has won by winning", x_win)
        break
    if y_win==win_limit:
        print("Y has won by winning", y_win)
        break
    
if err_flg is False:
    output_text.writelines("Correct")

output_text.close()
   

file_text.close()