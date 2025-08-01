from circleshape import *
from constants import *
class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        self.radius = SHOT_RADIUS

    def draw(self, screen):
        pygame.draw.circle (screen, "red", self.position, self.radius)

    def update(self, dt):
        self.move(dt)
    def move(self, dt):
        # forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += self.velocity*dt