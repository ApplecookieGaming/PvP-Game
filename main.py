from scene import *
from sprites import *
from d_pad import *
from settings import *

class Main (Scene):
	def setup(self):
		self.setup_player1()
		self.setup_player2()
	
	def update(self):
		self.p1_dL.update()
		self.p1_dR.update()
		
		self.p2_dL.update()
		self.p2_dR.update()
		
	def setup_player1(self):
		# Create Player 1
		self.player1 = Player() # from sprites.py
		self.player1.setup(self, (self.size.w / 2, self.size.h / 2), 1)
		# Player 1's left d-pad
		self.p1_dL = D_pad() # from d_pad.py
		self.p1_dL.setup(self, (150, 100), 1, 'L')
		# Player 1's right d-pad
		self.p1_dR = D_pad() # from d_pad.py
		self.p1_dR.setup(self, (self.size.w - 150, 100), 1, 'R')
		
	def setup_player2(self):
		# Create Player 2
		self.player2 = Player() # from sprites.py
		self.player2.setup(self, (self.size.w / 2 + 100, self.size.h / 2), 2)
		# Player 2's left d-pad
		self.p2_dL = D_pad() # from d_pad.py
		self.p2_dL.setup(self, (self.size.w - 150, self.size.h - 100), 2, 'L')
		# Player 2's right d-pad
		self.p2_dR = D_pad() # from d_pad.py
		self.p2_dR.setup(self, (150, self.size.h - 100), 2, 'R')

if __name__ == '__main__':
	run(Main(), orientation=PORTRAIT, show_fps=True)
