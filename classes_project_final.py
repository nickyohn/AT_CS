import pygame

# initialize code
pygame.init()

# set drawing screen
size = (500,440)
screen = pygame.display.set_mode(size)

# pygame clock to handle fps
clock = pygame.time.Clock()

# classes
class Upper_Bus:

    # constructor       
    def __init__(self, x, y, width, height, color_1, color_2, color_3):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3

    def show(self):   
        pygame.draw.rect(screen, (self.color_1, self.color_2, self.color_3), pygame.Rect(self.x, self.y, self.width, self.height))

    def draw_wheels(self):  
        gap = self.width*0.25   # distance between wheel and bumpers
            
        global radius
        radius = 20  # wheel radius

        # draw wheels
        pygame.draw.circle(screen,'black',(self.x + gap, self.height + self.y), radius)
        pygame.draw.circle(screen,'grey',(self.x + gap, self.height + self.y), radius/2)  
        pygame.draw.circle(screen,'black',(self.x + gap, self.height + self.y), radius)
        pygame.draw.circle(screen,'grey',(self.x + gap, self.height + self.y), radius/2)

    # draw windows on the bus
    def draw_windows(self, num_window):
        self.num_window = num_window

        size = 1   # window size

        window_color = (212,246,255)   # window color
        
        for window in range(1, num_window + 1):
            x = self.x + ((window/(num_window + 1)) * self.width) - (0.5*20*size)
            pygame.draw.rect(screen, window_color, pygame.Rect(x, self.y+12, 20*size, 20*size))

    def move(self):
        self.x += 5     # move to the right


# composite class
class Lower_Bus:

    def __init__(self, x, y, width, height, color_1, color_2, color_3):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3  
        
        # create object of component class
        self.bus = Upper_Bus(x, y, width, height, color_1, color_2, color_3)

    def show(self):
        self.bus.show()

    def draw_wheels(self):
        self.bus.draw_wheels()

    def draw_windows(self):
        self.bus.draw_windows(2)

    def move(self):
        self.bus.x -= 2.5   # move to the left


class Road:

    def __init__(self):
        pass

    def show(self):
        y = 275    
        height = size[1] - y 
        # draw road
        pygame.draw.rect(screen, (100,100,100), pygame.Rect(0,y,500,height))   
        pygame.draw.rect(screen, 'yellow', pygame.Rect(0,y + height/2,500,10))     


class Cloud:
   
    def __init__(self, x, y, size):  
        self.x = x
        self.y = y
        self.size = size

    def show(self):   
        # draw cloud(s)
        pygame.draw.circle(screen, 'white', (self.x, self.y), int(self.size*.5))  
        pygame.draw.circle(screen, 'white', (int(self.x+self.size*.5), self.y), int(self.size*.6))
        pygame.draw.circle(screen, 'white', (self.x+self.size, int(self.y-self.size*.1)), int(self.size*.4))

    def move(self):
        self.x -= 2     # move to the left
        
    def shrink(self):
        self.size -= 0.5    # shrink size


# instances
bus_1 = Upper_Bus(60,250,150,70,218,112,214)
bus_2 = Upper_Bus(300,250,150,70,0,204,0)
bus_3 = Lower_Bus(-40,340,150,70,255,0,0)
bus_4 = Lower_Bus(200,340,150,70,255,128,0)
bus_5 = Upper_Bus(-180,250,150,70,0,0,255)

road = Road()

cloud_1 = Cloud(350,85,85)
cloud_2 = Cloud(185,120,70)
cloud_3 = Cloud(70,60,60)


# run pygame
running = True
while running:
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False

    screen.fill((175,238,238))  # set blue skies background

    # show objects
    road.show()

    bus_1.show()
    bus_1.draw_wheels()   
    bus_1.draw_windows(4)
    bus_1.move()
      
    bus_2.show()
    bus_2.draw_wheels()
    bus_2.draw_windows(3)
    bus_2.move()

    bus_3.show()
    bus_3.draw_wheels()
    bus_3.draw_windows()
    bus_3.move()

    bus_4.show()
    bus_4.draw_wheels()
    bus_4.draw_windows()
    bus_4.move()

    bus_5.show()
    bus_5.draw_wheels()
    bus_5.draw_windows(5)
    bus_5.move()

    cloud_1.show()
    cloud_1.move() 
    cloud_1.shrink()

    cloud_2.show()
    cloud_2.move()
    cloud_2.shrink()
        
    cloud_3.show()
    cloud_3.move()
    cloud_3.shrink()
        
    # flip the display
    pygame.display.flip()

    # set clock
    clock.tick(40)

    
# done! time to quit
pygame.quit()
