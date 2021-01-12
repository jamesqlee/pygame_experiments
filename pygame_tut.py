import pygame
pygame.init()


# This line creates a window of specified width and height
window_width = 500
window_height = 480
win = pygame.display.set_mode((window_width, window_height))

#Window title
pygame.display.set_caption("Attack of the Rectangles Game - Prepare to get Reck't")

#set background colour
bg_red = 0
bg_green = 255
bg_blue = 0
win.fill((bg_red,bg_green,bg_blue))


clock = pygame.time.Clock()

# set character variables (positions, dimensions, vel = movement speed based on pixels)
x = 250
y = 250
width = 80
height = 60
vel = 20

# set jump variables
isJump = False
jumpIncrement = jumpCountReset = 10

# set character animation
leftfacing = False
rightfacing = False
walkCount = 0

#load graphics for character animation in a list
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]

bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')


#function to update game screen 
def redrawGameWindow():
    # We have 9 images for our walking animation, I want to show the same image for 3 frames
    # so I use the number 27 as an upper bound for walkCount because 27 / 3 = 9. 9 images shown
    # 3 times each animation.
    global walkCount
    
    win.blit(bg, (0,0))  

    if walkCount + 1 >= 27:
        walkCount = 0
        
    if leftfacing:  # If we are facing left
        win.blit(walkLeft[walkCount//3], (x,y))  # We integer divide walkCounr by 3 to ensure each
        walkCount += 1                           # image is shown 3 times every animation
    elif rightfacing:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        win.blit(char, (x, y))  # If the character is standing still
        
    pygame.display.update() 
    


  
#set condition of game loop
run = True

while run:


    
    # OLD This will delay the game the given amount of milliseconds. In our case 0.1 seconds will be the delay
    # pygame.time.delay(100)

    clock.tick(27)
        
    # This will loop through a list of any keyboard or mouse events.
    for event in pygame.event.get():
        
        # Checks if the red button in the corner of the window is clicked
        if event.type == pygame.QUIT:
            
            # Ends the game loop
            run = False

    # Keyboard events
    # The following will give us a dictonary where each key has a value of 1 or 0.
    # where 1 is pressed and 0 is not pressed.
    keys = pygame.key.get_pressed()
    
    # We can check if a key is pressed like this   
    if keys[pygame.K_LEFT] and x > 0:     # Making sure the top left position of our character is greater than 0 on the screen so we never move outside it.
        #shift x position left
        x -= vel
        
    if keys[pygame.K_RIGHT] and x < window_width - width:  # Making sure the top right corner position of our character is less than the screen width 
        #shift x position left
        x += vel
        

   
    if not(isJump): # Checks is user is not jumping
        
        if keys[pygame.K_UP] and y > 0:  # Same principles apply for the y coordinate
            #shift y position left
            y -= vel
            
        if keys[pygame.K_DOWN] and y < window_height - height:
            #shift y position left
            y += vel

        # Set up jump on space bar press
        if keys[pygame.K_SPACE]:
            isJump = True


    #JUMP CODE STARTS
            
    else: # This is what will happen if we are jumping
        #create a curve using a value squared. To stop it going one direction, flip it halfway using a negative value.

        #so, if jump increment is greater than a negative version of its starting value (using jumpcountreset) (i.e will repeat this double the jumpincrement value (second half will be flipped)
        if jumpIncrement >= -1*jumpCountReset:
    
            #Logic: halfway through jump (where jumpIncrement<0) Use flip to flip direction y forcing y from a negative to positive value to create a curve.
            #set flip to make y become a negative value -*+=-
            flip = 1
            if jumpIncrement < 0: #halfway through the jump, flip it
                #set flip to make y become a positive value -*-=+
                flip = -1
                
            #quadratic formula (jump increment squared for exponential growth. Divide this in half to reduce height. Then * by flip to flip direction halfway)
            y -= (jumpIncrement * jumpIncrement) / 2 * flip
            #change increment by 1 for loop
            jumpIncrement -= 1
            
        else: # This will execute if our jump is finished i.e 
            # Resetting our Variables
            jumpIncrement = jumpCountReset
            isJump = False

    #JUMP CODE ENDS            


    #OLD DRAW SCREEN CODE     
    # Fills the screen with background colour (refresh screen)
    #win.fill((bg_red,bg_green,bg_blue))
    #(re)draw character as a rectangle
    #pygame.draw.rect(win, (80,0,80), (x, y, width, height)) #This takes: window/surface, color, rect 

    # This updates the screen so we can see our rectangle
    # pygame.display.update()
    redrawGameWindow()
    
# If we exit the loop this will execute and close our game
pygame.quit()  
    
