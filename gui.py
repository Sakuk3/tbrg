import pygame
import config

class GUI:
    def __init__(self):
        self.breaking = 0
        self.acceleration = 0
        self.steering = 0

        # Load Wheel and position it
        self.wheel = pygame.image.load(config.wheel_sprite_location).convert_alpha()
        self.wheel_org = self.wheel
        self.wheel_rect = self.wheel.get_rect()
        self.wheel_rect.x = config.display_width/2-self.wheel_rect.width/2
        self.wheel_rect.y = config.display_height-self.wheel_rect.height/1.5

    def draw(self,screen,clock):

        # Display FPS
        if config.developer_mode:
            font = pygame.font.Font(config.font_type, 15)
            fps =  font.render(str(int(clock.get_fps())), True, config.white)
            screen.blit(fps, (5, 5))

        # draw wheel
        self.wheel = pygame.transform.rotozoom(self.wheel_org, -self.steering*config.max_steering*5,5)
        self.wheel_rect = self.wheel.get_rect(center=self.wheel_rect.center)
        screen.blit(self.wheel,self.wheel_rect)
