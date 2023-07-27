#Libaries
import pygame as py
import sys

#Screen Size
screen_width = 1280
screen_height = 720

#paddle center
paddle_width = 20
paddle_height = 120

#Game Setup
py.init()
screen = py.display.set_mode((screen_width, screen_height))
clock = py.time.Clock()
running = True

#Colors
white = (255, 255, 255)
black = (0, 0, 0)

class Paddle:
    COLOR = white
    vel = 10
    
    def __init__(self, x, y , width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
    def draw(self, screen):
        py.draw.rect(screen, self.COLOR, (self.x, self.y, self.width, self.height))
        
    def move(self, up=True):
        if up:
            self.y -= self.vel
        else:
            self.y += self.vel

def draw(screen, paddles):
    screen.fill('Black')
    
    for paddle in paddles:
        paddle.draw(screen)

def handle_paddle_movement(keys, left_paddle, right_paddle):

    #Left paddle
    if keys[py.K_k] and left_paddle.y - left_paddle.vel >= 0:
        left_paddle.move(up=True)
    if keys[py.K_m] and left_paddle.y + left_paddle.vel + left_paddle.height <= screen_height:
        left_paddle.move(up=False)

    #Right paddle
    if keys[py.K_UP] and right_paddle.y - right_paddle.vel >= 0:
        right_paddle.move(up=True)
    if keys[py.K_DOWN] and right_paddle.y + right_paddle.vel + right_paddle.height <= screen_height:
        right_paddle.move(up=False)
    

#Game loop
while running:
    #FPS
    clock.tick(60)
    
    #Player
    left_paddle = Paddle(10, screen_height//2 - paddle_height//2, paddle_width, paddle_height)
    right_paddle = Paddle(screen_width - 10 - paddle_width, screen_height//2 - paddle_height//2, paddle_width, paddle_height)
 
    draw(screen, [left_paddle, right_paddle])

    #Exit loop
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
            
    keys = py.key.get_pressed()
    handle_paddle_movement(keys, left_paddle, right_paddle)
    
    #Display what is being added        
    py.display.update()

py.quit()
sys.exit()