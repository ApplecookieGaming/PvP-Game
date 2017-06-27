from scene import *

class Player (Node):
	def setup(self, game, pos):
		player = SpriteNode(color='white', size=(50, 20))
		player.position = pos
		game.add_child(player)
