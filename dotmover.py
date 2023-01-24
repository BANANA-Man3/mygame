import pygame

# Initialize Pygame
pygame.init()

# Set the screen size and caption
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Game")

# Set the player's starting position
player_x = 400
player_y = 300

# Create a clock to control the frame rate
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the player's input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= 5
    if keys[pygame.K_RIGHT]:
        player_x += 5
    if keys[pygame.K_UP]:
        player_y -= 5
    if keys[pygame.K_DOWN]:
        player_y += 5

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the player
    pygame.draw.circle(screen, (255, 0, 0), (player_x, player_y), 20)

    # Update the screen
    pygame.display.update()

    # Limit the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
