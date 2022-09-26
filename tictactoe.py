import random,sys,time
n=[j for j in range(1,10)]
board=[" "for i in range(9)]
def print_board():
    row1=("| {} | {} | {} |".format(board[0],board[1],board[2]))
    row2=("| {} | {} | {} |".format(board[3],board[4],board[5]))
    row3=("| {} | {} | {} |".format(board[6],board[7],board[8]))
    print("\t\t TIC-TAC-TOE")
    print("\t\t"+row1)
    print("\t\t-------------")
    print("\t\t"+row2)
    print("\t\t-------------")
    print("\t\t"+row3)
def player_move(icon):
    if(icon=="X"):
        number=1
    elif(icon=="O"):
        number=2
    print("Player {} Turn".format(number))
    choice1=int(input("Enter the choice between 1-9:").strip())
    if(choice1>0 and choice1<=9):
        if(board[choice1-1]==" "):
            board[choice1-1]=icon
            n.remove(choice1)
        else:
            print()
            print("Space...Taken :(")
            player_move(icon)
    else:
        print("Enter the correct choice between 1-9:")
        player_move(icon)
def player_movec(icon,mode):
    if(mode==1):
        n1=random.choice(n)
        print("Computer choice:",end=' ')
        time.sleep(1)
        print(n1)
        time.sleep(2)
        if(board[n1-1]==" "):
            board[n1-1]=icon
            n.remove(n1)
        else:
            print()
            print("Space...Taken :(")
            player_movec(icon)
    elif(mode==2):
        print("Computer choice:",end=' ')
        #n1 will be the board with space + 1 because the substition of icon will be placed as n1-1
        if((board[0]==board[1]==icon)and board[2]==" "):
            n1=2+1
        elif((board[0]==board[2]==icon)and board[1]==" "):
            n1=1+1
        elif((board[1]==board[2]==icon)and board[0]==" "):
            n1=0+1
        elif((board[3]==board[4]==icon)and board[5]==" "):
            n1=5+1
        elif((board[3]==board[5]==icon)and board[4]==" "):
            n1=4+1
        elif((board[4]==board[5]==icon)and board[3]==" "):
            n1=3+1
        elif((board[6]==board[7]==icon)and board[8]==" "):
            n1=8+1
        elif((board[6]==board[8]==icon)and board[7]==" "):
            n1=7+1
        elif((board[7]==board[8]==icon)and board[6]==" "):
            n1=6+1
        elif((board[0]==board[3]==icon)and board[6]==" "):
            n1=6+1
        elif((board[0]==board[6]==icon)and board[3]==" "):
            n1=3+1
        elif((board[3]==board[6]==icon)and board[0]==" "):
            n1=0+1
        elif((board[1]==board[4]==icon)and board[7]==" "):
            n1=7+1
        elif((board[1]==board[7]==icon)and board[4]==" "):
            n1=4+1
        elif((board[4]==board[7]==icon)and board[1]==" "):
            n1=1+1
        elif((board[2]==board[5]==icon)and board[8]==" "):
            n1=8+1
        elif((board[2]==board[8]==icon)and board[5]==" "):
            n1=5+1
        elif((board[5]==board[8]==icon)and board[2]==" "):
            n1=2+1
        elif((board[0]==board[4]==icon)and board[8]==" "):
            n1=8+1
        elif((board[0]==board[8]==icon)and board[4]==" "):
            n1=4+1
        elif((board[4]==board[8]==icon)and board[0]==" "):
            n1=0+1
        elif((board[2]==board[4]==icon)and board[6]==" "):
            n1=6+1
        elif((board[2]==board[6]==icon)and board[4]==" "):
            n1=4+1
        elif((board[4]==board[6]==icon)and board[2]==" "):
            n1=2+1
        elif(board[0]==board[1]and board[2]==" "):
            n1=2+1
        elif(board[0]==board[2]and board[1]==" "):
            n1=1+1
        elif(board[1]==board[2]and board[0]==" "):
            n1=0+1
        elif(board[6]==board[7]and board[8]==" "):
            n1=8+1
        elif(board[6]==board[8]and board[7]==" "):
            n1=7+1
        elif(board[7]==board[8]and board[6]==" "):
            n1=6+1
        elif(board[1]==board[4]and board[7]==" "):
            n1=7+1
        elif(board[1]==board[7]and board[4]==" "):
            n1=4+1
        elif(board[4]==board[7]and board[1]==" "):
            n1=1+1
        elif(board[0]==board[4]and board[8]==" "):
            n1=8+1
        elif(board[0]==board[8]and board[4]==" "):
            n1=4+1
        elif(board[4]==board[8]and board[0]==" "):
            n1=0+1
        elif(board[2]==board[4]and board[6]==" "):
            n1=6+1
        elif(board[2]==board[6]and board[4]==" "):
            n1=4+1
        elif(board[4]==board[6]and board[2]==" "):
            n1=2+1
        else:
            n1=random.choice(n)
        time.sleep(1)
        print(n1)
        time.sleep(2)
        if(board[n1-1]==" "):
            board[n1-1]=icon
            n.remove(n1)
        else:
            print()
            print("No Space :(")
            player_movec(icon,mode)
    elif(mode==3):
        if(icon=="X"):
            sym="O"
        else:
            sym="X"
        print("Computer choice: ",end=' ')
        if((board[0]==board[1]==icon)and board[2]==" "):
            n1=2+1
        elif((board[0]==board[2]==icon)and board[1]==" "):
            n1=1+1
        elif((board[1]==board[2]==icon)and board[0]==" "):
            n1=0+1
        elif((board[3]==board[4]==icon)and board[5]==" "):
            n1=5+1
        elif((board[3]==board[5]==icon)and board[4]==" "):
            n1=4+1
        elif((board[4]==board[5]==icon)and board[3]==" "):
            n1=3+1
        elif((board[6]==board[7]==icon)and board[8]==" "):
            n1=8+1
        elif((board[6]==board[8]==icon)and board[7]==" "):
            n1=7+1
        elif((board[7]==board[8]==icon)and board[6]==" "):
            n1=6+1
        elif((board[0]==board[3]==icon)and board[6]==" "):
            n1=6+1
        elif((board[0]==board[6]==icon)and board[3]==" "):
            n1=3+1
        elif((board[3]==board[6]==icon)and board[0]==" "):
            n1=0+1
        elif((board[1]==board[4]==icon)and board[7]==" "):
            n1=7+1
        elif((board[1]==board[7]==icon)and board[4]==" "):
            n1=4+1
        elif((board[4]==board[7]==icon)and board[1]==" "):
            n1=1+1
        elif((board[2]==board[5]==icon)and board[8]==" "):
            n1=8+1
        elif((board[2]==board[8]==icon)and board[5]==" "):
            n1=5+1
        elif((board[5]==board[8]==icon)and board[2]==" "):
            n1=2+1
        elif((board[0]==board[4]==icon)and board[8]==" "):
            n1=8+1
        elif((board[0]==board[8]==icon)and board[4]==" "):
            n1=4+1
        elif((board[4]==board[8]==icon)and board[0]==" "):
            n1=0+1
        elif((board[2]==board[4]==icon)and board[6]==" "):
            n1=6+1
        elif((board[2]==board[6]==icon)and board[4]==" "):
            n1=4+1
        elif((board[4]==board[6]==icon)and board[2]==" "):
            n1=2+1
        elif(((board[3]==board[6]==sym)or(board[1]==board[2]==sym)or(board[4]==board[8]==sym))and(board[0]==" ")):
            n1=0+1
        elif(((board[0]==board[2]==sym)or(board[4]==board[7]==sym))and(board[1]==" ")):
            n1=1+1
        elif(((board[0]==board[1]==sym)or(board[5]==board[8]==sym)or(board[4]==board[6]==sym))and(board[2]==" ")):
            n1=2+1
        elif(((board[0]==board[6]==sym)or(board[4]==board[5]==sym))and(board[3]==" ")):
            n1=3+1
        elif(((board[0]==board[8]==sym)or(board[2]==board[6]==sym)or(board[1]==board[7]==sym)or(board[3]==board[5]==sym))and(board[4]==" ")):
            n1=4+1
        elif(((board[2]==board[8]==sym)or(board[3]==board[4]==sym))and(board[5]==" ")):
            n1=5+1
        elif(((board[0]==board[3]==sym)or(board[2]==board[4]==sym)or(board[7]==board[8]==sym))and(board[6]==" ")):
            n1=6+1
        elif(((board[6]==board[8]==sym)or(board[1]==board[4]==sym))and(board[7]==" ")):
            n1=7+1
        elif(((board[0]==board[4]==sym)or(board[2]==board[5]==sym)or(board[6]==board[7]==sym))and(board[8]==" ")):
            n1=8+1
        elif((board[4]==sym)and(board[0]==" ")):
             n1=0+1
        elif((board[4]==sym)and(board[2]==" ")):
             n1=2+1
        elif((board[4]==sym)and(board[6]==" ")):
             n1=6+1
        elif((board[4]==sym)and(board[8]==" ")):
             n1=8+1
        elif(((board[0]==sym)or(board[2]==sym)or(board[6]==sym)or(board[8]==sym))and board[4]==" "):
            n1=4+1
        elif((board[0]==board[8]==sym)and board[1]==" "):
            n1=1+1
        elif((board[2]==board[6]==sym)and board[1]==" "):
            n1=1+1
        elif(((board[1]==sym)or(board[3]==sym)or(board[5]==sym)or(board[7]==sym))and(board[4]==" ")):
            n1=4+1
        else:
            n1=random.choice(n)
        time.sleep(1)
        print(n1)
        time.sleep(2)
        if(board[n1-1]==" "):
            board[n1-1]=icon
            n.remove(n1)
        else:
            print()
            print("No Space :(")
            player_movec(icon,mode)
    else:
        print("Enter correct mode:")
def is_victory(icon):
    if(board[0]==board[1]==board[2]==icon)or\
        (board[3]==board[4]==board[5]==icon)or\
        (board[6]==board[7]==board[8]==icon)or\
        (board[0]==board[3]==board[6]==icon)or\
        (board[1]==board[4]==board[7]==icon)or\
        (board[2]==board[5]==board[8]==icon)or\
        (board[0]==board[4]==board[8]==icon)or\
        (board[2]==board[4]==board[6]==icon):
        return True
    else:
        return False
def is_draw():
    if " " not in board:
        return True
    else:
        return False
while True:
    print("Welcome to the Tic-Tac-Toe Game")
    ch1=int(input("Enter the choice: \n 1.Player Vs Computer \n 2.Player Vs Player \n Choice:"))
    if(ch1==1):
        m=int(input("Enter the Mode: \n 1.Easy \n 2.Medium \n 3.Hard \n Mode:"))
        while True:
            print_board()
            player_move("X")
            if is_victory("X"):
                print_board()
                print("Congratulations....Player Won")
                sys.exit()
            elif is_draw():
                print_board()
                print("Well Tried...The match is draw")
                sys.exit()
            print_board()
            player_movec("O",m)
            if is_victory("O"):
                print_board()
                print("Congratulations....Computer Won")
                sys.exit()
            elif is_draw():
                print_board()
                print("Well Tried...The match is draw")
                sys.exit()
    elif(ch1==2):
        while True:
            print_board()
            player_move("X")
            if is_victory("X"):
                print_board()
                print("Congratulations...Player1 Won")
                sys.exit()
            elif is_draw():
                print_board()
                print("Well Tried...The match is draw")
                sys.exit()
            print_board()
            player_move("O")
            if is_victory("O"):
                print_board()
                print("Congratulations...Player2 Won")
                sys.exit()
            elif is_draw():
                print_board()
                print("Well Tried...The match is draw")
                sys.exit()
    else:
        print("Enter the correct choice:")
