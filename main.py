import sys

import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from circleshape import *
from shot import *
def main():
    pygame.init()
    game=True
    clock=pygame.time.Clock()
    dt=0
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()
    Player.containers = (updatable_group, drawable_group)
    Asteroid.containers = (asteroid_group, updatable_group, drawable_group)
    AsteroidField.containers = updatable_group
    asteroidfield=AsteroidField()
    player=Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, shots_group)
    # print(pygame.get_init())
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # print(len(updatable_group), len(drawable_group))
    while game:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable_group.update(dt)
        shots_group.update(dt)
        for asteroid in asteroid_group:
            if asteroid.collisions(player):
                sys.exit("Game over!")
        for asteroid in asteroid_group:
            for bullet in shots_group:
                if asteroid.collisions(bullet):
                    asteroid.split()
                    bullet.kill()
        for item in drawable_group:
            item.draw(screen)
        for shot in shots_group:
            shot.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
