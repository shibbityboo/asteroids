from circleshape import *
from constants import *
import random
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <+ ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle1 = self.velocity.rotate(random.uniform(20, 50))
        angle2 = self.velocity.rotate(-random.uniform(20, 50))
        rad1 = self.radius - ASTEROID_MIN_RADIUS
        rad2 = self.radius - ASTEROID_MIN_RADIUS
        ast1 = Asteroid(self.position.x, self.position.y, rad1)
        ast2 = Asteroid(self.position.x, self.position.y, rad2)
        ast1.velocity = angle1 * 1.2
        ast2.velocity = angle2 * 1.2

        