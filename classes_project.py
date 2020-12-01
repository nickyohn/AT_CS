import pygame

# initialize code
pygame.init()

# set drawing screen
size = (500,500)
screen = pygame.display.set_mode(size)

running = True

while running:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    # set white background
    screen.fill((255, 255, 255))
    
    # define the class
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
      def wheels(self):  
        # distance between wheel and bumpers
        gap = 30
        # wheel radius
        global radius
        radius = 20  
        # draw wheel 1
        pygame.draw.circle(screen, 'black', (self.x_pos + gap, self.y_pos + self.height), radius)    
        # draw wheel 2
        pygame.draw.circle(screen, 'black', (self.x_pos + self.width - gap, self.y_pos + self.height), radius)	


      # draw road that bus drives on 
      def road(self):
      	# top of the road (y-pos)
      	road_top = self.y_pos + self.height + radius
      	# road height
      	height = 500 - road_top
      	# draw road
      	pygame.draw.rect(screen, (100, 100, 100), pygame.Rect(0, road_top, 500, height))
      	# center line in road
      	pygame.draw.rect(screen, 'yellow', pygame.Rect(0, road_top + height/2, 500, 10))


    # instance 1    
    bus_1 = Bus(60, 225, 150, 70, 255, 0, 0)
    bus_1.wheels() 
    bus_1.road() 

    # instance 2    
    bus_2 = Bus(300, 225, 150, 70, 0, 255, 0)
    bus_2.wheels() 
    bus_2.road() 

    # flip the display
    pygame.display.flip()

# done! time to quit
pygame.quit()

