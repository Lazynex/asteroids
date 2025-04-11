# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame, sys

from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # init
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    # groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    # player
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    # asteroids
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()

    # shots
    Shot.containers = (shots, updatable, drawable)

    # game loop
    while True:
        # close window on press X
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
    
        # update
        updatable.update(dt)
        for d in drawable:
            d.draw(screen)

        for a in asteroids:
            if a.collides(player):
                print("Game over!")
                sys.exit()
            for s in shots:
                if s.collides(a):
                    a.split()
                    s.kill()
        
        # flip screen
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()