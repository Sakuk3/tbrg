import pygame
import time
import config
def main():
    pygame.init()
    gameDisplay = pygame.display.set_mode((config.display_width,config.display_height))
    pygame.display.set_caption('TBRG')
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
        all_sprites_list.update()
        all_sprites_list.draw(gameDisplay)
        pygame.display.update()

    pygame.quit()

class Car(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.image = pygame.image.load("assets/car.png").convert()
        self.rect = self.image.get_rect()
        self.rect.x = pos_x - self.rect.width/2
        self.rect.y = pos_y - self.rect.height/2






if __name__ == "__main__":
    main()
