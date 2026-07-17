import pygame
from constants import SCREEN_WIDTH,SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot
import sys

def main():

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}",
          f"Screen height: {SCREEN_HEIGHT}",
          sep="\n")
    
    pygame.init()

    time = pygame.time.Clock()
    dt = 0.0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots,drawable,updatable)

    AsteroidField.containers = (updatable,)

    Asteroid.containers = (asteroids, updatable, drawable)

    Player.containers = (updatable,drawable)

    player= Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    astroidfield = AsteroidField()

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)

        for every_asteroid in asteroids:
            if player.collides_with(every_asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        
        for every_asteroid in asteroids:
            for every_shot in shots:
                if every_shot.collides_with(every_asteroid):
                    log_event("asteroid_shot")
                    every_shot.kill()
                    every_asteroid.split()

        screen.fill("black")
        for every_object in drawable:

            every_object.draw(screen)

        pygame.display.flip()

        dt = time.tick(60) / 1000

if __name__ == "__main__":
    main()

