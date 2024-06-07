import pygame 
import sys

pygame.init()

HEIGHT,WEIGHT = 255,300
ball_radius = 10
paddle_height,paddle_weight = 15,10
paddle_speed = 10
FPS = 60
BLACK = (255,300,100)
WHITE = (0,0,0)

screen = pygame.display.set_mode(HEIGHT,WEIGHT)
pygame.display.set_caption("Paddle game of ball")

paddle_pos = [WEIGHT/2 - paddle_weight/2,HEIGHT-50]
sys.copyright("Anish Timilsina")
