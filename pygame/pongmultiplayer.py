import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong Champions")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CONFETTI_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]

# Paddle and ball settings
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_RADIUS = 7
ball_speed = [5, 5]

# Game objects
left_paddle = pygame.Rect(30, HEIGHT // 2 - 50, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - 40, HEIGHT // 2 - 50, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_RADIUS * 2, BALL_RADIUS * 2)

# Clock and fonts
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)
title_font = pygame.font.SysFont(None, 64)

# Scores and game state
left_score = 0
right_score = 0
MAX_SCORE = 11
game_started = False
game_over = False
blink_timer = 0
confetti = []

def draw_intro():
    screen.fill(BLACK)
    title = title_font.render("Ping Pong Champions", True, WHITE)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 2 - 80))

    global blink_timer
    blink_timer += 1
    if (blink_timer // 30) % 2 == 0:
        msg = font.render("Press SPACE to Start", True, WHITE)
        screen.blit(msg, (WIDTH // 2 - msg.get_width() // 2, HEIGHT // 2))

    pygame.display.flip()

def draw():
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, left_paddle)
    pygame.draw.rect(screen, WHITE, right_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    left_text = font.render(str(left_score), True, WHITE)
    right_text = font.render(str(right_score), True, WHITE)
    screen.blit(left_text, (WIDTH // 4, 20))
    screen.blit(right_text, (WIDTH * 3 // 4, 20))

    if game_over:
        winner = "Left Player Wins!" if left_score >= MAX_SCORE else "Right Player Wins!"
        win_text = font.render(winner, True, random.choice(CONFETTI_COLORS))
        screen.blit(win_text, (WIDTH // 2 - win_text.get_width() // 2, HEIGHT // 2 - 30))
        restart_text = font.render("Press SPACE to Restart", True, WHITE)
        screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 20))
        for rect in confetti:
            pygame.draw.rect(screen, random.choice(CONFETTI_COLORS), rect)

    pygame.display.flip()

def ball_movement():
    global left_score, right_score
    if not game_started or game_over:
        return

    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed[1] *= -1

    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_speed[0] *= -1

    if ball.left <= 0:
        right_score += 1
        reset_ball()
        check_winner()

    if ball.right >= WIDTH:
        left_score += 1
        reset_ball()
        check_winner()

def reset_ball():
    ball.center = (WIDTH // 2, HEIGHT // 2)
    ball_speed[0] *= -1

def check_winner():
    global game_over, confetti
    if left_score >= MAX_SCORE or right_score >= MAX_SCORE:
        game_over = True
        confetti = [pygame.Rect(random.randint(0, WIDTH), random.randint(0, HEIGHT), 5, 10) for _ in range(100)]

def reset_game():
    global left_score, right_score, game_started, game_over, confetti
    left_score = 0
    right_score = 0
    left_paddle.y = HEIGHT // 2 - PADDLE_HEIGHT // 2
    right_paddle.y = HEIGHT // 2 - PADDLE_HEIGHT // 2
    ball.center = (WIDTH // 2, HEIGHT // 2)
    ball_speed[0] = 5
    ball_speed[1] = 5
    game_started = True
    game_over = False
    confetti = []

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            reset_game()

    keys = pygame.key.get_pressed()
    if game_started and not game_over:
        if keys[pygame.K_w] and left_paddle.top > 0:
            left_paddle.y -= 6
        if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
            left_paddle.y += 6
        if keys[pygame.K_UP] and right_paddle.top > 0:
            right_paddle.y -= 6
        if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
            right_paddle.y += 6

    ball_movement()
    if not game_started:
        draw_intro()
    else:
        draw()
    clock.tick(60)
w