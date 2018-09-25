import pygame

class Ball(pygame.sprite.Sprite):
    '''This class defines the sprite for our Ball.'''
    def __init__(self, screen):
        '''This initializer takes a screen surface as a parameter, initializes
        the image and rect attributes, and x,y direction of the ball.'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
 
        # Set the image and rect attributes for the Ball
        self.image = pygame.Surface((10, 10))
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        pygame.draw.circle(self.image, (204, 0, 204), (5, 5), 5, 0)
        self.rect = self.image.get_rect()
        self.rect.center = (screen.get_width()/2,screen.get_height()/2)
 
        # Instance variables to keep track of the screen surface
        # and set the initial x and y vector for the ball.
        self.__screen = screen
        self.__dx = 5
        self.__dy = 5
        
    def stop_ball(self):
        self.rect.center = (240,320)
        self.__dx = 0
        self.__dy = 0
 
    def changex(self):
        '''This method causes the x direction of the ball to reverse.'''
        self.__dx = -(self.__dx)

    def changey(self):
        '''This method causes the x direction of the ball to reverse.'''
        self.__dy = -(self.__dy)
    
    def location(self):
        midtop = self.rect.midtop
        midbottom = self.rect.midbottom
        midleft = self.rect.midleft
        midright = self.rect.midright
        return (midtop,midbottom,midleft,midright)
    def update(self):
        '''This method will be called automatically to reposition the
        ball sprite on the screen.'''
        # Check if we have reached the left or right wall of the screen.
        # If not, then keep moving the ball in the same x direction.
        if ((self.rect.left > 50) and (self.__dx < 0)) or\
           ((self.rect.right < self.__screen.get_width()-50) and (self.__dx > 0)):
            self.rect.left += self.__dx
        # If yes, then reverse the x direction. 
        else:
            self.__dx = -self.__dx
             
        # Check if we have reached the top or bottom of the game.
        # If not, then keep moving the ball in the same y direction.
        if ((self.rect.top > 0) and (self.__dy > 0)) or\
           ((self.rect.bottom < self.__screen.get_height()) and (self.__dy < 0)):
            self.rect.top -= self.__dy
        # If yes, then reverse the y direction. 
        else:
            self.__dy = -self.__dy
            
            
class Player(pygame.sprite.Sprite):
    '''This class defines the sprite for Player model'''
    def __init__(self, screen):
        '''This initializer takes a screen surface as
        parameters.  Depending on the player number it loads the appropriate
        image and positions it on the left or right end of the court'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        self.__screen = screen
        # Define the image attributes for a pink rectangle.
        self.image = pygame.Surface((60, 10))
        self.image = self.image.convert()
        self.image.fill((204, 0, 204))
        self.rect = self.image.get_rect()

        # Position it 50 pixels from screen bottom
        # Center the player horizontally in the window.
        self.rect.center = (screen.get_width()/2, 430)
        
        #State initial directions
        self.__dx = 0
        
        # Keep track of number of lives
        lives = 3        
      
    def go_left(self):
        self.__dx = -5
        
    def go_right(self):
        self.__dx = 5
        
    def rest(self):
        self.__dx = 0
    
    def location(self):
        left = self.rect.left 
        right = self.rect.right
        return (left,right)
         
    def update(self):
        '''This method will be called automatically to reposition the
        player sprite on the screen.'''
        # Check if we have reached the top or bottom of the screen.
        # If not, then keep moving the player in the same y direction.
        if (self.__dx != 0) :
            self.rect.right += self.__dx
        if (self.rect.left < 55) or (self.rect.right > self.__screen.get_width() - 55):
            self.__dx = 0
            if self.__dx == 5:
                self.rect.right -= 5
            elif self.__dx == -5:
                self.rect.right += 5

        # If yes, then we don't change the y position of the player at all.
        

class EndZone(pygame.sprite.Sprite):
    '''This class defines the sprite for our left and right end zones'''
    def __init__(self, screen):
        '''This initializer takes a screen surface, and x position  as
        parameters.  For the left (player 1) endzone, x_position will = 0,
        and for the right (player 2) endzone, x_position will = 639.'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
         
        # Our endzone sprite will be a 1 pixel wide black line.
        #pay attention to how to use this
        self.image = pygame.Surface((screen.get_width(),1))
        self.image = self.image.convert()
        self.image.fill((0, 0, 0))
         
        # Set the rect attributes for the endzone
        self.rect = self.image.get_rect()
        self.rect.left = 0
        self.rect.top = 479
        
class ScoreKeeper(pygame.sprite.Sprite):
    '''This class defines a label sprite to display the score.'''
    def __init__(self):
        '''This initializer loads the system font "Arial", and
        sets the starting score to 0:0'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
 
        # Load our custom font, and initialize the starting score.
        self.__font = pygame.font.SysFont("Blazed.ttf", 50)
        self.__playerscore = 0
        
        # Set up variable to keep track of lives
        self.__lives = 3
        
    def player_points(self, score):
        '''This method adds one to the score for player 1'''
        self.__playerscore += score
    
    def minus_life(self):
        '''This method will deduct lives when the ball hits the end zone'''
        self.__lives -= 1

    def update(self):
        '''This method will be called automatically to display 
        the current score at the top of the game window.'''
        #REVISE THIS PART

        if self.__lives == 0:
            message = "Game over" 
            self.image = self.__font.render(message, 1, (144, 144, 144))
            self.rect = self.image.get_rect()
            self.rect.center = (320, 15)   
        elif self.__playerscore < 378:
            message = "Lives: %d Score: %d"% (self.__lives, self.__playerscore)
            self.image = self.__font.render(message, 1, (144, 144, 144))
            self.rect = self.image.get_rect()
            self.rect.center = (320, 15)
        else:
            message = "You win! Score: %d"% (self.__playerscore)
            self.image = self.__font.render(message, 1, (144, 144, 144))
            self.rect = self.image.get_rect()
            self.rect.center = (320, 15)            

class Bricks(pygame.sprite.Sprite):
    '''This class defines the bricks in the game'''
    def __init__(self,x_coord,y_coord,colour):
        '''This initalizer will determine the location of
        the brick as well as the color'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        # Set the image and rect attributes for the bricks
        self.image = pygame.Surface((30, 15))
        self.image = self.image.convert()
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.left = x_coord
        self.rect.top = y_coord
        
        
class Walls(pygame.sprite.Sprite):
    '''This class defines the grey walls in the game'''
    def __init__(self, screen, x_coord):
        '''This initalizer will determine the location of
        the wall as well as the color'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)        
                 
        # Set the image and rect attributes for the bricks
        self.image = pygame.Surface((50, 375))
        self.image = self.image.convert()
        self.image.fill((144, 144, 144))
        self.rect = self.image.get_rect()
        self.rect.left = x_coord
        self.rect.top = 45
                 
class Ceiling(pygame.sprite.Sprite):
    '''This class defines the grey ceiling in the game'''
    def __init__(self):
        '''This initalizer will determine the location of the 
        ceiling as well as the colour'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)        
                 
        # Set the image and rect attributes for the bricks
        self.image = pygame.Surface((540, 50))
        self.image = self.image.convert()
        self.image.fill((144, 144, 144))
        self.rect = self.image.get_rect()
        self.rect.centerx = 320
        self.rect.centery = 70
        
class Wall_bottom(pygame.sprite.Sprite):
    '''This class defines the coloured bottom sections
    of the wall in the game'''
    def __init__(self,x_coord,colour):
        '''This initalizer will determine the location bottom
        sections of the wall as well as the colour'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)        
                 
        # Set the image and rect attributes for the wall bottoms
        self.image = pygame.Surface((50, 10))
        self.image = self.image.convert()
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.left = x_coord
        self.rect.top = 420
        
        
