from scene import *
from settings import *

class D_pad (Node):
	def setup(self, game, pos, joystick_type, side):
		self.game = game # Reference to main.py
		self.direction = 'none' # Direction pressed
		self.joystick_type = joystick_type # What player does it belong to?
		self.side = side # Left or right side?
				
		# Make 8 directional pad
		self.center = self.make_button(pos)
		self.left = self.make_button((pos[0] - D_SIZE[0], pos[1]))
		self.right = self.make_button((pos[0] + D_SIZE[0], pos[1]))
		self.down = self.make_button((pos[0], pos[1] - D_SIZE[1]))
		self.up = self.make_button((pos[0], pos[1] + D_SIZE[1]))
		self.left_down = self.make_button((pos[0] - D_SIZE[0], pos[1] - D_SIZE[1]))
		self.left_up = self.make_button((pos[0] - D_SIZE[0], pos[1] + D_SIZE[1]))
		self.right_down = self.make_button((pos[0] + D_SIZE[0], pos[1] - D_SIZE[1]))
		self.right_up = self.make_button((pos[0] + D_SIZE[0], pos[1] + D_SIZE[1]))
		
	def update(self):
		self.touch_button(self.left, 'left')
		self.touch_button(self.right, 'right')
		self.touch_button(self.down, 'down')
		self.touch_button(self.up, 'up')
		self.touch_button(self.left_down, 'left_down')
		self.touch_button(self.left_up, 'left_up')
		self.touch_button(self.right_down, 'right_down')
		self.touch_button(self.right_up, 'right_up')
		
	def make_button(self, pos):
		button = SpriteNode(size=D_SIZE, color='white', alpha=D_ALPHA, position=pos)
		self.game.add_child(button)
		return button
		
	def touch_button(self, button, direction):
		button.alpha = D_ALPHA
		self.direction = 'none'
		for t in self.game.touches.values():
			if button.frame.contains_point(t.location):
				button.alpha += 0.1
				self.direction = direction
				
	def get_joystick_type(self):
		return self.joystick_type
				
	def get_direction(self):
		return self.direction
