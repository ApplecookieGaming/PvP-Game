from scene import *
from main import *
from settings import *
from math import degrees, radians, sqrt
A = Action


class Player (Node):
	def setup(self, game, pos, colour, player_type):
		self.game = game
		self.player_type = player_type
		
		self.player = SpriteNode(color=colour, size=(50, 20))
		self.player.position = pos
		self.game.add_child(self.player)
	
	def update(self):
		left_pad = Main.get_player_direction(self.game, 'L', self.player_type)
			
		if left_pad == 'up':
			self.player.rotation = self.rotate(0)
			self.player.position += (0, SPEED)
		elif left_pad == 'left_up':
			self.player.rotation = self.rotate(45)
			self.player.position += (-SPEED_D, SPEED_D)
		elif left_pad == 'left':
			self.player.rotation = self.rotate(90)
			self.player.position += (-SPEED, 0)
		elif left_pad == 'left_down':
			self.player.rotation = self.rotate(135)
			self.player.position += (-SPEED_D, -SPEED_D)
		elif left_pad == 'down':
			self.player.rotation = self.rotate(180)
			self.player.position += (0, -SPEED)
		elif left_pad == 'right_down':
			self.player.rotation = self.rotate(-135)
			self.player.position += (SPEED_D, -SPEED_D)
		elif left_pad == 'right':
			self.player.rotation = self.rotate(-90)
			self.player.position += (SPEED, 0)
		elif left_pad == 'right_up':
			self.player.rotation = self.rotate(-45)
			self.player.position += (SPEED_D, SPEED_D)
		
		'''
		# Debug
		if left_pad != 'none':
			print("Player " + str(self.player_type) + " is moving " + left_pad)
		'''
			
	def rotate(self, deg):
		inital_d = self.myround(degrees(self.player.rotation))
		
		if inital_d == 180 and 0 > deg:
			inital_d *= -1
		if deg == 180 and 0 > inital_d:
			deg *= -1
		
		deg_rel1 = deg - inital_d  # First relative rotation of angle
		
		# Second relative rotation of angle
		if deg_rel1 > 0:
			deg_rel2 = deg_rel1 - 360
		else:
			deg_rel2 = deg_rel1 + 360
		
		# Choose smallest relative angle
		if abs(deg_rel1) < abs(deg_rel2):
			deg_rel = deg_rel1
		else:
			deg_rel = deg_rel2
			
		rot_speed = max(self.myround((abs(deg_rel) / ROT_TIME)), 5)  # speed = distance / time
		
		'''
		# Debug
		print("initial_d = " + str(inital_d) + ", deg = "
					+ str(deg) + ", deg_rel = " + str(deg_rel)
					+ ", rot_speed = " + str(rot_speed))
		'''
		
		if 0 < deg_rel:
			inital_d += rot_speed
		elif 0 > deg_rel:
			inital_d -= rot_speed
		
		# print(str(inital_d))
		
		return radians(inital_d)
	
	# Code from https://stackoverflow.com/questions/2272149/round-to-5-or-other-number-in-python
	# By Alok Singhal
	def myround(self, x, base=5):
		return int(base * round(float(x)/base))
