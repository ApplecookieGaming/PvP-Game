from scene import *
from main import *
from settings import *
from math import sin, cos, degrees, radians, sqrt


class Player (Node):
	def setup(self, game, pos, colour, player_type):
		self.game = game
		self.player_type = player_type
		
		self.player = SpriteNode(color=colour, size=(50, 20))
		self.player.position = pos
		self.game.add_child(self.player)
		
		self.health = 100
		self.cooldown = 0
		
		if self.player_type == 1:
			self.bar1 = HealthBar()
			self.bar1.setup(self.game, '#00ddff', '#0016ff', (self.game.size.w / 2, 200), self.player_type)
			
		elif self.player_type == 2:
			self.bar2 = HealthBar()
			self.bar2.setup(self.game, '#ff3c00', '#ff0000', (self.game.size.w / 2, 550), self.player_type)
		
		self.rot = 0
		self.vel = Vector2(0, 0)
		self.acc = Vector2(0, 0)
	
	def update(self):
		self.left_pad()
		self.right_pad()
		
		if self.cooldown > 0:
			self.cooldown -= 1
		
		# Limits max/min acceleration
		if self.acc[0] > MAX_ACC:
			self.acc.x = MAX_ACC
		if self.acc[1] > MAX_ACC:
			self.acc.y = MAX_ACC
		
		self.player.position += self.vel * self.acc  # Adds friction
		self.player.rotation = self.rot
	
	# Function to rotate player in the correct direction
	def rotate(self, deg):
		inital_d = self.myround(degrees(self.player.rotation))
		
		# Reverse signs to rotate in the correct direction
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
			
		rot_MAX_SPEED = max( self.myround( abs(deg_rel) / ROT_TIME ) , 5)  # speed = distance / time
		
		# Determine which direction to turn
		if 0 < deg_rel:
			inital_d += rot_MAX_SPEED
		elif 0 > deg_rel:
			inital_d -= rot_MAX_SPEED
		
		# Return output in radians
		return radians(inital_d)
	
	def left_pad(self):
		left_pad = Main.get_pad_direction(self.game, 'L', self.player_type)
		
		if left_pad != 'none':
			
			self.acc += Vector2(ACC, ACC)
			
			if left_pad == 'up':
				self.rot = self.rotate(0)
				self.vel = Vector2(0, MAX_SPEED)
				
			elif left_pad == 'left_up':
				self.rot = self.rotate(45)
				self.vel = Vector2(-MAX_SPEED_D, MAX_SPEED_D)
			
			elif left_pad == 'left':
				self.rot = self.rotate(90)
				self.vel = Vector2(-MAX_SPEED, 0)
			
			elif left_pad == 'left_down':
				self.rot = self.rotate(135)
				self.vel = Vector2(-MAX_SPEED_D, -MAX_SPEED_D)
			
			elif left_pad == 'down':
				self.rot = self.rotate(180)
				self.vel = Vector2(0, -MAX_SPEED)
			
			elif left_pad == 'right_down':
				self.rot = self.rotate(-135)
				self.vel = Vector2(MAX_SPEED_D, -MAX_SPEED_D)
			
			elif left_pad == 'right':
				self.rot = self.rotate(-90)
				self.vel = Vector2(MAX_SPEED, 0)
			
			elif left_pad == 'right_up':
				self.rot = self.rotate(-45)
				self.vel = Vector2(MAX_SPEED_D, MAX_SPEED_D)
				
		else:
			# If the player isn't moving, add friciton to slow down
			if self.acc > (0, 0):
				self.acc += (FRICTION, FRICTION)
			else:
				self.acc = (0, 0)
				
	def right_pad(self):
		right_pad = Main.get_pad_direction(self.game, 'R', self.player_type)
		
		if right_pad != 'none':
			if self.cooldown <= 0:
				self.cooldown = SHOOT_RATE
				bullet = Bullet()
				bullet.setup(self.game, self, self.player_type)
				Main.append_bullet_list(self.game, bullet)
			
			if right_pad == 'up':
				self.rot = self.rotate(0)
				
			elif right_pad == 'left_up':
				self.rot = self.rotate(45)
			
			elif right_pad == 'left':
				self.rot = self.rotate(90)
			
			elif right_pad == 'left_down':
				self.rot = self.rotate(135)
			
			elif right_pad == 'down':
				self.rot = self.rotate(180)
			
			elif right_pad == 'right_down':
				self.rot = self.rotate(-135)
			
			elif right_pad == 'right':
				self.rot = self.rotate(-90)
			
			elif right_pad == 'right_up':
				self.rot = self.rotate(-45)
	
	def get_player(self, player_type):
		if self.player_type == player_type:
			return self.player
		
	# Code from https://stackoverflow.com/questions/2272149/round-to-5-or-other-number-in-python
	# By Alok Singhal
	# This is used to round numbers to a base, in this case, 5
	# e.g. myround(12) --> 10, myround(16) --> 15
	def myround(self, x, base=5):
		return int(base * round(float(x)/base))

		
class Bullet (Node):
	def setup(self, game, player_class, bullet_type):
		self.game = game
		self.player_class = player_class
		self.player = Player.get_player(self.player_class, bullet_type)
		
		self.bullet = SpriteNode(color='#f3ff00', size=(10, 20))
		self.bullet.position = self.player.position + self.rotate_number(self.player.size.h / 2, self.player.rotation)
		self.bullet.rotation = self.player.rotation
		self.game.add_child(self.bullet)
		
		self.vel = self.rotate_number(BULLET_SPEED, self.player.rotation)
		
	def update(self):
		self.bullet.position += self.vel
	
	def rotate_number(self, speed, rad):
		x = speed * sin(rad)
		y = speed * cos(rad)
		
		x *= -1  # Reverse sign
		
		vec = Vector2(x, y)
		return vec
	
	def get_pos(self):
		return self.bullet.position
	
	def remove_bullet(self):
		self.bullet.remove_from_parent()


class HealthBar (Node):
	def setup(self, game, fore, back, pos, health_type):
		self.game = game
		
		bar_size = (self.game.size.w / 2 - 70, 20)
		
		self.back = SpriteNode(color=back, size=bar_size)
		self.fore = SpriteNode(color=fore, size=bar_size)
		
		self.back.anchor_point = (1, 0)
		self.fore.anchor_point = (1, 0)
	
		self.back.position = pos
		self.fore.position = pos
		
		if health_type == 2:
			self.back.x_scale = -1
			self.fore.x_scale = -1
		
		self.game.add_child(self.back)
		self.game.add_child(self.fore)
	
	def update(self):
		pass
