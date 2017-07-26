from scene import *
from sprites import *
from d_pad import *
from settings import *


class Main (Scene):
	def setup(self):
		self.background_color = '#000000'
		
		self.d_pads = []
		self.bullets = []
		
		self.setup_player1()
		self.setup_player2()
	
	def update(self):
		self.p1_dL.update()
		self.p1_dR.update()
		
		self.p2_dL.update()
		self.p2_dR.update()
		
		self.player1.update()
		self.player2.update()
		
		for b in self.bullets:
			pos = b.get_pos()
			if pos.x < 0 or pos.x > self.size.w or pos.y < 0 or pos.y > self.size.h:
				self.kill_bullet(b)
			b.update()
		
	def setup_player1(self):
		# Create Player 1
		self.player1 = Player()  # from sprites.py
		self.player1.setup(self, (self.size.w / 2, self.size.h / 2), 'blue', 1)
		# Player 1's left d-pad
		self.p1_dL = D_pad()  # from d_pad.py
		self.p1_dL.setup(self, (150, 100), 1, 'L')
		self.d_pads.append(self.p1_dL)
		# Player 1's right d-pad
		self.p1_dR = D_pad()  # from d_pad.py
		self.p1_dR.setup(self, (self.size.w - 150, 100), 1, 'R')
		self.d_pads.append(self.p1_dR)
		
	def setup_player2(self):
		# Create Player 2
		self.player2 = Player()  # from sprites.py
		self.player2.setup(self, (self.size.w / 2 + 100, self.size.h / 2), 'red', 2)
		# Player 2's left d-pad
		self.p2_dL = D_pad()  # from d_pad.py
		self.p2_dL.setup(self, (self.size.w - 150, self.size.h - 100), 2, 'L')
		self.d_pads.append(self.p2_dL)
		# Player 2's right d-pad
		self.p2_dR = D_pad()  # from d_pad.py
		self.p2_dR.setup(self, (150, self.size.h - 100), 2, 'R')
		self.d_pads.append(self.p2_dR)
		
	def get_pad_direction(self, side, player_type):
		for i in range(len(self.d_pads)):
			if self.d_pads[i].get_side() == side:
				if self.d_pads[i].get_joystick_type() == player_type:
					return self.d_pads[i].get_direction()
		
	def append_bullet_list(self, bullet):
		self.bullets.append(bullet)
	
	def get_bullet_list(self):
		return self.bullets
	
	def kill_bullet(self, b):
		self.bullets.remove(b)
		b.remove_bullet()

if __name__ == '__main__':
	run(Main(), orientation=PORTRAIT, show_fps=True)
