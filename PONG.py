from random import choice
from turtle import width
import pygame
pygame.init()
playerScore = 0
player2Score = 0
clock = pygame.time.Clock()

font = pygame.font.SysFont('comicsans', 20)
font2 = pygame.font.SysFont('comicsans', 20)
font3 = pygame.font.SysFont('comicsans', 90)
font4 = pygame.font.SysFont('comicsans', 20)


def ballFunction():
    global ballVelx, ballVely, playerScore, player2Score
    ball.x += ballVelx
    ball.y += ballVely
    if ball.top <= 0 or ball.bottom >= winHeight:
        ballVely *= -1
    if ball.left <= -8 or ball.right > winWidth+8:
        if ball.left <= -8:
            playerScore += 1
        if ball.right > winWidth+8:
            player2Score += 1
        pygame.time.delay(2000)
        ballReset()
        playerReset()
    if ball.colliderect(player) or ball.colliderect(player2):
        ballVelx *= -1


def ballReset():
    ball.center = (winWidth/2, 390)
    global ballVelx, ballVely
    ballVely *= choice((1, -1))
    ballVelx *= choice((1, -1))


def playerReset():
    player.center = (winWidth - 20, winHeight/2-70)
    player2.center = (20, winHeight/2-70)


playerVel = 7
winWidth = 1260
winHeight = 780
win = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption('Pong')
run = True
ball = pygame.Rect(winWidth/2 - 15, winHeight/2-15, 30, 30)
player = pygame.Rect(winWidth - 20, winHeight/2-70, 7, 140)
player2 = pygame.Rect(20, winHeight/2-70, 7, 140)
ballVelx = 8.5
ballVely = 8.5
chosi = pygame.font.SysFont('comicsans', 15)
chosit = chosi.render('developed by ARTIN mj', 1, (255,255,255))
# pygame.display.set_icon(pygame.image.load('stuff/pongicon.png'))
while run:
    win.fill((0, 0, 0))
    win.blit(chosit,(10,10))
    text2 = font2.render('Score: '+str(player2Score), True, (255, 255, 255))
    text = font.render('Score: '+str(playerScore), True, (255, 255, 255))
    text3 = font3.render('WINNER', True, (255, 255, 255))
    text4 = font4.render('developed by ARTIN mj', True, (255, 255, 255))
    win.blit(text, (910, 10))
    win.blit(text2, (260, 10))
    pygame.draw.ellipse(win, (255, 255, 255), ball)
    pygame.draw.rect(win, (255, 255, 255), player)
    pygame.draw.rect(win, (255, 255, 255), player2)
    pygame.draw.aaline(win, (90, 90, 90), (winWidth/2, 0),
                       (winWidth/2, winHeight))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    key = pygame.key.get_pressed()
    if key[pygame.K_UP] and player.top >= 0:
        player.y -= playerVel
    if key[pygame.K_DOWN] and player.bottom <= winHeight:
        player.y += playerVel
    if key[pygame.K_F2] and player2.top >= 0:
        player2.y -= playerVel
    if key[pygame.K_2] and player2.bottom <= winHeight:
        player2.y += playerVel
    i = False
    ballFunction()
    clock.tick(70)
    if player2Score==5:
        win.blit(text3, (70, 40))
        win.blit(text4, (70,150))
        i = True
    elif playerScore == 5:
        win.blit(text3,(750,40))
        win.blit(text4, (750,150))

        i = True
    pygame.display.update()
    

    if i:
        ballReset()
        playerReset()
        ballVelx = 0 ; ballVely = 0
        # playerVel = 0

        pygame.time.delay(5000)
        run = False

















