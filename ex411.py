import pyfiglet


def show():
  for row in game_board:
    for cell in row:
        print(cell, end="")      
    print()  

def check_game():
    if game_board[0][0]=="x " and game_board[0][1]=="x " and game_board[0][2]=="x ":
        print("player1 wins")
    if game_board[0][0]=="x " and game_board[1][0]=="x " and game_board[2][0]=="x ":
        print("player1 wins")

    if game_board[1][0]=="x " and game_board[1][1]=="x " and game_board[1][2]=="x ":
        print("player1 wins")

    if game_board[2][0]=="x " and game_board[2][1]=="x " and game_board[2][2]=="x ":
        print("player1 wins")

    if game_board[0][1]=="x " and game_board[1][1]=="x " and game_board[2][1]=="x ":
        print("player1 wins")

    if game_board[0][2]=="x " and game_board[1][2]=="x " and game_board[2][2]=="x ":
        print("player1 wins")

    if game_board[0][0]=="o " and game_board[0][1]=="o " and game_board[0][2]=="o ":
        print("player1 wins")

    if game_board[0][0]=="o " and game_board[1][0]=="o " and game_board[2][0]=="o ":
        print("player1 wins")

    if game_board[1][0]=="o " and game_board[1][1]=="o " and game_board[1][2]=="o ":
        print("player1 wins")

    if game_board[2][0]=="o " and game_board[2][1]=="o " and game_board[2][2]=="o ":
        print("player1 wins")

    if game_board[0][1]=="o " and game_board[1][1]=="o " and game_board[2][1]=="o ":
        print("player1 wins")
    if all(cell != '_' for row in Game for cell in row):
        print('Draw')
        exit()

    if game_board[0][2]=="o " and game_board[1][2]=="o " and game_board[2][2]=="o ":
        print("player1 wins")
title =pyfiglet.figlet_format("Tic Tac Toe", font="slant")
print(title)
game_board=[["- ","- ","- "], 
            ["- ","- ","- "],
            ["- ","- ","- "]]
show()
while True:
    print("Player1")
    while True:
        row= int(input())
        col= int(input())  
        if 0 <= row <= 2 and 0 <= col<=2:
            if game_board[row][col]=="- ":
                game_board[row][col]="x"   
                show()
                break
            else:
                print("another cell")
        else:
            print("Enter row and coiumn between 0 and 2")       
  
    print("Player2")
    while True:
        row= int(input())
        col= int(input()) 
        if 0 <= row<= 2 and 0 <= col<=2:
            if game_board[row][col]=="- ":
                game_board[row][col]="o"   
                show() 
                break
            else:
                print("another cell") 
        else:
            print("Enter row and coiumn between 0 and 2")      
check_game()