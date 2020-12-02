import pygame

# initialize code
pygame.init()

# set drawing screen
size = (500,500)
screen = pygame.display.set_mode(size)

# define class
class Bus:

    # constructor       
    def __init__(self, x_pos, y_pos, width, height, color_1, color_2, color_3):
            
        # bus attributes
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3

        # pygame drawing    
        pygame.draw.rect(screen, (color_1, color_2, color_3), pygame.Rect(x_pos, y_pos, width, height))

    # draw wheels on the bus  
    def draw_wheels(self):  

        # distance between wheel and bumpers
        gap = self.width*0.25
            
        # wheel radius
        global radius
        radius = 20  

        # draw wheel 1
        pygame.draw.circle(screen,'black',(self.x_pos + gap,self.height + self.y_pos),radius)    
        # draw wheel 2
        pygame.draw.circle(screen,'black',(self.x_pos + self.width - gap, self.height + self.y_pos),radius)

    # draw windows on the bus
    def draw_windows(self, num_window, size):

        # window attributes
        self.num_window = num_window
        self.size = size
        window_color = (212,246,255)

        for window in range(1,num_window+1):
            x_pos = self.x_pos + ((window/(num_window+1))*self.width) - (0.5*20*size)
            pygame.draw.rect(screen, window_color, pygame.Rect(x_pos, self.y_pos + 12, 20*size, 20*size))

# define class
class Road(Bus):

    # inherit some of the bus attributes needed to draw road
    def __init__(self, class_bus):
        
        # inherited attributes
        self.y_pos = class_bus.y_pos
        self.height = class_bus.height

    def draw_road(self):

        # top of the road (y-pos)
        road_top = self.y_pos + self.height + radius
        
        # road height
        road_height = 500 - road_top

        # draw road
        pygame.draw.rect(screen, (100, 100, 100), pygame.Rect(0, road_top, 500, road_height))
        # center line in road
        pygame.draw.rect(screen, 'yellow', pygame.Rect(0, road_top + road_height/2, 500, 10))


running = True

while running:
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    # set white background
    screen.fill((255, 255, 255))
        

    # bus instance 1    
    bus_1 = Bus(60, 225, 150, 70, 255, 0, 0)
    bus_1.draw_wheels()
    bus_1.draw_windows(3,1.5)

    # bus instance 2    
    bus_2 = Bus(300, 225, 150, 70, 0, 255, 0)
    bus_2.draw_wheels()
    bus_2.draw_windows(3,1.5)

    # road instance
    road = Road(bus_1)
    road.draw_road()

    # flip the display
    pygame.display.flip()
    

# done! time to quit
pygame.quit()

