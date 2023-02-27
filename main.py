MATCH_LIST = [['.','.','.'],['.','.','.'],['.','.','.']]
SCORE_1 = 0
SCORE_2 = 0
PLAYER1 = ''
PLAYER2 = ''
SWAP = 1
Button_list = []

import sys
from tkinter import *
import tkinter.messagebox as msg

def start(event=None):
	global PLAYER1, PLAYER2, e1, e2, root_, player1_var, player2_var
	PLAYER1 = e1.get()
	PLAYER2 = e2.get()

	root_.destroy()

	del e1, e2, root_, player1_var, player2_var

#Enter Name
root_ = Tk()
root_.title('TIC TAC TOE')
root_.configure(bg='black')

Label(master=root_, text='TIC', font="Times 25", bg='black', fg='purple').grid(row=0, column=1)
Label(master=root_, text='TAC', font="Times 25", bg='black', fg='silver').grid(row=1, column=1, columnspan=2)
Label(master=root_, text='TOE', font="Times 25", bg='black', fg='gold').grid(row=2, column=2)

Label(master=root_, text="Player 1:", bg='black', fg='brown', font='Arial 14').grid(row=3, column=1)
player1_var = StringVar()
e1 = Entry(master=root_, textvariable=player1_var, fg='dark blue', bg='light green')
e1.insert(0, 'A')
e1.grid(row=3, column=2)

Label(master=root_, text="Player 2:", bg='black', fg='brown', font='Arial 14').grid(row=4, column=1)
player2_var = StringVar()
e2 = Entry(master = root_, textvariable = player2_var, fg='dark blue', bg='light green')
e2.insert(0, 'B')
e2.grid(row=4, column=2)

Button(master=root_, text='Start Game', command=start, fg='yellow', bg='green').grid(row=5, column=1, columnspan=2)

e1.focus_set()
root_.bind('<Return>', start)
root_.protocol("WM_DELETE_WINDOW", sys.exit)
root_.mainloop()




#Main Game
def onExit():
	if SCORE_1 == SCORE_2:
		sys.exit()
	else:
		if SCORE_1>SCORE_2:
			msg.showinfo("Final Result", f"{PLAYER1} won by {SCORE_1 - SCORE_2} matches.")
			sys.exit()
		elif SCORE_1<SCORE_2:
			msg.showinfo("Final Result", f"{PLAYER2} won by {SCORE_2 - SCORE_1} matches.")
			sys.exit()

def displayResult(statement, sc):
	msg.showinfo('Result', statement)

	global Button_list, MATCH_LIST, ScoreLabel, PLAYER1, PLAYER2, SCORE_1, SCORE_2
	MATCH_LIST = [['.','.','.'],['.','.','.'],['.','.','.']]
	ScoreLabel.config(text=f'Score\n{PLAYER1} = {SCORE_1}\n{PLAYER2} = {SCORE_2}')
	for b in Button_list:
		# b.b.config(state='normal')
		b.b.config(text='')


root = Tk()
root.title('TIC TAC TOE Game')
root.configure(bg='black')

Label(master=root, text='TIC', font="Times 25", bg='black', fg='purple').grid(row=0, column=1)
Label(master=root, text='TAC', font="Times 25", bg='black', fg='silver').grid(row=1, column=1, columnspan=2)
Label(master=root, text='TOE', font="Times 25", bg='black', fg='gold').grid(row=2, column=2)

Label(master=root, text=f'{PLAYER1}: X\n{PLAYER2}: O', font="Arial 16", fg='green', bg='black').grid(row=0, column=3)

ScoreLabel = Label(master=root, text=f'Score\n{PLAYER1} = {SCORE_1}\n{PLAYER2} = {SCORE_2}', font="Arial 17", bg='black', fg='cyan')
ScoreLabel.grid(row=2, column=3)

class Create_Button:
	def __init__(self, r, c):
		self.r = r
		self.c = c
		self.b = Button(master=root, width=8, font='Arial 16 bold', height=3, bg='orange', command=self.IamPressed)
		self.b.grid(row=self.r, column=self.c)
		self.symbol = None

	def IamPressed(self):
		global MATCH_LIST, SWAP, SCORE_1, SCORE_2
		
		if self.b['text'] == '':
			if SWAP == 1:
				self.symbol = 'X'
				self.b.config(text=self.symbol, fg='red')
			else:
				self.symbol = 'O'
				self.b.config(text=self.symbol, fg='blue')

			SWAP *= -1

			MATCH_LIST[self.r-3][self.c-1] = self.symbol

			checkWin = self.IamAwinner(self.symbol)
			if checkWin and self.symbol=='X':
				SCORE_1+=1
				displayResult(f'{PLAYER1} is the Winner', 1)
			elif checkWin and self.symbol=='O':
				SCORE_2+=1
				displayResult(f'{PLAYER2} is the Winner', 2)
			elif self.isMatchDraw():
				displayResult("Match Tied", 0)
		
	def IamAwinner(self, sign):
		return ((MATCH_LIST[0][0]==MATCH_LIST[0][1]==MATCH_LIST[0][2]==sign)
		or (MATCH_LIST[1][0]==MATCH_LIST[1][1]==MATCH_LIST[1][2]==sign)
		or (MATCH_LIST[2][0]==MATCH_LIST[2][1]==MATCH_LIST[2][2]==sign)
		or (MATCH_LIST[0][0]==MATCH_LIST[1][1]==MATCH_LIST[2][2]==sign)
		or (MATCH_LIST[0][2]==MATCH_LIST[1][1]==MATCH_LIST[2][0]==sign)
		or (MATCH_LIST[0][0]==MATCH_LIST[1][0]==MATCH_LIST[2][0]==sign)
		or (MATCH_LIST[0][1]==MATCH_LIST[1][1]==MATCH_LIST[2][1]==sign)
		or (MATCH_LIST[0][2]==MATCH_LIST[1][2]==MATCH_LIST[2][2]==sign)
		)

	def isMatchDraw(self):
		global MATCH_LIST
		for i in MATCH_LIST:
			if '.' in i:
				break
		else:
			return 1
		return


for i in range(3, 6):
	for j in range(1, 4):
		Button_list.append(Create_Button(r=i, c=j))

root.protocol("WM_DELETE_WINDOW", onExit)
root.mainloop()
