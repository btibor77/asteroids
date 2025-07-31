import pygame
from constants import *
from player import *
def main():
    pygame.init()
    game=True
    clock=pygame.time.Clock()
    dt=0
    player=Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    # print(pygame.get_init())
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        dt=clock.tick()/1000

if __name__ == "__main__":
    main()
