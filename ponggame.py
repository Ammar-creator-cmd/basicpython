


import pygame
import random

#initialize pygame
pygame.init()

width, height = 800, 600
fps = 60

#colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

#paddle dimensions
padddle_width, paddle_height = 20, 100

#ball properties

ball_size = 20
ball_speed_x = 7
ball_speed_y = 7

#score font
font = pygame.font.Font(None, 88)
message_font = pygame.font.Font(None, 68)

#set up display
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong Game")

#game clock
clock = pygame.time.Clock()

#game class
class Paddle:
    def __init__(self, x, y, color):
        self.rect = pygame.Rect(x, y, padddle_width, paddle_height)
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def move(self, dy):
        self.rect.y += dy
        # Keep paddle within screen bounds
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > height:
            self.rect.bottom = height

    def ai_move(self, ball):
        if self.rect.centery < ball.rect.centery:
            self.move(paddle_speed)
        elif self.rect.centery > ball.rect.centery:
            self.move(-paddle_speed)
        
class ball:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, ball_size, ball_size)
        self.speed_x = random.choice([-ball_speed_x, ball_speed_x])
        self.speed_y = random.choice([-ball_speed_y, ball_speed_y])

    def draw(self, surface):
        pygame.draw.ellipse(surface, white, self.rect)

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Bounce off top and bottom walls
        if self.rect.top <= 0 or self.rect.bottom >= height:
            self.speed_y *= -1

        # Reset if it goes out of bounds
        if self.rect.left <= 0 or self.rect.right >= width:
            self.reset()

    def reset(self, color):
        self.rect = pygame.Rect(width // 2 - ball_size // 2, height // 2 - ball_size // 2, ball_size, ball_size)
        self.color = color
        self.dx =ball_speed_x= random.choice([1, -1])   #randomize direction
        self.dy =ball_speed_y= random.choice([1, -1])