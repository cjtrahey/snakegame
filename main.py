import pygame
import time
import random

pygame.init()

# Set up display
width, height = 600, 400
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Snake variables
snake_block = 10
snake_speed = 15

# Snake direction
direction = "RIGHT"

# Initial snake position
snake_list = [(width // 2, height // 2)]
length_of_snake = 1

# Apple position
apple = [(random.randrange(0, width - snake_block, snake_block),
          random.randrange(0, height - snake_block, snake_block))]


# Draw the snake
def draw_snake(snake_block):
    for block in snake_list:
        pygame.draw.rect(display, green, [block[0], block[1], snake_block, snake_block])


# Draw the apple
def draw_apple(apple_block):
    pygame.draw.rect(display, red, [apple_block[0], apple_block[1], snake_block, snake_block])


# Game over message
def game_over():
    font_style = pygame.font.SysFont(None, 50)
    message = font_style.render("Game Over!", True, white)
    display.blit(message, (width // 4, height // 2))
    pygame.display.update()
    time.sleep(2)

# Game loop
game_over_flag = False
clock = pygame.time.Clock()

while not game_over_flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over_flag = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"
            elif event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"

    # Move the snake
    if direction == "LEFT":
        snake_list[0] = (snake_list[0][0] - snake_block, snake_list[0][1])
    elif direction == "RIGHT":
        snake_list[0] = (snake_list[0][0] + snake_block, snake_list[0][1])
    elif direction == "UP":
        snake_list[0] = (snake_list[0][0], snake_list[0][1] - snake_block)
    elif direction == "DOWN":
        snake_list[0] = (snake_list[0][0], snake_list[0][1] + snake_block)

    # Check for collisions with walls
    if (snake_list[0][0] >= width or snake_list[0][0] < 0 or
            snake_list[0][1] >= height or snake_list[0][1] < 0):
        game_over_flag = True

    # Check for collisions with itself
    for block in snake_list[1:]:
        if snake_list[0] == block:
            game_over_flag = True

    # Check if snake eats the apple
    if snake_list[0] == apple[0]:
        apple = [(random.randrange(0, width - snake_block, snake_block),
                  random.randrange(0, height - snake_block, snake_block))]
        length_of_snake += 1
        snake_list.append((0, 0))  # Add a new block to the snake

    # Move the rest of the snake body only if the snake doesn't eat an apple
    for i in range(len(snake_list) - 1, 0, -1):
        snake_list[i] = snake_list[i - 1]

    # Clear the display
    display.fill(black)

    # Draw the snake and apple
    draw_snake(snake_block)
    draw_apple(apple[0])

    pygame.display.update()

    # Set frames per second
    clock.tick(snake_speed)

# Quit the game
pygame.quit()
