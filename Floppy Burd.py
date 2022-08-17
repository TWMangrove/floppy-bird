import pygame
import time
import random


# In order for this program to work the images bird.png, obstacle2.jpg, obstacle1.jpg, and background1.jpg must be in
# the same file as the program
pygame.init()
display_width = 1000  # Establish display parameters
display_height = 700
black = (0, 0, 0)     # Rgb Code for black (is later used to fill background)
white = (255, 255, 255)  # Rgb Code for white (used for score)
display = pygame.display.set_mode((display_width, display_height))   # Set parameters
pygame.display.set_caption('Floppy Burd')  # Set title of window
bird = pygame.image.load('bird.png')  # Call a picture of flappy bird located in the same file
top_obstacle = pygame.image.load('obstacle2.jpg')  # Open a picture of the obstacles located in the same file
bottom_obstacle = pygame.image.load('obstacle1.jpg')
background = pygame.image.load('background1.png')  # Open a picture of the desired background
clock = pygame.time.Clock()   # Established an internal clock that will later be used to determine frames per second

def f_bird(x, y):
    display.blit(bird, (x, y))  # Display the bird at given x and y coordinates
def top_obstacles(top_start_x, top_height):
    display.blit(top_obstacle, (top_start_x, top_height))  # Display the top obstacles at given coordinates
def bottom_obstacles(bottom_start_x, bottom_height):
    display.blit(bottom_obstacle, (bottom_start_x, bottom_height))   # Display the bottom obstacles at given coordinates
def score(points):
    basicfont = pygame.font.SysFont(None, 48)   # Set font style and size
    text = basicfont.render('Score: ' + str(points), True, white)  # Render score with specified points
    display.blit(text, (0, 0))  # Display score on screen
    pygame.display.update()

def game_loop():
    rage_quit = False   # Establish that exiting out of the game is false (and will therefore cancel the loop later)
    jump = 0   # Define all variables
    x = 100
    y = 300
    points = 0
    top_start_x = 1000  # Establish initial positions for the obstacles off-screen and 200 pixels apart
    top_start_x1 = 1250
    top_start_x2 = 1500
    top_start_x3 = 1750
    bottom_start_x = 1000
    bottom_start_x1 = 1250
    bottom_start_x2 = 1500
    bottom_start_x3 = 1750
    top_height = random.randrange(-300, -100)   # Randomize the height of the top obstacle by randomizing the y-
    top_height1 = random.randrange(-300, -100)  # coordinate that the obstacle first renders on. The range of the
    top_height2 = random.randrange(-300, -100)  # coordinates is negative because the entire obstacle is not on the
    top_height3 = random.randrange(-300, -100)  # screen.
    bottom_height = top_height + 600       # The height of the bottom obstacle will be determined by the randomized
    bottom_height1 = top_height1 + 600     # y-coordinate of its corresponding top obstacle. The y-coordinate of the
    bottom_height2 = top_height2 + 600     # bottom obstacle will always be 600 pixels from that of the top obstacle,
    bottom_height3 = top_height3 + 600     # allowing enough space for the bird to jump through.

    while not rage_quit:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:  # Allow user to quit
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:   # If the up arrow is pressed down, then birds height will increase by 20
                    jump = -20
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:  # If up key in unpressed or if nothing is pressed, then the height  of the
                    jump = 7                  # bird will decrease by 7 pixels

        y += jump   # Add change in height to y position of bird

        display.fill(black)   # Fill background with black
        display.blit(background, (-10, -10))

        top_obstacles(top_start_x, top_height)   # Display the obstacles
        top_obstacles(top_start_x1, top_height1)
        top_obstacles(top_start_x2, top_height2)
        top_obstacles(top_start_x3, top_height3)
        bottom_obstacles(bottom_start_x, bottom_height)
        bottom_obstacles(bottom_start_x1, bottom_height1)
        bottom_obstacles(bottom_start_x2, bottom_height2)
        bottom_obstacles(bottom_start_x3, bottom_height3)

        f_bird(x, y)          # Display the bird

        top_start_x -= 8   # Have the obstacles move towards the bird at a speed of 8 pixels per loop
        bottom_start_x -= 8
        top_start_x1 -= 8
        bottom_start_x1 -= 8
        top_start_x2 -= 8
        bottom_start_x2 -= 8
        top_start_x3 -= 8
        bottom_start_x3 -= 8

        if y > 610 or y < -50:
            time.sleep(2)  # If the bird reaches a border, then stop the game and restart the game loop
            game_loop()

        if top_start_x < -75 and bottom_start_x < -75:   # Once the obstacles go off screen, a point is added and the
            top_start_x = 1000                           # top and bottom obstacles are randomized and placed on the
            bottom_start_x = 1000                        # other side of the screen
            top_height = random.randrange(-300, -100)
            bottom_height = top_height + 600
            points += 1
        if top_start_x1 < -75 and bottom_start_x1 < -75:
            top_start_x1 = 1000
            bottom_start_x1 = 1000
            top_height1 = random.randrange(-300, -100)
            bottom_height1 = top_height1 + 600
            points += 1
        if top_start_x2 < -75 and bottom_start_x2 < -75:
            top_start_x2 = 1000
            bottom_start_x2 = 1000
            top_height2 = random.randrange(-300, -100)
            bottom_height2 = top_height2 + 600
            points += 1
        if top_start_x3 < -75 and bottom_start_x3 < -75:
            top_start_x3 = 1000
            bottom_start_x3 = 1000
            top_height3 = random.randrange(-300, -100)
            bottom_height3 = top_height3 + 600
            points += 1

        if top_start_x < x + 50 < top_start_x + 25 or top_start_x < x - 25 < top_start_x + 50:
            if not bottom_height - 245 < y + 20 < bottom_height - 75 or not bottom_height - 255 < y - 12.5 < bottom_height - 100:
                time.sleep(2)  # Pause game if a collision is detected so that player can see the fault
                game_loop()  # Start the game from the beginning
        if top_start_x1 < x + 50 < top_start_x1 + 25 or top_start_x1 < x - 25 < top_start_x1 + 50:
            if not bottom_height1 - 245 < y + 20 < bottom_height1 - 75 or not bottom_height1 - 255 < y - 12.5 < bottom_height1 - 100:
                time.sleep(2)
                game_loop()
        if top_start_x2 < x + 50 < top_start_x2 + 25 or top_start_x2 < x - 25 < top_start_x2 + 50:
            if not bottom_height2 - 245 < y + 20 < bottom_height2 - 75 or not bottom_height2 - 255 < y - 12.5 < bottom_height2 - 100:
                time.sleep(2)
                game_loop()
        if top_start_x3 < x + 50 < top_start_x3 + 25 or top_start_x3 < x - 25 < top_start_x3 + 50:
            if not bottom_height3 - 245 < y + 20 < bottom_height3 - 75 or not bottom_height3 - 255 < y - 12.5 < bottom_height3 - 100:
                time.sleep(2)
                game_loop()
        # The code block above checks for a collision between the bird and the obstacles. The parameters used aren't
        # completely accurate and were found through a trial-and-error process, however, the results are close enough to
        # the desired outcome that the inaccuracy doesn't prominently affect the game play.
        score(points)   # Display the scored points
        pygame.display.update()  # Update screen
        clock.tick(42)  # Set the frames per second

game_loop()
pygame.quit()
quit()