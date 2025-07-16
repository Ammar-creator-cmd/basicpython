import pygame
import random

# Initialize Pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255) 
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Paddle and Ball Properties
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100   
PADDLE_SPEED = 7

BALL_SIZE = 20
BALL_SPEED_X = 7
BALL_SPEED_Y = 7

# Fonts
FONT = pygame.font.Font(None, 80)   
MESSAGE_FONT = pygame.font.Font(None, 60)

# Display setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")
clock = pygame.time.Clock()

# Classes
class Paddle:
    def __init__(self, x, y, color):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def move(self, dy):
        self.rect.y += dy
        self.rect.top = max(self.rect.top, 0)
        self.rect.bottom = min(self.rect.bottom, HEIGHT)

    def ai_move(self, ball):
        if self.rect.centery < ball.rect.centery:
            self.move(PADDLE_SPEED)
        elif self.rect.centery > ball.rect.centery:
            self.move(-PADDLE_SPEED)

class Ball:
    def __init__(self, x, y, color):
        self.rect = pygame.Rect(x, y, BALL_SIZE, BALL_SIZE)
        self.color = color
        self.dx = BALL_SPEED_X * random.choice((1, -1))
        self.dy = BALL_SPEED_Y * random.choice((1, -1))

    def draw(self, surface):
        pygame.draw.ellipse(surface, self.color, self.rect)

    def move(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

    def check_collision_wall(self):
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.dy *= -1

    def check_collision_paddle(self, paddle):
        if self.rect.colliderect(paddle.rect):
            self.dx *= -1
            self.dy += random.uniform(-1, 1) * 0.5
            self.dy = max(-BALL_SPEED_Y * 1.5, min(BALL_SPEED_Y * 1.5, self.dy))

    def reset(self):
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.dx = BALL_SPEED_X * random.choice((1, -1))
        self.dy = BALL_SPEED_Y * random.choice((1, -1))

def reset_game():
    player_paddle = Paddle(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, GREEN)
    ai_paddle = Paddle(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, BLUE)
    ball = Ball(WIDTH // 2, HEIGHT // 2, WHITE)
    return player_paddle, ai_paddle, ball

def show_intro():
    intro = True
    while intro:
        screen.fill(BLACK)
        title = FONT.render("Welcome to Pong!", True, WHITE)
        prompt = MESSAGE_FONT.render("Press SPACE to Begin", True, GREEN)
        screen.blit(title, title.get_rect(center=(WIDTH // 2, HEIGHT // 3)))
        screen.blit(prompt, prompt.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                intro = False

def draw_game_over(winner):
    screen.fill(BLACK)

    for i in range(5):
        pygame.draw.rect(screen, GREEN if winner == "Player" else BLUE,
                         pygame.Rect(random.randint(100, WIDTH - 100), random.randint(100, HEIGHT - 100),
                                     random.randint(10, 30), random.randint(10, 30)))

    for i in range(15):
        pygame.draw.circle(screen, WHITE,
                           (random.randint(100, WIDTH - 100), random.randint(100, HEIGHT - 100)),
                           random.randint(2, 6))

    for _ in range(3):
        x = random.randint(150, WIDTH - 150)
        pygame.draw.lines(screen, (255, 255, 0), False,
                          [(x, HEIGHT//2 - 100), (x+20, HEIGHT//2 - 60), (x-20, HEIGHT//2 - 20), (x+20, HEIGHT//2 + 20)], 3)

    game_over_text = FONT.render("GAME OVER", True, (255, 0, 255))
    winner_text = MESSAGE_FONT.render(f"{winner} Wins!", True, WHITE)
    prompt_text = MESSAGE_FONT.render("Press SPACE to Play Again", True, GREEN)

    screen.blit(game_over_text, game_over_text.get_rect(center=(WIDTH//2, HEIGHT//2 - 60)))
    screen.blit(winner_text, winner_text.get_rect(center=(WIDTH//2, HEIGHT//2)))
    screen.blit(prompt_text, prompt_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 50)))

    pygame.display.flip()
    pygame.time.wait(2000)

# Start screen
show_intro()

# Game setup
player_paddle, ai_paddle, ball = reset_game()
game_active = False
player_score = 0
ai_score = 0
max_score = 5

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_active:
                game_active = True
                player_paddle, ai_paddle, ball = reset_game()
                player_score = 0
                ai_score = 0

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_paddle.move(-PADDLE_SPEED)
    if keys[pygame.K_DOWN]:
        player_paddle.move(PADDLE_SPEED)

    if game_active:
        ball.move()
        ball.check_collision_wall()
        ball.check_collision_paddle(player_paddle)
        ball.check_collision_paddle(ai_paddle)
        ai_paddle.ai_move(ball)

        if ball.rect.left <= 0:
            ai_score += 1
            ball.reset()
            if ai_score >= max_score:
                draw_game_over("AI")
                game_active = False
        elif ball.rect.right >= WIDTH:
            player_score += 1
            ball.reset()
            if player_score >= max_score:
                draw_game_over("Player")
                game_active = False

    screen.fill(BLACK)
    player_paddle.draw(screen)
    ai_paddle.draw(screen)
    ball.draw(screen)

    for i in range(0, HEIGHT, 20):
        pygame.draw.line(screen, WHITE, (WIDTH // 2, i), (WIDTH // 2, i + 10), 1)

    player_text = FONT.render(str(player_score), True, GREEN)
    ai_text = FONT.render(str(ai_score), True, BLUE)
    screen.blit(player_text, (WIDTH // 4, 20))
    screen.blit(ai_text, (WIDTH * 3 // 4 - ai_text.get_width(), 20))

    if not game_active and player_score < max_score and ai_score < max_score:
        message = MESSAGE_FONT.render("Press SPACE to Start", True, WHITE)
        screen.blit(message, message.get_rect(center=(WIDTH // 2, HEIGHT // 2)))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
exit()