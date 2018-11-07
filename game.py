import pygame
from pygame.math import Vector2
from math import tan, radians, degrees, copysign
import time
import config
class Game:
    def __init__(self):
        pygame.init()
        self.gameDisplay = pygame.display.set_mode((config.display_width,config.display_height))
        pygame.display.set_caption(config.title)
        self.gameDisplay.fill(config.white)
        self.clock = pygame.time.Clock()
        self.cars = pygame.sprite.Group()
        self.cars.add(Car(config.display_height/2,config.display_width/2))
    def run(self):
        breaking = 0
        acceleration = 0
        steering = 0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()
                    elif event.key == pygame.K_w:
                        acceleration += 1
                    elif event.key == pygame.K_s:
                        acceleration -= 1
                    elif event.key == pygame.K_a:
                        steering -= 1
                    elif event.key == pygame.K_d:
                        steering += 1
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()
                    elif event.key == pygame.K_w:
                        acceleration -= 1
                    elif event.key == pygame.K_s:
                        acceleration += 1
                    elif event.key == pygame.K_a:
                        steering += 1
                    elif event.key == pygame.K_d:
                        steering -= 1

            self.cars.update(acceleration,steering,breaking)
            self.gameDisplay.fill(config.white)
            self.cars.draw(self.gameDisplay)
            pygame.display.update()
            self.clock.tick(config.fps)

        pygame.quit()

class Car(pygame.sprite.Sprite):
    def __init__(self, x, y, angle=0.0):
        super().__init__()
        self.image = pygame.image.load(config.car_sprite_location)
        self.orig_image = self.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity = Vector2(0.0, 0.0)
        self.position = Vector2(x,y)
        self.angle = angle

    def update(self,acceleration,steering,breaking):
        #accelerate Car
        self.velocity += (acceleration * config.max_acceleration, 0)
        #if car is faster than max velocity set velocity to max velocity
        self.velocity.x = max(-config.max_velocity, min(self.velocity.x, config.max_velocity))
        #slow car
        isVelocityPositive = self.velocity.x > 0
        negativeAcceleration = breaking * config.max_brake_deceleration
        if(acceleration == 0):
            negativeAcceleration += config.free_deceleration

        if(abs(self.velocity.x) - negativeAcceleration) < 0.0:
            self.velocity.x = 0
        elif isVelocityPositive:
            self.velocity.x -= negativeAcceleration
        elif not isVelocityPositive:
            self.velocity.x += negativeAcceleration




        if steering != 0:
            turning_radius = config.car_length / tan(radians(steering*config.max_steering))
            angular_velocity = self.velocity.x / turning_radius
        else:
            angular_velocity = 0
        self.angle += degrees(angular_velocity)
        self.position += self.velocity.rotate(-self.angle)
        self.rect.y = self.position[0] - self.rect.height/2
        self.rect.x = self.position[1] - self.rect.width/2
        self.image = pygame.transform.rotozoom(self.orig_image, -self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)
        #self.image = pygame.transform.rotate(self.image, self.angle)


class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, image, friction=1.0, angle=0.0):
        super().__init__()
        self.image = pygame.image.load(image)
        self.angle = angle
        self.friction = friction
        self.rect = self.image.get_rect()


class Map:
    def __init__(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y

        grass_tile = Tile(config.tile_size, config.tile_size, config.grass_sprite_location)

        self.map_matrix = [[grass_tile for x in range(size_x)] for y in range(size_y)]

    def friction_at(self, x, y):
        return self.map_matrix[x][y].friction



if __name__ == "__main__":
    game = Game()
    game.run()
