import pygame

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))

# Create the Snake class


class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = 'up'
        self.body = [(x, y), (x-1, y), (x-2, y)]

    def move(self):
        # Update the snake's position based on its direction
        if self.direction == 'up':
            self.y -= 1
        elif self.direction == 'down':
            self.y += 1
        elif self.direction == 'left':
            self.x -= 1
        elif self.direction == 'right':
            self.x += 1

        # Add a new head to the snake and remove the tail
        self.body.insert(0, (self.x, self.y))
        self.body.pop()

# Create the Food class


class Food:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Set up the game loop
running = True
while running:
    # Handle user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.direction = 'up'
            elif event.key == pygame.K_DOWN:
                snake.direction = 'down'
            elif event.key == pygame.K_LEFT:
                snake.direction = 'left'
            elif event.key == pygame.K_RIGHT:
                snake.direction = 'right'

    # Update the snake's position
    snake.move()

    # Check for collisions
    if snake.x < 0 or snake.x >= window_width or snake.y < 0 or snake.y >= window_height:
        # The snake has run into a wall, end the game
        running = False
    for segment in snake.body[1:]:
        if segment == (snake.x, snake.y):
            # The snake has run into itself, end the game
            running = False
    if snake.x == food.x and snake.y == food.y:
