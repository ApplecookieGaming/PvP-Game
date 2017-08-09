from scene import *
from main import *
from settings import *
from random import uniform, randrange
from math import pi

class ParticleFX (Node):
	def setup(self, game, effect, pos, fx_size, fx_color, spread, amount):
		self.game = game
		self.effect = effect
		self.particles = []
		
		if self.effect == 'playerDeath':
			for i in range(amount):
				death_fx = Particle()
				death_fx.setup(self.game, pos, fx_size, fx_color, spread)
				self.particles.append(death_fx)
	
	def update(self):
		for p in self.particles:
			p.update()
			counter = p.get_counter()
			self.fx = p.get_effect()
			
			self.fx.alpha -= (1 / FX_DESPAWN)
			
			if counter > FX_DESPAWN:
				self.kill_particle(p)
	
	def kill_particle(self, particle):
		self.fx.remove_from_parent()
		particle.remove_from_parent()
		self.particles.remove(particle)


class Particle (Node):
	def setup(self, game, pos, fx_size, col, spread):
		self.game = game
		
		self.counter = 0
		
		self.fx = SpriteNode(color=col, position=pos, size=fx_size)
		self.game.add_child(self.fx)
		
		self.vel = Vector2(uniform(-spread, spread), (uniform(-spread, spread)))
		self.rot = uniform(-1, 1)
		
	def update(self):
		self.counter += 1
		
		self.vel *= (0.9, 0.9)
		self.rot *= 0.9
		
		self.fx.position += self.vel
		self.fx.rotation += self.rot
		
	def get_counter(self):
		return self.counter
	
	def get_effect(self):
		return self.fx
