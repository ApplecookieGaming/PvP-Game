from scene import *
from main import *
from settings import *
from math import sin, cos, tan, degrees, radians, sqrt


class Player (Node):
	def setup(self, game, pos, colour, player_type):
		self.game = game
		self.player_type = player_type
		
		self.player = SpriteNode(color=colour, size=(50, 20))
		self.player.position = pos
		self.game.add_child(self.player)
		
		self.health = MAX_HEALTH
		self.energy = MAX_ENERGY
		self.cooldown = 0
		self.hitboxes = []
		
		## Resource bars
		if self.player_type == 1:
			# Health bar
			self.h_bar1 = ResourceBar()
			h_bar1_pos = (self.game.size.w / 2, BAR_DIST)
			self.h_bar1.setup(self.game, self, h_bar1_pos, self.player_type, 'health')
			
			# Energy bar
			self.e_bar1 = ResourceBar()
			e_bar1_pos = (self.game.size.w / 2, BAR_DIST)
			self.e_bar1.setup(self.game, self, e_bar1_pos, self.player_type, 'energy')
			
		elif self.player_type == 2:
			self.h_bar2 = ResourceBar()
			h_bar2_pos = (self.game.size.w / 2, self.game.size.h - BAR_DIST)
			self.h_bar2.setup(self.game, self, h_bar2_pos, self.player_type, 'health')
			
			self.e_bar2 = ResourceBar()
			e_bar2_pos = (self.game.size.w / 2, self.game.size.h - BAR_DIST)
			self.e_bar2.setup(self.game, self, e_bar2_pos, self.player_type, 'energy')
		
		self.setup_hitboxes()
		
		self.rot = 0
		self.vel = Vector2(0, 0)
		self.acc = Vector2(0, 0)
	
	def update(self):
		self.left_pad()
		self.right_pad()
		
		self.update_hitbox()
		
		if self.cooldown > 0:
			self.cooldown -= 1
		
		if self.energy < MAX_ENERGY:
			self.energy += ENERGY_REGEN
		
		# Limits max/min acceleration
		if self.acc[0] > MAX_ACC:
			self.acc.x = MAX_ACC
		if self.acc[1] > MAX_ACC:
			self.acc.y = MAX_ACC
		
		self.player.position += self.vel * self.acc  # Adds friction
		self.player.rotation = self.rot
		
		self.bullet_collision()
		
		# Health
		if self.player_type == 1:
			self.h_bar1.update()
			self.e_bar1.update()
		elif self.player_type == 2:
			self.h_bar2.update()
			self.e_bar2.update()
		
		#if self.health <= 0:
			#self.kill()
	
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
			if self.cooldown <= 0 and self.energy >= BULLET_DEP:
				self.cooldown = SHOOT_RATE
				
				bullet = Bullet()
				bullet.setup(self.game, self, self.player_type)
				Main.append_bullet_list(self.game, bullet)
				
				self.energy -= BULLET_DEP
			
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
	
	def bullet_collision(self):
		bullets = Main.get_bullet_list(self.game)
		
		for b in bullets:
			if b.get_type() != self.player_type:
				bullet_rect = b.get_bbox()
				
				for h in self.player_hitboxes:
					if h.intersects(bullet_rect):
						try:							
							self.health -= BULLET_DAMG
							Main.kill_bullet(self.game, b)
						except Exception:
							pass
	
	def get_player(self, player_type):
		if self.player_type == player_type:
			return self.player
	
	def get_health(self, player_type):
		return self.health
		
	def get_energy(self, player_type):
		return self.energy
	
	def kill(self):
		self.player.remove_from_parent()
	
	def setup_hitboxes(self):
		self.player_hitboxes = []
		
		# Middle hitbox
		mid_x = self.player.position.x
		mid_y = self.player.position.y
		mid_w = self.player.size.w / 3
		mid_h = self.player.size.w / 3
		self.hitbox_mid = Rect(mid_x, mid_y, mid_w, mid_h)
		self.player_hitboxes.append(self.hitbox_mid)
		
		# Left hitbox
		left_x = self.player.position.x
		left_y = self.player.position.y
		left_w = self.player.size.w / 3
		left_h = self.player.size.w / 3
		self.hitbox_left = Rect(left_x, left_y, left_w, left_h)
		self.player_hitboxes.append(self.hitbox_left)
		
		# Right hitbox
		right_x = self.player.position.x
		right_y = self.player.position.y
		right_w = self.player.size.w / 3
		right_h = self.player.size.w / 3
		self.hitbox_right = Rect(right_x, right_y, right_w, right_h)
		self.player_hitboxes.append(self.hitbox_right)
		
		if SHOW_HITBOX:
			# Middle hixbox display
			self.outline_mid = SpriteNode(texture='assets/outline.png')
			self.outline_mid.anchor_point = (0, 0)
			self.outline_mid.position = self.hitbox_mid.origin
			self.outline_mid.size = self.hitbox_mid.size
			self.game.add_child(self.outline_mid)
			
			# Left hitbox display
			self.outline_left = SpriteNode(texture='assets/outline.png')
			self.outline_left.anchor_point = (0, 0)
			self.outline_left.position = self.hitbox_left.origin
			self.outline_left.size = self.hitbox_left.size
			self.game.add_child(self.outline_left)
			
			# Right hitbox display
			self.outline_right = SpriteNode(texture='assets/outline.png')
			self.outline_right.anchor_point = (0, 0)
			self.outline_right.position = self.hitbox_right.origin
			self.outline_right.size = self.hitbox_right.size
			self.game.add_child(self.outline_right)
	
	def update_hitbox(self):
		# Middle hitbox
		mid_x = self.player.position.x
		mid_y = self.player.position.y
		self.hitbox_mid.center(mid_x, mid_y)
		
		# Left hitbox
		left_x = self.player.position.x - self.hitbox_left.size.w * cos(self.rot)
		left_y = self.player.position.y - self.hitbox_left.size.h * sin(self.rot)
		self.hitbox_left.center(left_x, left_y)
		
		# Right hitbox
		right_x = self.player.position.x + self.hitbox_right.size.w * cos(self.rot)
		right_y = self.player.position.y - self.hitbox_right.size.h * -sin(self.rot)
		self.hitbox_right.center(right_x, right_y)
		
		if SHOW_HITBOX:
			self.outline_mid.position = self.hitbox_mid.origin
			self.outline_left.position = self.hitbox_left.origin
			self.outline_right.position = self.hitbox_right.origin
		
		if self.player_type == 1:
			# print("sin(" + str(self.rot) + ") = " + str(sin(self.rot)) + '	' + "cos(" + str(self.rot) + ") = " + str(cos(self.rot)) + '	' + "tan(" + str(self.rot) + ") = " + str(tan(self.rot)))
			
			# print("sin(" + str(self.rot) + ") = " + str(sin(self.rot)))
			# print("cos(" + str(self.rot) + ") = " + str(cos(self.rot)))
			# print("tan(" + str(self.rot) + ") = " + str(tan(self.rot)))
			pass
	
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
		self.bullet_type = bullet_type
		
		self.bullet = SpriteNode(color=BULLET_COL, size=(10, 10))
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
		
		return Vector2(x, y)
	
	def get_pos(self):
		return self.bullet.position
	
	def remove_bullet(self):
		self.bullet.remove_from_parent()
	
	def get_type(self):
		return self.bullet_type
	
	def get_bbox(self):
		return self.bullet.bbox


class ResourceBar (Node):
	def setup(self, game, player_class, pos, resource_type, type):
		self.game = game
		self.player_class = player_class
		self.resource_type = resource_type
		self.type = type
		
		bar_size = (self.game.size.w / 2 - 70, BAR_HEIGHT)
		
		if type == 'health':
			self.back = SpriteNode(color=HB_COL, size=bar_size)
			self.fore = SpriteNode(color=HF_COL, size=bar_size)
			
			if resource_type == 1:
				self.back.anchor_point = (1, 0)
				self.fore.anchor_point = (1, 0)
				
			elif resource_type == 2:
				self.back.anchor_point = (1, 1)
				self.fore.anchor_point = (1, 1)
			
		elif type == 'energy':
			self.back = SpriteNode(color=EB_COL, size=bar_size)
			self.fore = SpriteNode(color=EF_COL, size=bar_size)
			
			if resource_type == 1:
				self.back.anchor_point = (0, 0)
				self.fore.anchor_point = (0, 0)
				
			elif resource_type == 2:
				self.back.anchor_point = (0, 1)
				self.fore.anchor_point = (0, 1)
				
		if resource_type == 2:
			self.back.x_scale = -1
			self.fore.x_scale = -1
		
		self.back.position = pos
		self.fore.position = pos
		
		self.game.add_child(self.back)
		self.game.add_child(self.fore)
	
	def update(self):
		if self.type == 'health':
			health = Player.get_health(self.player_class, self.resource_type)
			self.fore.size = (self.back.size.x * (health / MAX_HEALTH), self.back.size.y)
			
		elif self.type == 'energy':
			energy = Player.get_energy(self.player_class, self.resource_type)
			self.fore.size = (self.back.size.x * (energy / MAX_ENERGY), self.back.size.y)
