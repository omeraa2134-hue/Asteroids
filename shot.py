from circleshape import CircleShape
from constants import LINE_WIDTH,SHOT_RADIUS
import pygame

class Shot(CircleShape):
    
    def __init__(self,x,y):
        super().__init__(x,y,SHOT_RADIUS)
    def draw(self, display):
        pygame.draw.circle(display,"white", self.position, self.radius,width=LINE_WIDTH)
    def update(self, dt):
        self.position += self.velocity * dt
