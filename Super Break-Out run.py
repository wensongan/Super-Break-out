#Importing and Initializing
import pygame, mySprites
pygame.init()
screen = pygame.display.set_mode((640,480))


def main():
    '''This function defines the 'mainline logic' for our pyPong game.'''
      
    # DISPLAY
    pygame.display.set_caption("Super Break-Out!")
     
    # ENTITIES
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    lives = -1
    bricks = 108
    ballmidtop = ()
    ballmidbottom = ()
    ballmidleft = ()
    ballmidright = ()
    playerleft = ()
    playerright = ()
    row_total_1 = 0
    row_total_2 = 0
    row_total_3 = 0
    row_total_4 = 0
    row_total_5 = 0
    row_total_6 = 0
    
    pygame.mixer.init()
    pygame.mixer.music.load("01. Rock or Bust.mp3")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)
    boing = pygame.mixer.Sound("boing.wav")
    boing.set_volume(1)  
    
    # Sprites for: ScoreKeeper label, End Zones, Ball, and Players
    score_keeper = mySprites.ScoreKeeper()
    ball = mySprites.Ball(screen)
    player = mySprites.Player(screen)
    endzone = mySprites.EndZone(screen)
    wall_left = mySprites.Walls(screen,0)
    wall_right = mySprites.Walls(screen,screen.get_width() - 50)
    wall_group = pygame.sprite.Group (wall_left, wall_right)
    wall_bottom_left = mySprites.Wall_bottom(0,(144, 25, 72))
    wall_bottom_right = mySprites.Wall_bottom(screen.get_width() - 50,(72, 25, 144))
    wall_bottom_group = pygame.sprite.Group (wall_bottom_left, wall_bottom_right)
    ceiling = mySprites.Ceiling()
    #Create Rows of bricks
    brick_row_1 = []
    for brick in range(50,screen.get_width()-50,30):
        brick_row_1.append(mySprites.Bricks(brick,200,(0, 102, 204)))
        row_total_1 += 1
    brick_group_1 = pygame.sprite.Group (brick_row_1)
    brick_row_2 = []
    for brick in range(50,screen.get_width()-50,30):
        brick_row_2.append(mySprites.Bricks(brick,185,(0, 153, 0)))
        row_total_2 += 1
    brick_group_2 = pygame.sprite.Group (brick_row_2)    
    brick_row_3 = []
    for brick in range(50,screen.get_width()-50,30):
        brick_row_3.append(mySprites.Bricks(brick,170,(255, 128, 0)))
        row_total_3 += 1
    brick_group_3 = pygame.sprite.Group (brick_row_3)    
    brick_row_4 = []
    for brick in range(50,screen.get_width()-50,30):
        brick_row_4.append(mySprites.Bricks(brick,155,(255, 255, 0))) 
        row_total_4 += 1
    brick_group_4 = pygame.sprite.Group (brick_row_4)    
    brick_row_5 = []
    for brick in range(50,screen.get_width()-50,30):
        brick_row_5.append(mySprites.Bricks(brick,140,(255, 0, 0))) 
        row_total_5 += 1
    brick_group_5 = pygame.sprite.Group (brick_row_5)    
    brick_row_6 = []
    for brick in range(50,screen.get_width()-50,30):
        brick_row_6.append(mySprites.Bricks(brick,125,(204, 0, 204)))
        row_total_6 += 1
    brick_group_6 = pygame.sprite.Group (brick_row_6)
    #Fill the 
    allSprites = pygame.sprite.Group(score_keeper, endzone, ball, player, wall_left,  wall_right, wall_bottom_group, wall_bottom_right, ceiling, brick_row_1, brick_row_2, brick_row_3, brick_row_4, brick_row_5, brick_row_6)
      
    # ASSIGN 
    clock = pygame.time.Clock()
    keepGoing = True
 
    # Hide the mouse pointer
    pygame.mouse.set_visible(False)
 
    # LOOP
    while keepGoing:
     
        # TIME
        clock.tick(30)
     
        ballmidtop,ballmidbottom,ballmidleft,ballmidright = ball.location()
        playerleft,playerright = player.location()
        # EVENT HANDLING: Player 1 uses joystick, Player 2 uses arrow keys
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False           
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
            elif event.type == pygame.KEYUP:
                player.rest()

                
        if pygame.sprite.spritecollide(ball, brick_group_1, True):
            if int(str(brick_group_1).lstrip("<Group(").rstrip(" sprites)>")) == (row_total_1 - 1):
                score_keeper.player_points(1)
                row_total_1 -= 1
            elif int(str(brick_group_1).lstrip("<Group(").rstrip(" sprites)>")) == (row_total_1 - 2):
                score_keeper.player_points(2)
                row_total_1 -= 2
            if ballmidtop[1] == 210:
                ball.changey()
                boing.play()
            elif ballmidbottom[1] == 205:
                ball.changey()
                boing.play()
            else:
                ball.changex()
                boing.play()
            bricks -= 1
        if pygame.sprite.spritecollide(ball, brick_group_2, True):
            if int(str(brick_group_2).lstrip("<Group(").rstrip(" sprites)>")) == (row_total_2 - 1):
                score_keeper.player_points(2)
                row_total_2 -= 1
            elif int(str(brick_group_2).lstrip("<Group(").rstrip(" sprites)>")) == (row_total_2 - 2):
                score_keeper.player_points(4)
                row_total_2 -= 2            
            if ballmidtop[1] == 195:
                ball.changey()
                boing.play()
            elif ballmidbottom[1] == 190:
                ball.changey()
                boing.play()
            else:
                ball.changex()
                boing.play()
            bricks -= 1
        if pygame.sprite.spritecollide(ball, brick_group_3, True):
            if int(str(brick_group_3).lstrip("<Group(").rstrip(" sprites)>")) == (row_total_3 - 1):
                score_keeper.player_points(3)
                row_total_3 -= 1
            elif int(str(brick_group_3).lstrip("<Group(").rstrip(" sprites)>")) == (row_total_3 - 2):
                score_keeper.player_points(6)
                row_total_3 -= 2            
            if ballmidtop[1] == 180:
                ball.changey()
                boing.play()
            elif ballmidbottom[1] == 175:
                ball.changey()
                boing.play()
            else:
                ball.changex()
                boing.play()
            bricks -= 1
        if pygame.sprite.spritecollide(ball, brick_group_4, True):
            if int(str(brick_group_4).lstrip("<Group(").rstrip(" sprites)>")) == (row_total_4 - 1):
                score_keeper.player_points(4)
                row_total_4 -= 1
            elif int(str(brick_group_4).lstrip("<Group(").rstrip(" sprites)>")) == (row_total_4 - 2):
                score_keeper.player_points(8)
                row_total_4 -= 2   
            if ballmidtop[1] == 165:
                ball.changey()
                boing.play()
            elif ballmidbottom[1] == 160:
                ball.changey()
                boing.play()
            else:
                ball.changex()
                boing.play()
            bricks -= 1
        if pygame.sprite.spritecollide(ball, brick_group_5, True):
            if int(str(brick_group_5).lstrip("<Group(").rstrip(" sprites)>")) == (row_total_5 - 1):
                score_keeper.player_points(5)
                row_total_5 -= 1
            elif int(str(brick_group_5).lstrip("<Group(").rstrip(" sprites)>")) == (row_total_5 - 2):
                score_keeper.player_points(10)
                row_total_5 -= 2   
            if ballmidtop[1] == 150:
                ball.changey()
                boing.play()
            elif ballmidbottom[1] == 145:
                ball.changey()
                boing.play()
            else:
                ball.changex()
                boing.play()
            bricks -= 1
        if pygame.sprite.spritecollide(ball, brick_group_6, True):
            if int(str(brick_group_6).lstrip("<Group(").rstrip(" sprites)>")) == (row_total_6 - 1):
                score_keeper.player_points(6)
                row_total_6 -= 1
            elif int(str(brick_group_6).lstrip("<Group(").rstrip(" sprites)>")) == (row_total_6 - 2):
                score_keeper.player_points(12)
                row_total_6 -= 2               
            if ballmidtop[1] == 135:
                ball.changey()
                boing.play()
            elif ballmidbottom[1] == 130:
                ball.changey()
                boing.play()
            else:
                ball.changex()
                boing.play()
            bricks -= 1
        if pygame.sprite.spritecollide(ball, wall_group, False):
            ball.changex()
            boing.play()
        if pygame.sprite.spritecollide(ball, wall_bottom_group, False):
            ball.changey()
            boing.play()
        if ball.rect.colliderect(ceiling.rect):
            ball.changey()
            boing.play()
            
        if (ballmidtop[1] > 425 and ballmidtop[1] < 435) or (ballmidbottom > 425 and ballmidbottom < 435):
            
            if ball.rect.colliderect(player.rect) or ballmidright[0] > playerleft:
                if ballmidleft[0] <= playerright:
                    ball.changex()
                    boing.play()
                

                
        if ball.rect.colliderect(player.rect):
            ball.changey()
            boing.play()


            
        if ball.rect.colliderect(endzone.rect):
            lives -= 1
            score_keeper.minus_life()
            ball.changey()
            boing.play()
            if lives == 0:
                ball.stop_ball()            

            
            
            

        # REFRESH SCREEN
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)       
        pygame.display.flip()
         
    # Unhide the mouse pointer
    pygame.mouse.set_visible(True)
 
    # Close the game window
    pygame.quit()     
     
# Call the main function
main()  