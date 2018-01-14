#sudo apt-get install python-tk
#sudo apt-get install python3-tk

# This code is just for education purpose and its no my creation i just make exercise

from Tkinter import *
import random
import time
from game2 import Paddle

class Ball:
	def __init__(self, canvas,paddle, color):
		self.canvas = canvas 
		self.paddle = paddle
		self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
		self.canvas.move(self.id, 245, 100)
		starts = [-3, -2, -1, 1, 2, 3]
		random.shuffle(starts)
		self.x = starts[0]
		self.y = -3
		self.canvas_height = self.canvas.winfo_height()
		self.canvas_width = self.canvas.winfo_width()
		self.hit_bottom = False

	def hit_paddle(self, pos):
		paddle_pos = self.canvas.coords(self.paddle.id)
		if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
			if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
				return True
		return False

	def draw(self):
		self.canvas.move(self.id, self.x, self.y)
		pos = self.canvas.coords(self.id)
		if pos[1] <= 0:
			self.y = 3
		if pos[3] >=  self.canvas_height:
			self.hit_bottom = True
		if self.hit_paddle(pos) == True:
			self.y = - 3
		if pos[0] <= 0:
			self.x = 3
		if pos[2] >= self.canvas_width:
			self.x = -3


tk = Tk()
tk.title("Igrica")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height = 400, bd = 0, highlightthickness = 0)
canvas.pack()
tk.update()

paddle = Paddle(canvas, 'green')
ball = Ball(canvas,paddle, 'red')

while 1:
	if ball.hit_bottom == False:
		ball.draw()
		paddle.draw()
	tk.update_idletasks()
	tk.update()
	time.sleep(0.01)