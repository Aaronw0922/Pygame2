import pygame
import sys
import random

pygame.init()

size = width, height = 640, 480
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

shapePos = (0, 0)
shapeSize = (50, 30)
shapeRect = pygame.Rect(shapePos, shapeSize)

rectColor = (255, 0, 0)
lineColor = (255, 0, 255)
circleColor = (0, 255, 0)

circlePos = (100, 90)


while True:
  clock.tick(60)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
    if event.type == pygame.MOUSEBUTTONDOWN:
      if event.button == pygame.BUTTON_LEFT:
        shapeRect.center = event.pos
      if event.button == pygame.BUTTON_RIGHT:
        circlePos = event.pos
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        rectColor = (r, g, b)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        lineColor = (r, g, b)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        circleColor = (r, g, b)

  screen.fill((10, 10, 255))
  screen.fill(rectColor, rect = shapeRect)
  pygame.draw.circle(screen, circleColor, circlePos, 25)
  pygame.draw.line(screen, lineColor, circlePos, shapeRect.center, 5)
  pygame.display.flip()
