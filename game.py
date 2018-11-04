import pygame
from pygame.math import Vector2
from math import tan, radians, degrees, copysign
import numpy
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
        #self.cars.add(Car(config.display_width/2,config.display_height/2))
        self.car = Car(config.display_width/2,config.display_height/2)
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            for keypress in pygame.key.get_pressed():
                if keypress == pygame.K_q:
                    pygame.quit()
                    quit()

                elif keypress == pygame.K_UP:
                    if self.car.velocity.x < 0:
                        self.car.acceleration = self.car.brake_deceleration
                    else:
                        self.car.acceleration += 1
                elif keypress == pygame.K_DOWN:
                    if self.car.velocity.x > 0:
                        self.car.acceleration = -self.car.brake_deceleration
                    else:
                        self.car.acceleration -= 1
                elif keypress == pygame.K_SPACE:
                    if abs(self.car.velocity.x) > self.car.brake_deceleration:
                        self.car.acceleration = -copysign(self.car.brake_deceleration, self.car.velocity.x)
                    else:
                        self.car.acceleration = -self.car.velocity.x
                else:
                    if abs(self.car.velocity.x) > config.free_deceleration:
                        self.car.acceleration = -copysign(config.free_deceleration, self.car.velocity.x)
                    else:
                        self.car.acceleration = -self.car.velocity.x
                self.car.acceleration = max(-config.max_acceleration, min(self.car.acceleration, config.max_acceleration))

            if keypress == pygame.K_RIGHT:
                self.car.steering -= 30
            elif keypress == pygame.K_LEFT:
                self.car.steering += 30
            else:
                self.car.steering = 0
            self.car.steering = max(-config.max_steering, min(self.car.steering, config.max_steering))


            self.cars.update()
            self.gameDisplay.fill(config.white)
            self.cars.draw(self.gameDisplay)
            pygame.display.update()
            self.clock.tick(config.fps)

        pygame.quit()

class Car(pygame.sprite.Sprite):
    def __init__(self, x, y, angle=0.0, length=4):
        super().__init__()
        self.position = Vector2(x, y)
        self.velocity = Vector2(0.0, 0.0)
        self.angle = angle
        self.length = length
        self.image = pygame.image.load(config.car_spirte_location)
        self.rect = self.image.get_rect()

        self.acceleration = 0.0
        self.steering = 0.0

    def update(self):
        self.velocity += (self.acceleration, 0)
        self.velocity.x = max(-config.max_velocity, min(self.velocity.x, config.max_velocity))

        if self.steering:
            turning_radius = self.length / tan(radians(self.steering))
            angular_velocity = self.velocity.x / turning_radius
        else:
            angular_velocity = 0

        self.position += self.velocity.rotate(-self.angle)
        self.angle += degrees(angular_velocity)
        self.image = pygame.transform.rotate(self.image, self.car.angle)






if __name__ == "__main__":
    game = Game()
    game.run()
