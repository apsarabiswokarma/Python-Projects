# Import the necessary modules
import pygame

# Initialize pygame
pygame.init()

# Set the width and height of the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the window
pygame.display.set_caption("Block Game")

# Set the colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Set the block size and position
block_size = 50
block_x = screen_width/2 - block_size/2
block_y = screen_height/2 - block_size/2

# Set the movement speed
movement_speed = 5

# Run the game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # Check for key presses
    keys = pygame.key.get_pressed()
    
    # Move the block up
    if keys[pygame.K_UP]:
        block_y -= movement_speed
        
    # Move the block down
    if keys[pygame.K_DOWN]:
        block_y += movement_speed
        
    # Move the block left
    if keys[pygame.K_LEFT]:
        block_x -= movement_speed
        
    # Move the block right
    if keys[pygame.K_RIGHT]:
        block_x += movement_speed
        
    # Draw the block on the screen
    pygame.draw.rect(screen, white, (block_x, block_y, block_size, block_size))
    
    # Update the display
    pygame.display.update()

# Quit pygame
pygame.quit()
