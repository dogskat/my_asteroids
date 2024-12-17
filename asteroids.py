import pygame
import random
from constants import ASTEROID_MIN_RADIUS
from circleshape import CircleShape


SPLIT_SPEED_SCALER = 1.2


class Asteroid(CircleShape):
    
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)

	def draw(self, screen):
		pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

	def update(self, dt):
		self.position += self.velocity * dt

	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		random_angle = random.uniform(20, 50)
		new_radius = self.radius - ASTEROID_MIN_RADIUS
		self._create_new_asteroid(new_radius, random_angle)
		self._create_new_asteroid(new_radius, -random_angle)

	def _create_new_asteroid(self, radius, angle):
		velocity = self.velocity.rotate(angle) * SPLIT_SPEED_SCALER
		new_asteroid = Asteroid(self.position.x, self.position.y, radius)
		new_asteroid.velocity = velocity

