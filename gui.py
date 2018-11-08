import pygame
import config

class GUI:
    def __init__(self):
        self.breaking = 0
        self.acceleration = 0
        self.steering = 0

    def draw(self,screen,clock):
        font = pygame.font.Font(config.font_type, 15)
        fps =  font.render(str(int(clock.get_fps())), True, config.white)
        screen.blit(fps, (5, 5))
