from scene import *
from sprites import *
from joystick import *
from settings import *

class Main (Scene):
	def setup(self):
		# Create Player 1
		self.player1 = Player() # from sprites.py
		self.player1.setup(self, (self.size.w / 2, self.size.h / 2))
		
		# Create Player 1's left joystick
		self.p1_joyL = Joystick() # from joystick.py
		self.p1_joyL.setup(self, BASE_R, STICK_R, (DIST, DIST))
		
		# Create Player 1's right joystick
		self.p1_joyR = Joystick() # from joystick.py
		self.p1_joyR.setup(self, BASE_R, STICK_R, (self.size.w - DIST, DIST))
		
		# Get the joystick base
		self.p1_baseL = self.p1_joyL.get_base()
		self.p1_baseR = self.p1_joyR.get_base()
	
	def update(self):
		pass
	
	def touch_began(self, touch):
		pass
	
	def touch_moved(self, touch):
		pass
	
	def touch_ended(self, touch):
		pass

if __name__ == '__main__':
	run(Main(), orientation=PORTRAIT, show_fps=True)
