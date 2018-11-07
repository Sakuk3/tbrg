import pygame
import time
import config
from car import Car
from gui import GUI
class Game:
    def __init__(self):
        pygame.init()
        self.gameDisplay = pygame.display.set_mode((config.display_width,config.display_height))
        pygame.display.set_caption(config.title)
        self.gameDisplay.fill(config.white)
        self.clock = pygame.time.Clock()

        self.map = Map(100,50)
        self.gui = GUI()

        self.cars = pygame.sprite.Group()
        self.player_car = Car(self.map.size_y/2*config.tile_size,self.map.size_x/2*config.tile_size)
        self.cars.add(self.player_car)
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
                        self.gui.acceleration += 1
                    elif event.key == pygame.K_s:
                        self.gui.acceleration -= 1
                    elif event.key == pygame.K_a:
                        self.gui.steering -= 1
                    elif event.key == pygame.K_d:
                        self.gui.steering += 1
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()
                    elif event.key == pygame.K_w:
                        self.gui.acceleration -= 1
                    elif event.key == pygame.K_s:
                        self.gui.acceleration += 1
                    elif event.key == pygame.K_a:
                        self.gui.steering += 1
                    elif event.key == pygame.K_d:
                        self.gui.steering -= 1

            self.cars.update(self.gui.acceleration,self.gui.steering,self.gui.breaking)
            self.gameDisplay.fill(config.white)
            self.map.draw(self.gameDisplay,self.player_car.position)
            self.cars.draw(self.gameDisplay)
            self.gui.draw(self.gameDisplay)
            pygame.display.update()

            self.clock.tick(config.fps)

        pygame.quit()



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

    def draw(self,screen,player_position):
        for x in range(0,self.size_x):
            for y in range(0,self.size_y):
                screen.blit(self.map_matrix[y][x].image,(x*config.tile_size,y*config.tile_size))
        """
        Draw Grid        
        for x in range(0,config.display_width,config.tile_size):
            pygame.draw.line(screen,config.black,(x,0),(x,config.display_height))

        for y in range(0,config.display_height,config.tile_size):
            pygame.draw.line(screen,config.black,(0,y),(config.display_width,y))
        """
if __name__ == "__main__":
    game = Game()
    game.run()
