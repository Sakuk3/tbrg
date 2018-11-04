import pygame
import numpy
import time
import config
def main():
    pygame.init()
    gameDisplay = pygame.display.set_mode((config.display_width,config.display_height))
    pygame.display.set_caption(config.title)
    gameDisplay.fill(config.white)
    clock = pygame.time.Clock()
    all_sprites_list = pygame.sprite.Group(Car(config.display_width/2,config.display_height/2))
    while True:
        x = pygame.event.get()
        for event in x:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        gameDisplay.fill(config.white)
        all_sprites_list.update(0,0)

        all_sprites_list.draw(gameDisplay)
        pygame.display.update()

    pygame.quit()

class Car(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.image = pygame.image.load("assets/car.png").convert()
        self.image = pygame.transform.rotate(self.image, 10)
        self.rect = self.image.get_rect()
        self.momentum = Momentum([0,0])
        self.rect.x = pos_x - self.rect.width/2
        self.rect.y = pos_y - self.rect.height/2

    def update(self,acceleration_percentage,break_percentage):
        #self.speed.accelerate(config.max_acceleration * acceleration_percentage)
        self.rect.y += 10
        self.rect.x += 10

class Momentum():
    def __init__(self,start_momentum):
        self.speed = Vector2D(start_momentum)
    def accelerate(acceleration):
        self.speed.add(acceleration)

class Vector2D():
    def __init__(self,start_vector):
        self.vector = start_vector
    def add(vector):
        self.vector += vector




if __name__ == "__main__":
    main()
