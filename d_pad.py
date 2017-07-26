from scene import *
from settings import *


class D_pad (Node):
	def setup(self, game, pos, joystick_type, side):
		self.game = game  # Reference to main.py
		self.direction = 'none'  # Direction pressed
		self.joystick_type = joystick_type  # What player does it belong to?
		self.side = side  # Left or right side?
		
		self.d_size = (self.game.size.w/20, self.game.size.w/20)
		
		# Make 8 directional pad
		self.center = self.make_button(pos)
		self.left = self.make_button((pos[0] - self.d_size[0], pos[1]))
		self.right = self.make_button((pos[0] + self.d_size[0], pos[1]))
		self.down = self.make_button((pos[0], pos[1] - self.d_size[1]))
		self.up = self.make_button((pos[0], pos[1] + self.d_size[1]))
		self.left_down = self.make_button((pos[0] - self.d_size[0], pos[1] - self.d_size[1]))
		self.left_up = self.make_button((pos[0] - self.d_size[0], pos[1] + self.d_size[1]))
		self.right_down = self.make_button((pos[0] + self.d_size[0], pos[1] - self.d_size[1]))
		self.right_up = self.make_button((pos[0] + self.d_size[0], pos[1] + self.d_size[1]))
		
	def update(self):
		self.direction = 'none'
		
		self.touch_button(self.left, 'left')
		self.touch_button(self.right, 'right')
		self.touch_button(self.down, 'down')
		self.touch_button(self.up, 'up')
		self.touch_button(self.left_down, 'left_down')
		self.touch_button(self.left_up, 'left_up')
		self.touch_button(self.right_down, 'right_down')
		self.touch_button(self.right_up, 'right_up')
		
	def make_button(self, pos, d_alpha=D_ALPHA):
		button = SpriteNode(size=self.d_size, color='white', alpha=d_alpha, position=pos)
		self.game.add_child(button)
		return button
		
	def touch_button(self, button, direction):
		button.alpha = D_ALPHA
		for t in self.game.touches.values():
			if button.frame.contains_point(t.location):
				button.alpha = D_ALPHA - 0.1
				self.direction = direction
				
	def get_side(self):
		return self.side
		
	def get_joystick_type(self):
		return self.joystick_type
				
	def get_direction(self):
		return self.direction
