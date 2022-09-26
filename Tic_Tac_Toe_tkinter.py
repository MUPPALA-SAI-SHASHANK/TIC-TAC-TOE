import sys
import random
import tkinter
from tkinter import *
from tkinter import messagebox
clicked = True
count=0
global k
x=0
s=0
n=[j for j in range(1,10)]
b=[[0,0,0],[0,0,0],[0,0,0]]
def mode():
    mode = Tk()
    mode.title('SELECT THE MODE:')
    mode.configure(bg="lawngreen")
    mode.geometry("275x75+500+300")
    l = Label(mode, text="SELECT MODE", anchor="center", bg="lawngreen", fg="maroon1")
    b1 = Radiobutton(mode, text="1.Player VS Computer", anchor="w", bg="lawngreen",fg="maroon1",
                     command=lambda: [mode.destroy(), game_mode(1)])
    b2 = Radiobutton(mode, text="2.Player VS Player", anchor="w", bg="lawngreen",fg="maroon1",
                     command=lambda: [mode.destroy(), game_mode(2)])
    l.pack()
    b1.pack()
    b2.pack()
    mode.mainloop()
def mode1():
    mode1 = Tk()
    mode1.title('SELECT THE LEVEL:')
    mode1.configure(bg="lawngreen")
    mode1.geometry("275x100+500+300")
    l = Label(mode1, text="SELECT MODE", anchor="center", bg="lawngreen", fg="maroon1")
    b1 = Radiobutton(mode1, text="1.EASY", anchor="w", fg="maroon1", bg="lawngreen",
                     command=lambda: [mode1.destroy(), computer_mode(1)])
    b2 = Radiobutton(mode1, text="2.MEDIUM", anchor="w", fg="maroon1", bg="lawngreen",
                     command=lambda: [mode1.destroy(), computer_mode(2)])
    b3 = Radiobutton(mode1, text="3.HARD", anchor="w", fg="maroon1", bg="lawngreen",
                     command=lambda: [mode1.destroy(), computer_mode(3)])
    l.pack()
    b1.pack()
    b2.pack()
    b3.pack()
def exit():
    sys.exit()
def checkwon():
    global winner
    winner=False
    if (b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X"):
        b1.config(bg="green")
        b2.config(bg="green")
        b3.config(bg="green")
        winner=True
        messagebox.showinfo("TIC-TAC-TOE","Player with X wins!!!")
        replay()
    elif (b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X"):
        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")
        winner=True
        messagebox.showinfo("TIC-TAC-TOE","Player with X wins!!!")
        replay()
    elif (b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X"):
        b7.config(bg="green")
        b8.config(bg="green")
        b9.config(bg="green")
        winner=True
        messagebox.showinfo("TIC-TAC-TOE","Player with X wins!!!")
        replay()
    elif (b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X"):
        b1.config(bg="green")
        b4.config(bg="green")
        b7.config(bg="green")
        winner=True
        messagebox.showinfo("TIC-TAC-TOE","Player with X wins!!!")
        replay()
    elif (b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X"):
        b2.config(bg="green")
        b5.config(bg="green")
        b8.config(bg="green")
        winner=True
        messagebox.showinfo("TIC-TAC-TOE","Player with X wins!!!")
        replay()
    elif (b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X"):
        b3.config(bg="green")
        b6.config(bg="green")
        b9.config(bg="green")
        winner=True
        messagebox.showinfo("TIC-TAC-TOE","Player with X wins!!!")
        replay()
    elif (b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X"):
        b1.config(bg="green")
        b5.config(bg="green")
        b9.config(bg="green")
        winner=True
        messagebox.showinfo("TIC-TAC-TOE","Player with X wins!!!")
        replay()
    elif (b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X"):
        b3.config(bg="green")
        b5.config(bg="green")
        b7.config(bg="green")
        winner=True
        messagebox.showinfo("TIC-TAC-TOE","Player with X wins!!!")
        replay()
    elif (b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O"):
        b1.config(bg="green")
        b2.config(bg="green")
        b3.config(bg="green")
        winner=True
        messagebox.showinfo("TIC-TAC-TOE","Player with O wins!!!")
        replay()
    elif (b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O"):
        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")
        winner=True
        messagebox.showinfo("TIC-TAC-TOE","Player with O wins!!!")
        replay()
    elif (b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O"):
        b7.config(bg="green")
        b8.config(bg="green")
        b9.config(bg="green")
        winner=True
        messagebox.showinfo("TIC-TAC-TOE","Player with O wins!!!")
        replay()
    elif (b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O"):
        b1.config(bg="green")
        b4.config(bg="green")
        b7.config(bg="green")
        winner=True
        messagebox.showinfo("TIC-TAC-TOE","Player with O wins!!!")
        replay()
    elif (b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O"):
        b2.config(bg="green")
        b5.config(bg="green")
        b8.config(bg="green")
        winner=True
        messagebox.showinfo("TIC-TAC-TOE","Player with O wins!!!")
        replay()
    elif (b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O"):
        b3.config(bg="green")
        b6.config(bg="green")
        b9.config(bg="green")
        winner=True
        messagebox.showinfo("TIC-TAC-TOE","Player with O wins!!!")
        replay()
    elif (b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O"):
        b1.config(bg="green")
        b5.config(bg="green")
        b9.config(bg="green")
        winner=True
        messagebox.showinfo("TIC-TAC-TOE","Player with O wins!!!")
        replay()
    elif (b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O"):
        b3.config(bg="green")
        b5.config(bg="green")
        b7.config(bg="green")
        winner=True
        messagebox.showinfo("TIC-TAC-TOE","Player with O wins!!!")
        replay()
    if(count==9) and winner==False:
        messagebox.showinfo("TIC-TAC-TOE","Great Play Its a TIE...")
        replay()
def b_click(b):
    global clicked,count
    if b["text"]==" " and clicked==True:
        b["text"]="X"
        clicked=False
        count+=1
        checkwon()
    elif b["text"]==" " and clicked==False:
        b["text"]="O"
        clicked=True
        count+=1
        checkwon()
    else:
        messagebox.showerror("TIC-TAC-TOE","Already Box was Taken Please select a Valid box...")
def game_mode(k):
    if (k == 1):
        mode1()
    if (k == 2):
        reset()
def computer_mode(k):
    if(k==1):
        mode_easy(k)
    elif(k==2):
        mode_medium(k)
    elif(k==3):
        mode_hard(k)
def replay():
    global root
    root.destroy()
    Replay = Tk()
    Replay.title('Do you want to play?')
    Replay.configure(bg="lawngreen")
    Replay.geometry("300x75+500+300")
    l = Label(Replay, text="Select from the following : ", anchor="center", bg="lawngreen", fg="maroon1")
    b1 = Radiobutton(Replay, text="Replay", anchor="w", fg="maroon1", bg="lawngreen",
                     command=lambda: [Replay.destroy(), replay1(1)])
    b2 = Radiobutton(Replay, text="Quit", anchor="w", fg="maroon1", bg="lawngreen",
                     command=lambda: [Replay.destroy(), replay1(2)])
    l.pack()
    b1.pack()
    b2.pack()
    Replay.mainloop()
def replay1(k):
    if(k==1):
        reset()
    else:
        exit()
def winner(k):
    global b
    if(btn0_0['text']=='X' and btn0_1['text']=='X' and btn0_2['text']=='X'):
        btn0_0.config(bg="green")
        btn0_1.config(bg="green")
        btn0_2.config(bg="green")
        winner_message('X',k)
        return 1
    elif(btn1_0['text']=='X' and btn1_1['text']=='X' and btn1_2['text']=='X'):
        btn1_0.config(bg="green")
        btn1_1.config(bg="green")
        btn1_2.config(bg="green")
        winner_message('X',k)
        return 1
    elif (btn2_0['text'] == 'X' and btn2_1['text'] == 'X' and btn2_2['text'] == 'X'):
        btn2_0.config(bg="green")
        btn2_1.config(bg="green")
        btn2_2.config(bg="green")
        winner_message('X',k)
        return 1
    elif (btn0_0['text'] == 'X' and btn1_0['text'] == 'X' and btn2_0['text'] == 'X'):
        btn0_0.config(bg="green")
        btn1_0.config(bg="green")
        btn2_0.config(bg="green")
        winner_message('X',k)
        return 1
    elif (btn0_1['text'] == 'X' and btn1_1['text'] == 'X' and btn2_1['text'] == 'X'):
        btn0_1.config(bg="green")
        btn1_1.config(bg="green")
        btn2_1.config(bg="green")
        winner_message('X',k)
        return 1
    elif (btn0_2['text'] == 'X' and btn1_2['text'] == 'X' and btn2_2['text'] == 'X'):
        btn0_2.config(bg="green")
        btn1_2.config(bg="green")
        btn2_2.config(bg="green")
        winner_message('X',k)
        return 1
    elif (btn0_0['text'] == 'X' and btn1_1['text'] == 'X' and btn2_2['text'] == 'X'):
        btn0_0.config(bg="green")
        btn1_1.config(bg="green")
        btn2_2.config(bg="green")
        winner_message('X',k)
        return 1
    elif (btn0_2['text'] == 'X' and btn1_1['text'] == 'X' and btn2_0['text'] == 'X'):
        btn0_2.config(bg="green")
        btn1_1.config(bg="green")
        btn2_0.config(bg="green")
        winner_message('X',k)
        return 1
    elif (btn0_0['text'] == 'O' and btn0_1['text'] == 'O' and btn0_2['text'] == 'O'):
        btn0_0.config(bg="red")
        btn0_1.config(bg="red")
        btn0_2.config(bg="red")
        winner_message('O',k)
        return 1
    elif (btn1_0['text'] == 'O' and btn1_1['text'] == 'O' and btn1_2['text'] == 'O'):
        btn1_0.config(bg="red")
        btn1_1.config(bg="red")
        btn1_2.config(bg="red")
        winner_message('O',k)
        return 1
    elif (btn2_0['text'] == 'O' and btn2_1['text'] == 'O' and btn2_2['text'] == 'O'):
        btn2_0.config(bg="red")
        btn2_1.config(bg="red")
        btn2_2.config(bg="red")
        winner_message('O',k)
        return 1
    elif (btn0_0['text'] == 'O' and btn1_0['text'] == 'O' and btn2_0['text'] == 'O'):
        btn0_0.config(bg="red")
        btn1_0.config(bg="red")
        btn2_0.config(bg="red")
        winner_message('O',k)
        return 1
    elif (btn0_1['text'] == 'O' and btn1_1['text'] == 'O' and btn2_1['text'] == 'O'):
        btn0_1.config(bg="red")
        btn1_1.config(bg="red")
        btn2_1.config(bg="red")
        winner_message('O',k)
        return 1
    elif (btn0_2['text'] == 'O' and btn1_2['text'] == 'O' and btn2_2['text'] == 'O'):
        btn0_2.config(bg="red")
        btn1_2.config(bg="red")
        btn2_2.config(bg="red")
        winner_message('O',k)
        return 1
    elif (btn2_0['text'] == 'O' and btn1_1['text'] == 'O' and btn0_2['text'] == 'O'):
        btn2_0.config(bg="red")
        btn1_1.config(bg="red")
        btn0_2.config(bg="red")
        winner_message('O',k)
        return 1
    elif (btn0_0['text'] == 'O' and btn1_1['text'] == 'O' and btn2_2['text'] == 'O'):
        btn0_0.config(bg="red")
        btn1_1.config(bg="red")
        btn2_2.config(bg="red")
        winner_message('O',k)
        return 1
    else:
        return 0
def winner_message(h,k):
    global gui
    if(h=='X'):
        messagebox.showinfo('Winner','Player Won...')
        gui.destroy()
        replay_com(k)
    else:
        messagebox.showinfo('Winner','Computer Won...')
        gui.destroy()
        replay_com(k)
def replay_com(k):
    global replay_comp
    replay_comp = Tk()
    replay_comp.title('Do you want to play?')
    replay_comp.configure(bg="lawngreen")
    replay_comp.geometry("300x75+500+300")
    l = Label(replay_comp, text="Select from the following : ", anchor="center", bg="lawngreen", fg="maroon1")
    b1 = Radiobutton(replay_comp, text="Replay", anchor="w", fg="maroon1", bg="lawngreen",
                     command=lambda: [replay_comp.destroy(), replay1_com(k)])
    b2 = Radiobutton(replay_comp, text="Quit", anchor="w", fg="maroon1", bg="lawngreen",
                     command=lambda: [replay_comp.destroy(), exit()])
    l.pack()
    b1.pack()
    b2.pack()
    replay_comp.mainloop()
def replay1_com(k):
    global b,x
    if(k==1):
        x=0
        b[0][0]=b[0][1]=b[0][2]=b[1][0]=b[1][1]=b[1][2]=b[2][0]=b[2][1]=b[2][2]=0
        mode_easy(k)
    elif(k==2):
        x=0
        b[0][0] = b[0][1] = b[0][2] = b[1][0] = b[1][1] = b[1][2] = b[2][0] = b[2][1] = b[2][2] = 0
        mode_medium(k)
    else:
        x=0
        b[0][0] = b[0][1] = b[0][2] = b[1][0] = b[1][1] = b[1][2] = b[2][0] = b[2][1] = b[2][2] = 0
        mode_hard(k)
def change(bt,l,m,k):
    global x
    count1=0
    if(b[l][m]==0):
        if(x%2==0):
            bt['text']='X'
            x=x+1
            b[l][m]=1
            count1=check(k)
        if(count1!=1):
            computer_play(1)
            b[l][m] = 1
            x=x+1
            count1=check(k)
    else:
        messagebox.showinfo("Error Message","Already Taken...Please Select another box...")
def change1(bt,l,m,k):
    global x
    count1=0
    if(b[l][m]==0):
        if(x%2==0):
            bt['text']='X'
            x=x+1
            b[l][m]=1
            count1=check(1)
        if(count1!=1):
            computer_play(2)
            x=x+1
            count1=check(1)
    else:
        messagebox.showinfo("Error Message","Already Taken...Please Select another box...")
def change2(bt,l,m,k):
    global x
    count1=0
    if(b[l][m]==0):
        if(x%2==0):
            bt['text']='X'
            x=x+1
            b[l][m]=1
            count1=check(k)
        if(count1!=1):
            computer_play(3)
            x=x+1
            count1=check(k)
    else:
        messagebox.showinfo("Error Message","Already Taken...Please Select another box...")
def check(k):
    count1=0
    global x,gui
    if(x>=5):
        count1=winner(k)
        if(count1!=1):
            if(x==9):
                messagebox.showinfo("TIED","Well Played! Match Tried...")
                gui.destroy()
                replay_com(k)
    else:
        return count1
def randomk():
    global x
    if(x<9):
        t = [0, 1, 2]
        n = random.choice(t)
        s = random.choice(t)
        if (b[n][s] == 0):
            if(n==0 and s==0):
                btn0_0['text']='O'
            elif(n==0 and s==1):
                btn0_1['text']='O'
            elif (n == 0 and s == 2):
                btn0_2['text'] = 'O'
            elif (n == 1 and s == 0):
                btn1_0['text'] = 'O'
            elif (n == 1 and s == 1):
                btn1_1['text'] = 'O'
            elif (n == 1 and s == 2):
                btn1_2['text'] = 'O'
            elif (n == 2 and s == 0):
                btn2_0['text'] = 'O'
            elif (n == 2 and s == 1):
                btn2_1['text'] = 'O'
            elif (n == 2 and s == 2):
                btn2_2['text'] = 'O'
            b[n][s] = 1
            return
        else:
            randomk()
    else:
        pass
def medium(k):
    global b
    if (btn0_0['text'] == btn0_1['text'] == 'O' and btn0_2['text'] == ' '):
        btn0_2['text'] = 'O'
        b[0][2] = 1
    elif (btn0_0['text'] == btn0_2['text'] == 'O' and btn0_1['text'] == ' '):
        btn0_1['text'] = 'O'
        b[0][1] = 1
    elif (btn0_1['text'] == btn0_2['text'] == 'O' and btn0_0['text'] == ' '):
        btn0_0['text'] = 'O'
        b[0][0] = 1
    elif (btn1_0['text'] == btn1_1['text'] == 'O' and btn1_2['text'] == ' '):
        btn1_2['text'] = 'O'
        b[1][2] = 1
    elif (btn1_0['text'] == btn1_2['text'] == 'O' and btn1_1['text'] == ' '):
        btn1_1['text'] = 'O'
        b[1][1] = 1
    elif (btn1_1['text'] == btn1_2['text'] == 'O' and btn1_0['text'] == ' '):
        btn1_0['text'] = 'O'
        b[1][0] = 1
    elif (btn2_0['text'] == btn2_1['text'] == 'O' and btn2_2['text'] == ' '):
        btn2_2['text'] = 'O'
        b[2][2] = 1
    elif (btn2_0['text'] == btn2_2['text'] == 'O' and btn2_1['text'] == ' '):
        btn2_1['text'] = 'O'
        b[2][1] = 1
    elif (btn2_1['text'] == btn2_2['text'] == 'O' and btn2_0['text'] == ' '):
        btn2_0['text'] = 'O'
        b[2][0] = 1
    elif (btn0_0['text'] == btn1_0['text'] == 'O' and btn2_0['text'] == ' '):
        btn2_0['text'] = 'O'
        b[2][0] = 1
    elif (btn0_0['text'] == btn2_0['text'] == 'O' and btn1_0['text'] == ' '):
        btn1_0['text'] = 'O'
        b[1][0] = 1
    elif (btn1_0['text'] == btn2_0['text'] == 'O' and btn0_0['text'] == ' '):
        btn0_0['text'] = 'O'
        b[0][0] = 1
    elif (btn0_1['text'] == btn1_1['text'] == 'O' and btn2_1['text'] == ' '):
        btn2_1['text'] = 'O'
        b[2][1] = 1
    elif (btn0_1['text'] == btn2_1['text'] == 'O' and btn1_1['text'] == ' '):
        btn1_1['text'] = 'O'
        b[1][1] = 1
    elif (btn1_1['text'] == btn2_1['text'] == 'O' and btn0_1['text'] == ' '):
        btn0_1['text'] = 'O'
        b[0][1] = 1
    elif (btn0_2['text'] == btn1_2['text'] == 'O' and btn2_2['text'] == ' '):
        btn2_2['text'] = 'O'
        b[2][2] = 1
    elif (btn0_2['text'] == btn2_2['text'] == 'O' and btn1_2['text'] == ' '):
        btn1_2['text'] = 'O'
        b[1][2] = 1
    elif (btn1_2['text'] == btn2_2['text'] == 'O' and btn0_2['text'] == ' '):
        btn0_2['text'] = 'O'
        b[0][2] = 1
    elif (btn0_0['text'] == btn1_1['text'] == 'O' and btn2_2['text'] == ' '):
        btn2_2['text'] = 'O'
        b[2][2] = 1
    elif (btn0_0['text'] == btn2_2['text'] == 'O' and btn1_1['text'] == ' '):
        btn1_1['text'] = 'O'
        b[1][1] = 1
    elif (btn1_1['text'] == btn2_2['text'] == 'O' and btn0_0['text'] == ' '):
        btn0_0['text'] = 'O'
        b[0][0] = 1
    elif (btn0_2['text'] == btn1_1['text'] == 'O' and btn2_0['text'] == ' '):
        btn2_0['text'] = 'O'
        b[2][0] = 1
    elif (btn0_2['text'] == btn2_0['text'] == 'O' and btn1_1['text'] == ' '):
        btn1_1['text'] = 'O'
        b[1][1] = 1
    elif (btn1_1['text'] == btn2_0['text'] == 'O' and btn0_2['text'] == ' '):
        btn0_2['text'] = 'O'
        b[0][2] = 1
    elif(btn0_0['text']==btn0_1['text']=='X' and btn0_2['text']==' '):
        btn0_2['text']='O'
        b[0][2]=1
    elif(btn0_0['text']==btn0_2['text']=='X' and btn0_1['text']==' '):
        btn0_1['text']='O'
        b[0][1] = 1
    elif (btn0_1['text'] == btn0_2['text'] == 'X' and btn0_0['text'] == ' '):
        btn0_0['text'] = 'O'
        b[0][0] = 1
    elif (btn1_0['text'] == btn1_1['text'] == 'X' and btn1_2['text'] == ' '):
        btn1_2['text'] = 'O'
        b[1][2] = 1
    elif (btn1_0['text'] == btn1_2['text'] == 'X' and btn1_1['text'] == ' '):
        btn1_1['text'] = 'O'
        b[1][1] = 1
    elif (btn1_1['text'] == btn1_2['text'] == 'X' and btn1_0['text'] == ' '):
        btn1_0['text'] = 'O'
        b[1][0] = 1
    elif (btn2_0['text'] == btn2_1['text'] == 'X' and btn2_2['text'] == ' '):
        btn2_2['text'] = 'O'
        b[2][2] = 1
    elif (btn2_0['text'] == btn2_2['text'] == 'X' and btn2_1['text'] == ' '):
        btn2_1['text'] = 'O'
        b[2][1] = 1
    elif (btn2_1['text'] == btn2_2['text'] == 'X' and btn2_0['text'] == ' '):
        btn2_0['text'] = 'O'
        b[2][0] = 1
    elif (btn0_0['text'] == btn1_0['text'] == 'X' and btn2_0['text'] == ' '):
        btn2_0['text'] = 'O'
        b[2][0] = 1
    elif (btn0_0['text'] == btn2_0['text'] == 'X' and btn1_0['text'] == ' '):
        btn1_0['text'] = 'O'
        b[1][0] = 1
    elif (btn1_0['text'] == btn2_0['text'] == 'X' and btn0_0['text'] == ' '):
        btn0_0['text'] = 'O'
        b[0][0] = 1
    elif (btn0_1['text'] == btn1_1['text'] == 'X' and btn2_1['text'] == ' '):
        btn2_1['text'] = 'O'
        b[2][1] = 1
    elif (btn0_1['text'] == btn2_1['text'] == 'X' and btn1_1['text'] == ' '):
        btn1_1['text'] = 'O'
        b[1][1] = 1
    elif (btn1_1['text'] == btn2_1['text'] == 'X' and btn0_1['text'] == ' '):
        btn0_1['text'] = 'O'
        b[0][1] = 1
    elif (btn0_2['text'] == btn1_2['text'] == 'X' and btn2_2['text'] == ' '):
        btn2_2['text'] = 'O'
        b[2][2] = 1
    elif (btn0_2['text'] == btn2_2['text'] == 'X' and btn1_2['text'] == ' '):
        btn1_2['text'] = 'O'
        b[1][2] = 1
    elif (btn1_2['text'] == btn2_2['text'] == 'X' and btn0_2['text'] == ' '):
        btn0_2['text'] = 'O'
        b[0][2] = 1
    else:
        randomk()
def hard(k):
    global b
    if (btn0_0['text'] == btn0_1['text'] == 'O' and btn0_2['text'] == ' '):
        btn0_2['text'] = 'O'
        b[0][2] = 1
    elif (btn0_0['text'] == btn0_2['text'] == 'O' and btn0_1['text'] == ' '):
        btn0_1['text'] = 'O'
        b[0][1] = 1
    elif (btn0_1['text'] == btn0_2['text'] == 'O' and btn0_0['text'] == ' '):
        btn0_0['text'] = 'O'
        b[0][0] = 1
    elif (btn1_0['text'] == btn1_1['text'] == 'O' and btn1_2['text'] == ' '):
        btn1_2['text'] = 'O'
        b[1][2] = 1
    elif (btn1_0['text'] == btn1_2['text'] == 'O' and btn1_1['text'] == ' '):
        btn1_1['text'] = 'O'
        b[1][1] = 1
    elif (btn1_1['text'] == btn1_2['text'] == 'O' and btn1_0['text'] == ' '):
        btn1_0['text'] = 'O'
        b[1][0] = 1
    elif (btn2_0['text'] == btn2_1['text'] == 'O' and btn2_2['text'] == ' '):
        btn2_2['text'] = 'O'
        b[2][2] = 1
    elif (btn2_0['text'] == btn2_2['text'] == 'O' and btn2_1['text'] == ' '):
        btn2_1['text'] = 'O'
        b[2][1] = 1
    elif (btn2_1['text'] == btn2_2['text'] == 'O' and btn2_0['text'] == ' '):
        btn2_0['text'] = 'O'
        b[2][0] = 1
    elif (btn0_0['text'] == btn1_0['text'] == 'O' and btn2_0['text'] == ' '):
        btn2_0['text'] = 'O'
        b[2][0] = 1
    elif (btn0_0['text'] == btn2_0['text'] == 'O' and btn1_0['text'] == ' '):
        btn1_0['text'] = 'O'
        b[1][0] = 1
    elif (btn1_0['text'] == btn2_0['text'] == 'O' and btn0_0['text'] == ' '):
        btn0_0['text'] = 'O'
        b[0][0] = 1
    elif (btn0_1['text'] == btn1_1['text'] == 'O' and btn2_1['text'] == ' '):
        btn2_1['text'] = 'O'
        b[2][1] = 1
    elif (btn0_1['text'] == btn2_1['text'] == 'O' and btn1_1['text'] == ' '):
        btn1_1['text'] = 'O'
        b[1][1] = 1
    elif (btn1_1['text'] == btn2_1['text'] == 'O' and btn0_1['text'] == ' '):
        btn0_1['text'] = 'O'
        b[0][1] = 1
    elif (btn0_2['text'] == btn1_2['text'] == 'O' and btn2_2['text'] == ' '):
        btn2_2['text'] = 'O'
        b[2][2] = 1
    elif (btn0_2['text'] == btn2_2['text'] == 'O' and btn1_2['text'] == ' '):
        btn1_2['text'] = 'O'
        b[1][2] = 1
    elif (btn1_2['text'] == btn2_2['text'] == 'O' and btn0_2['text'] == ' '):
        btn0_2['text'] = 'O'
        b[0][2] = 1
    elif (btn0_0['text'] == btn1_1['text'] == 'O' and btn2_2['text'] == ' '):
        btn2_2['text'] = 'O'
        b[2][2] = 1
    elif (btn0_0['text'] == btn2_2['text'] == 'O' and btn1_1['text'] == ' '):
        btn1_1['text'] = 'O'
        b[1][1] = 1
    elif (btn1_1['text'] == btn2_2['text'] == 'O' and btn0_0['text'] == ' '):
        btn0_0['text'] = 'O'
        b[0][0] = 1
    elif (btn0_2['text'] == btn1_1['text'] == 'O' and btn2_0['text'] == ' '):
        btn2_0['text'] = 'O'
        b[2][0] = 1
    elif (btn0_2['text'] == btn2_0['text'] == 'O' and btn1_1['text'] == ' '):
        btn1_1['text'] = 'O'
        b[1][1] = 1
    elif (btn1_1['text'] == btn2_0['text'] == 'O' and btn0_2['text'] == ' '):
        btn0_2['text'] = 'O'
        b[0][2] = 1
    elif (btn0_0['text'] == btn0_1['text'] == 'X' and btn0_2['text'] == ' '):
        btn0_2['text'] = 'O'
        b[0][2] = 1
    elif (btn0_0['text'] == btn0_2['text'] == 'X' and btn0_1['text'] == ' '):
        btn0_1['text'] = 'O'
        b[0][1] = 1
    elif (btn0_1['text'] == btn0_2['text'] == 'X' and btn0_0['text'] == ' '):
        btn0_0['text'] = 'O'
        b[0][0] = 1
    elif (btn1_0['text'] == btn1_1['text'] == 'X' and btn1_2['text'] == ' '):
        btn1_2['text'] = 'O'
        b[1][2] = 1
    elif (btn1_0['text'] == btn1_2['text'] == 'X' and btn1_1['text'] == ' '):
        btn1_1['text'] = 'O'
        b[1][1] = 1
    elif (btn1_1['text'] == btn1_2['text'] == 'X' and btn1_0['text'] == ' '):
        btn1_0['text'] = 'O'
        b[1][0] = 1
    elif (btn2_0['text'] == btn2_1['text'] == 'X' and btn2_2['text'] == ' '):
        btn2_2['text'] = 'O'
        b[2][2] = 1
    elif (btn2_0['text'] == btn2_2['text'] == 'X' and btn2_1['text'] == ' '):
        btn2_1['text'] = 'O'
        b[2][1] = 1
    elif (btn2_1['text'] == btn2_2['text'] == 'X' and btn2_0['text'] == ' '):
        btn2_0['text'] = 'O'
        b[2][0] = 1
    elif (btn0_0['text'] == btn1_0['text'] == 'X' and btn2_0['text'] == ' '):
        btn2_0['text'] = 'O'
        b[2][0] = 1
    elif (btn0_0['text'] == btn2_0['text'] == 'X' and btn1_0['text'] == ' '):
        btn1_0['text'] = 'O'
        b[1][0] = 1
    elif (btn1_0['text'] == btn2_0['text'] == 'X' and btn0_0['text'] == ' '):
        btn0_0['text'] = 'O'
        b[0][0] = 1
    elif (btn0_1['text'] == btn1_1['text'] == 'X' and btn2_1['text'] == ' '):
        btn2_1['text'] = 'O'
        b[2][1] = 1
    elif (btn0_1['text'] == btn2_1['text'] == 'X' and btn1_1['text'] == ' '):
        btn1_1['text'] = 'O'
        b[1][1] = 1
    elif (btn1_1['text'] == btn2_1['text'] == 'X' and btn0_1['text'] == ' '):
        btn0_1['text'] = 'O'
        b[0][1] = 1
    elif (btn0_2['text'] == btn1_2['text'] == 'X' and btn2_2['text'] == ' '):
        btn2_2['text'] = 'O'
        b[2][2] = 1
    elif (btn0_2['text'] == btn2_2['text'] == 'X' and btn1_2['text'] == ' '):
        btn1_2['text'] = 'O'
        b[1][2] = 1
    elif (btn1_2['text'] == btn2_2['text'] == 'X' and btn0_2['text'] == ' '):
        btn0_2['text'] = 'O'
        b[0][2] = 1
    elif (btn0_1['text'] == btn1_1['text'] == 'X' and btn2_1['text'] == ' '):
        btn2_1['text'] = 'O'
        b[2][1] = 1
    elif (btn0_1['text'] == btn2_1['text'] == 'X' and btn1_1['text'] == ' '):
        btn1_1['text'] = 'O'
        b[1][1] = 1
    elif (btn1_1['text'] == btn2_1['text'] == 'X' and btn0_1['text'] == ' '):
        btn0_1['text'] = 'O'
        b[0][1] = 1
    elif (btn0_2['text'] == btn1_2['text'] == 'X' and btn2_2['text'] == ' '):
        btn2_2['text'] = 'O'
        b[2][2] = 1
    elif (btn0_2['text'] == btn2_2['text'] == 'X' and btn1_2['text'] == ' '):
        btn1_2['text'] = 'O'
        b[1][2] = 1
    elif (btn1_2['text'] == btn2_2['text'] == 'X' and btn0_2['text'] == ' '):
        btn0_2['text'] = 'O'
        b[0][2] = 1
    elif(btn1_1['text']=='X' and btn0_0['text']==' '):
        btn0_0['text']='O'
        b[0][0]=1
    elif (btn1_1['text'] == 'X' and btn0_2['text']==' '):
        btn0_2['text'] = 'O'
        b[0][2] = 1
    elif (btn1_1['text'] == 'X' and btn2_0['text']==' '):
        btn2_0['text'] = 'O'
        b[2][0] = 1
    elif (btn1_1['text'] == 'X' and btn2_2['text']==' '):
        btn2_2['text'] = 'O'
        b[2][2] = 1
    elif((btn0_0['text']=='X' or btn0_2['text']=='X' or btn2_0['text']=='X' or btn2_2['text']=='X')and(btn1_1['text']==' ')):
        btn1_1['text']='O'
        b[1][1]=1
    elif(btn0_0['text']=='X' and btn2_2['text']=='X' and btn0_1['text']==' '):
        btn0_1['text']='O'
        b[0][1]=1
    elif (btn0_2['text'] == 'X' and btn2_0['text'] == 'X' and btn0_1['text'] == ' '):
        btn0_1['text'] = 'O'
        b[0][1] = 1
    elif ((btn0_1['text'] == 'X' or btn1_0['text'] == 'X' or btn1_2['text'] == 'X' or btn2_1['text'] == 'X') and (btn1_1['text'] == ' ')):
        btn1_1['text'] = 'O'
        b[1][1] = 1
    else:
        randomk()
def computer_play(k):
    global b
    if(k==1):
        randomk()
    elif(k==2):
        medium(k)
    else:
        hard(k)
def mode_easy(k):
    global gui, b, btn0_0, btn0_1, btn0_2, btn1_0, btn1_1, btn1_2, btn2_0, btn2_1, btn2_2, mode
    gui = Tk()
    gui.title('Player Vs Computer')
    gui.geometry("+420+50")
    btn0_0 = Button(gui, text=" ", font=("Times", 32), height=3, width=6, bg="SystemButtonFace",
                    command=lambda: change(btn0_0, 0, 0,1))
    btn0_1 = Button(gui, text=" ", font=("Times", 32), height=3, width=6, bg="SystemButtonFace",
                    command=lambda: change(btn0_1, 0, 1,1))
    btn0_2 = Button(gui, text=" ", font=("Times", 32), height=3, width=6, bg="SystemButtonFace",
                    command=lambda: change(btn0_2, 0, 2,1))
    btn1_0 = Button(gui, text=" ", font=("Times", 32), height=3, width=6, bg="SystemButtonFace",
                    command=lambda: change(btn1_0, 1, 0,1))
    btn1_1 = Button(gui, text=" ", font=("Times", 32), height=3, width=6, bg="SystemButtonFace",
                    command=lambda: change(btn1_1, 1, 1,1))
    btn1_2 = Button(gui, text=" ", font=("Times", 32), height=3, width=6, bg="SystemButtonFace",
                    command=lambda: change(btn1_2, 1, 2,1))
    btn2_0 = Button(gui, text=" ", font=("Times", 32), height=3, width=6, bg="SystemButtonFace",
                    command=lambda: change(btn2_0, 2, 0,1))
    btn2_1 = Button(gui, text=" ", font=("Times", 32), height=3, width=6, bg="SystemButtonFace",
                    command=lambda: change(btn2_1, 2, 1,1))
    btn2_2 = Button(gui, text=" ", font=("Times", 32), height=3, width=6, bg="SystemButtonFace",
                    command=lambda: change(btn2_2, 2, 2,1))
    btn0_0.grid(row=0, column=0)
    btn0_1.grid(row=0, column=1)
    btn0_2.grid(row=0, column=2)
    btn1_0.grid(row=1, column=0)
    btn1_1.grid(row=1, column=1)
    btn1_2.grid(row=1, column=2)
    btn2_0.grid(row=2, column=0)
    btn2_1.grid(row=2, column=1)
    btn2_2.grid(row=2, column=2)
    b[0][0] = b[0][1] = b[0][2] = b[1][0] = b[1][1] = b[1][2] = b[2][0] = b[2][1] = b[2][2] = 0
    menu1 = Menu(gui)
    gui.config(menu=menu1)
    menu1.add_command(label="Reset", command=lambda: [gui.destroy(), mode_easy(k)])
    menu1.add_command(label="Quit", command=lambda: [gui.destroy(), exit()])
    gui.mainloop()
def mode_medium(k):
    global gui, b, btn0_0, btn0_1, btn0_2, btn1_0, btn1_1, btn1_2, btn2_0, btn2_1, btn2_2, mode
    gui = Tk()
    gui.title('Player Vs Computer')
    gui.geometry("+420+50")
    btn0_0 = Button(gui, text=" ", font=("Times", 32), height=3, width=6, bg="SystemButtonFace",
                    command=lambda: change1(btn0_0, 0, 0,2))
    btn0_1 = Button(gui, text=" ", font=("Times", 32), height=3, width=6, bg="SystemButtonFace",
                    command=lambda: change1(btn0_1, 0, 1,2))
    btn0_2 = Button(gui, text=" ", font=("Times", 32), height=3, width=6, bg="SystemButtonFace",
                    command=lambda: change1(btn0_2, 0, 2,2))
    btn1_0 = Button(gui, text=" ", font=("Times", 32), height=3, width=6, bg="SystemButtonFace",
                    command=lambda: change1(btn1_0, 1, 0,2))
    btn1_1 = Button(gui, text=" ", font=("Times", 32), height=3, width=6, bg="SystemButtonFace",
                    command=lambda: change1(btn1_1, 1, 1,2))
    btn1_2 = Button(gui, text=" ", font=("Times", 32), height=3, width=6, bg="SystemButtonFace",
                    command=lambda: change1(btn1_2, 1, 2,2))
    btn2_0 = Button(gui, text=" ", font=("Times", 32), height=3, width=6, bg="SystemButtonFace",
                    command=lambda: change1(btn2_0, 2, 0,2))
    btn2_1 = Button(gui, text=" ", font=("Times", 32), height=3, width=6, bg="SystemButtonFace",
                    command=lambda: change1(btn2_1, 2, 1,2))
    btn2_2 = Button(gui, text=" ", font=("Times", 32), height=3, width=6, bg="SystemButtonFace",
                    command=lambda: change1(btn2_2, 2, 2,2))
    btn0_0.grid(row=0, column=0)
    btn0_1.grid(row=0, column=1)
    btn0_2.grid(row=0, column=2)
    btn1_0.grid(row=1, column=0)
    btn1_1.grid(row=1, column=1)
    btn1_2.grid(row=1, column=2)
    btn2_0.grid(row=2, column=0)
    btn2_1.grid(row=2, column=1)
    btn2_2.grid(row=2, column=2)
    b[0][0] = b[0][1] = b[0][2] = b[1][0] = b[1][1] = b[1][2] = b[2][0] = b[2][1] = b[2][2] = 0
    menu1 = Menu(gui)
    gui.config(menu=menu1)
    menu1.add_command(label="Reset", command=lambda: [gui.destroy(), mode_medium(k)])
    menu1.add_command(label="Quit", command=lambda: [gui.destroy(), exit()])
    gui.mainloop()
def mode_hard(k):
    global gui, b, btn0_0, btn0_1, btn0_2, btn1_0, btn1_1, btn1_2, btn2_0, btn2_1, btn2_2, mode
    gui = Tk()
    gui.title('Player Vs Computer')
    gui.geometry("+420+50")
    btn0_0 = Button(gui,text=" ",font=("Times",32),height=3,width=6,bg="SystemButtonFace",command=lambda:change2(btn0_0,0,0,3))
    btn0_1 = Button(gui,text=" ",font=("Times",32),height=3,width=6,bg="SystemButtonFace",command=lambda:change2(btn0_1,0,1,3))
    btn0_2 = Button(gui,text=" ",font=("Times",32),height=3,width=6,bg="SystemButtonFace",command=lambda:change2(btn0_2,0,2,3))
    btn1_0 = Button(gui,text=" ",font=("Times",32),height=3,width=6,bg="SystemButtonFace",command=lambda:change2(btn1_0,1,0,3))
    btn1_1 = Button(gui,text=" ",font=("Times",32),height=3,width=6,bg="SystemButtonFace",command=lambda:change2(btn1_1,1,1,3))
    btn1_2 = Button(gui,text=" ",font=("Times",32),height=3,width=6,bg="SystemButtonFace",command=lambda:change2(btn1_2,1,2,3))
    btn2_0 = Button(gui,text=" ",font=("Times",32),height=3,width=6,bg="SystemButtonFace",command=lambda:change2(btn2_0,2,0,3))
    btn2_1 = Button(gui,text=" ",font=("Times",32),height=3,width=6,bg="SystemButtonFace",command=lambda:change2(btn2_1,2,1,3))
    btn2_2 = Button(gui,text=" ",font=("Times",32),height=3,width=6,bg="SystemButtonFace",command=lambda:change2(btn2_2,2,2,3))
    btn0_0.grid(row=0, column=0)
    btn0_1.grid(row=0, column=1)
    btn0_2.grid(row=0, column=2)
    btn1_0.grid(row=1, column=0)
    btn1_1.grid(row=1, column=1)
    btn1_2.grid(row=1, column=2)
    btn2_0.grid(row=2, column=0)
    btn2_1.grid(row=2, column=1)
    btn2_2.grid(row=2, column=2)
    b[0][0] = b[0][1] = b[0][2] = b[1][0] = b[1][1] = b[1][2] = b[2][0] = b[2][1] = b[2][2] = 0
    menu1 = Menu(gui)
    gui.config(menu=menu1)
    menu1.add_command(label="Reset", command=lambda: [gui.destroy(), mode_hard(k)])
    menu1.add_command(label="Quit", command=lambda: [gui.destroy(), exit()])
    gui.mainloop()
def reset():
    global root,gui
    root = Tk()
    root.title('Player Vs Player')
    root.geometry("+420+50")
    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    global clicked,count,winner
    clicked = True
    count=0
    winner=False
    b1=Button(root,text=" ",font=("Times",32),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(b1))
    b2=Button(root,text=" ",font=("Times",32),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(b2))
    b3=Button(root,text=" ",font=("Times",32),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(b3))
    b4=Button(root,text=" ",font=("Times",32),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(b4))
    b5=Button(root,text=" ",font=("Times",32),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(b5))
    b6=Button(root,text=" ",font=("Times",32),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(b6))
    b7=Button(root,text=" ",font=("Times",32),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(b7))
    b8=Button(root,text=" ",font=("Times",32),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(b8))
    b9=Button(root,text=" ",font=("Times",32),height=3,width=6,bg="SystemButtonFace",command=lambda:b_click(b9))
    b1.grid(row=0,column=0)
    b2.grid(row=0,column=1)
    b3.grid(row=0,column=2)
    b4.grid(row=1,column=0)
    b5.grid(row=1,column=1)
    b6.grid(row=1,column=2)
    b7.grid(row=2,column=0)
    b8.grid(row=2,column=1)
    b9.grid(row=2,column=2)
    menu = Menu(root)
    root.config(menu=menu)
    menu.add_command(label="Reset",command=lambda:[root.destroy(),reset()])
    root.mainloop()
mode()
