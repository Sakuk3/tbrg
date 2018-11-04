import pygame
import time
import config
def main():
    pygame.init()
    gameDisplay = pygame.display.set_mode((config.display_width,config.display_height))
    pygame.display.set_caption('TBRG')
    clock = pygame.time.Clock()
    while True:
        x = pygame.event.get()
        for event in x:
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
    pygame.quit()

if __name__ == "__main__":
    main()
