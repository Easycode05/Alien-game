import pygame 

pygame.init()

#Step 2: Create a game window
WIDTH,HEIGHT = 800,600 #Screen dimensions
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("My first Game") #Widow title

x, y = 50, 50
width, height = 100, 50
velocity = 5

#step3: create a game loop
running = True
while running:
    pygame.time.delay(30) #control the game speed
    for event in pygame.event.get(): #look for events
        if event.type == pygame.QUIT: #If user closes the window
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: #Move left
        x -= velocity
    if keys[pygame.K_RIGHT]: #Move right
        x += velocity
    if keys[pygame.K_UP]: #Move up
        x -= velocity
    if keys[pygame.K_DOWN]: #Move down
        x += velocity
        
    #update the display
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE,(x,y,width,height)) #draw the rectangle
    pygame.display.update() 

#Step 4: Quit pygame
pygame.quit()