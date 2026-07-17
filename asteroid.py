import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random
class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, display):
        pygame.draw.circle(display,"white", self.position, self.radius,width=LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random_degree = random.uniform(20,50)
        asteroid1_movement = self.velocity.rotate(random_degree)
        asteroid2_movement = self.velocity.rotate(-random_degree)
        asteroid_radiuses = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x,self.position.y, asteroid_radiuses)
        asteroid2 = Asteroid(self.position.x,self.position.y, asteroid_radiuses)
        asteroid1.velocity = asteroid1_movement * 1.2
        asteroid2.velocity = asteroid2_movement * 1.2

