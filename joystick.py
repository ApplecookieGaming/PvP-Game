from scene import *
from settings import *

class Joystick (Node):
	def setup(self, game, base_d, stick_d, pos):
		self.game = game
		self.pos = pos
		self.base_d = base_d
		
		#base = SpriteNode(color="#ffffff", alpha=0.2, size=(base_size, base_size))
		base_circle = ui.Path.oval(0, 0, self.base_d, self.base_d)
		self.base = ShapeNode(base_circle, '#858585', '#ffffff', alpha=0.3)
		self.base.position = self.pos
		
		#stick = SpriteNode(color="#ffffff", alpha=0.2, size=(stick_size, stick_size))
		stick_circle = ui.Path.oval(0, 0, stick_d, stick_d)
		self.stick = ShapeNode(stick_circle, '#ff0000', '#ffffff', alpha=0.5)
		self.stick.position = self.pos
		
		self.game.add_child(self.base)
		self.game.add_child(self.stick)
	
	def update(self):
		pass
	
	def touch_began(self, touch):
		pass
	
	def touch_moved(self, touch):
		pass
	
	def touch_ended(self, touch):
		pass
		
	def get_base(self):
		return self.base
