from scene import *

class Player (Node):
	def setup(self, game, pos, player_type):
		self.game = game
		self.player_type = player_type
		
		self.player = SpriteNode(color='white', size=(50, 20))
		self.player.position = pos
		self.game.add_child(self.player)
	
	def update(self):
		pass
