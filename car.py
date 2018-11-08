import pygame
from pygame.math import Vector2
from math import tan, radians, degrees, copysign
import config

class Car(pygame.sprite.Sprite):
    def __init__(self, x, y, angle=0.0):
        super().__init__()
        self.image = pygame.image.load(config.car_sprite_location).convert_alpha()
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
