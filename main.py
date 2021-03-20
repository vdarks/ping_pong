import pygame, sys, random, itertools


#General setup
pygame.init()
clock = pygame.time.Clock()
game_font = pygame.font.SysFont("Comic Sams ms",100)
plr_scr = 0
opn_scr = 0


#Functions
def ball_animation():
  global ball_speed_x,ball_speed_y,plr_scr,opn_scr
  ball.x += ball_speed_x
  ball.y += ball_speed_y
  if ball.left <= 0:
    ball.center = (screen_width/2,screen_height/2)
    ball_speed_x *= random.choice([-1,1])
    ball_speed_y *= random.choice([-1,1])
    plr_scr += 1
  if ball.right >= screen_width:
    ball.center = (screen_width/2,screen_height/2)
    ball_speed_x *= random.choice([-1,1])
    ball_speed_y *= random.choice([-1,1])
    opn_scr += 1

  if ball.top <= 0 or ball.bottom >= screen_height:
    ball_speed_y *= -1
  if ball.colliderect(player) or ball.colliderect(opponent):
    ball_speed_x *= -1
    

def player_animation():
  global player_speed
  player.y += player_speed
  if player.top <= 0:
    player.top = 0
  if player.bottom >= 640:
    player.bottom = 640

def opponent_animation():
  global opponent_speed
  opponent.y += opponent_speed
  if opponent.top <= 0:
    opponent.top = 0
  if opponent.bottom >= 640:
    opponent.bottom = 640

def score():
  opn_score = game_font.render(str(opn_scr),True,(255,255,255))
  plr_score = game_font.render(str(plr_scr),True,(255,255,255))
  screen.blit(opn_score,(525,5))
  screen.blit(plr_score,(630,5))


#Colors
bg_color = pygame.Color('grey12')
ball_color = (80,155,155)


#Setting up the main window
screen_width = 1200
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong')


#Speeds
ball_speed_x = 9 * random.choice([-1,1])
ball_speed_y = 9 * random.choice([-1,1])
player_speed = 0
opponent_speed = 0


#Objects
ball = pygame.Rect(screen_width/2 - 10,screen_height/2 - 10,30,30)
player = pygame.Rect(screen_width - 15, screen_height/2 - 60,7.5,120)
opponent = pygame.Rect(7.5,screen_height/2 - 60,7.5,120)


#Game loop
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_s:
        player_speed += 7
      if event.key == pygame.K_w:
        player_speed -= 7
      if event.key == pygame.K_k:
        opponent_speed += 7
      if event.key == pygame.K_i:
        opponent_speed -= 7
      if event.key == pygame.K_1:
        ball_speed_x = 9
        ball_speed_y = 9
      if event.key == pygame.K_2:
        ball_speed_x = 14
        ball_speed_y = 14
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_s:
        player_speed -= 7
      if event.key == pygame.K_w:
        player_speed += 7
      if event.key == pygame.K_k:
        opponent_speed -= 7
      if event.key == pygame.K_i:
        opponent_speed += 7
        
  #Changing the ball color
  if ball.x <= 600:
    ball_color = (180,80,80)
  else:
    ball_color = (80,155,155)


  #Visual
  screen.fill(bg_color)
  pygame.draw.ellipse(screen,ball_color,ball)
  pygame.draw.rect(screen,(80,155,155),player)
  pygame.draw.rect(screen,(180,80,80),opponent)
  pygame.draw.aaline(screen,(255,255,255),(600,0),(600,640))
  score()


  #"Physics"
  ball_animation()
  player_animation()
  opponent_animation()


  #Screen refresh
  pygame.display.flip()
  clock.tick(60)
