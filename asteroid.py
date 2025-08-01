from circleshape import *
from constants import *
import random
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        self.position = pygame.Vector2(x, y)
        self.radius=radius

    def draw(self, screen):
        pygame.draw.circle (screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.move(dt)
    def move(self, dt):
        # forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += self.velocity*dt
    def split(self):
        self.kill()
        if self.radius<=ASTEROID_MIN_RADIUS:
            return
        new_angle=random.uniform(20,50)
        vector_one=self.velocity.rotate(new_angle)
        vector_two=self.velocity.rotate(-new_angle)
        new_radius=self.radius-ASTEROID_MIN_RADIUS
        aster_one=Asteroid(self.position.x, self.position.y, new_radius)
        aster_one.velocity=vector_one*1.2
        aster_two = Asteroid(self.position.x, self.position.y, new_radius)
        aster_two.velocity = vector_two*1.2