from scene import *
from sprites import *
from effects import *
from d_pad import *
from settings import *


class Main (Scene):
	def setup(self):
		self.background_color = '#000000'
		
		self.d_pads = []
		self.bullets = []
		self.particles = []
		
		self.setup_player1()
		self.setup_player2()
	
	def update(self):
		self.p1_dL.update()
		self.p1_dR.update()
		
		self.p2_dL.update()
		self.p2_dR.update()
		
		
		if self.player1.get_health(1) <= 0 and self.p1_alive == True:
			# Kill player 1
			self.p1_alive = False
			self.player1.kill()
			self.player1.remove_from_parent()
			
			self.p1_fx = ParticleFX()
			self.p1_fx.setup(self, 'playerDeath', self.player1.get_player(1).position, (25, 20), 'blue', 3, 2)
			
		elif self.p1_alive == True:
			# Keep updating player 1
			self.player1.update()
		
		else:
			# Update player 1's death effects
			self.p1_fx.update()
			
		if self.player2.get_health(2) <= 0 and self.p2_alive == True:
			# Kill player 2
			self.player2.kill()
			self.player2.remove_from_parent()
			
			self.p2_fx = ParticleFX()
			self.p2_fx.setup(self, 'playerDeath', self.player2.get_player(2).position, (25, 20), 'red', 3, 2)
			self.p2_alive = False
			
		elif self.p2_alive == True:
			# Keep updating player 2
			self.player2.update()
		
		else:
			# Update player 2's death effects
			self.p2_fx.update()
		
		for b in self.bullets:
			pos = b.get_pos()
			# Check if a bullet goes off the screen
			if pos.x < 0 or pos.x > self.size.w or pos.y < 0 or pos.y > self.size.h:
				self.kill_bullet(b)
			b.update()  # Update all bullets
		
		# Update all particle effects
		for p in self.particles:
			p.update()
		
	def setup_player1(self):
		# Create Player 1
		self.player1 = Player()  # from sprites.py
		self.player1.setup(self, (self.size.w / 2, self.size.h / 2), P1_COL, 1)
		# Player 1's left d-pad
		self.p1_dL = D_pad()  # from d_pad.py
		self.p1_dL.setup(self, (150, 100), 1, 'L')
		self.d_pads.append(self.p1_dL)
		# Player 1's right d-pad
		self.p1_dR = D_pad()  # from d_pad.py
		self.p1_dR.setup(self, (self.size.w - 150, 100), 1, 'R')
		self.d_pads.append(self.p1_dR)
		# Determins if player is alive or dead
		self.p1_alive = True
		
	def setup_player2(self):
		# Create Player 2
		self.player2 = Player()  # from sprites.py
		self.player2.setup(self, (self.size.w / 2 + 100, self.size.h / 2), P2_COL, 2)
		# Player 2's left d-pad
		self.p2_dL = D_pad()  # from d_pad.py
		self.p2_dL.setup(self, (self.size.w - 150, self.size.h - 100), 2, 'L')
		self.d_pads.append(self.p2_dL)
		# Player 2's right d-pad
		self.p2_dR = D_pad()  # from d_pad.py
		self.p2_dR.setup(self, (150, self.size.h - 100), 2, 'R')
		self.d_pads.append(self.p2_dR)
		# Determins if player is alive or dead
		self.p2_alive = True
		
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
	
	def append_particle_list(self, particle):
		self.particles.append(particle)

if __name__ == '__main__':
	run(Main(), orientation=PORTRAIT, show_fps=True)
