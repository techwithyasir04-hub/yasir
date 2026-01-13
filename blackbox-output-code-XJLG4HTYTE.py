import pygame
import random

# Initialize Pygame
pygame.init()

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Free Car Racing Game")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Car settings
car_width = 50
car_height = 100
car_x = SCREEN_WIDTH // 2 - car_width // 2
car_y = SCREEN_HEIGHT - car_height - 10
car_speed = 5

# Obstacle settings
obstacle_width = 50
obstacle_height = 50
obstacle_speed = 3
obstacles = []

# Finish line
finish_line_y = 50
score = 0
font = pygame.font.SysFont(None, 36)

# Clock for FPS
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    screen.fill(BLACK)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Car movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < SCREEN_WIDTH - car_width:
        car_x += car_speed
    
    # Generate obstacles
    if random.randint(1, 100) < 5:
        obstacles.append([random.randint(0, SCREEN_WIDTH - obstacle_width), -obstacle_height])
    
    # Move obstacles and check collisions
    for obs in obstacles:
        obs[1] += obstacle_speed
        pygame.draw.rect(screen, RED, (obs[0], obs[1], obstacle_width, obstacle_height))
        # Simple collision detection
        if (car_x < obs[0] + obstacle_width and car_x + car_width > obs[0] and
            car_y < obs[1] + obstacle_height and car_y + car_height > obs[1]):
            score -= 1  # Penalty for hitting obstacle
    
    # Remove off-screen obstacles
    obstacles = [obs for obs in obstacles if obs[1] < SCREEN_HEIGHT]
    
    # Check finish line
    if car_y <= finish_line_y:
        score += 10  # Reward for reaching finish
        car_y = SCREEN_HEIGHT - car_height - 10  # Reset car position
    
    # Draw finish line
    pygame.draw.line(screen, GREEN, (0, finish_line_y), (SCREEN_WIDTH, finish_line_y), 5)
    
    # Draw car
    pygame.draw.rect(screen, WHITE, (car_x, car_y, car_width, car_height))
    
    # Display score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    
    # Update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()