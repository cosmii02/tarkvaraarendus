import pygame
pygame.init()

screen=pygame.display.set_mode([300,300])
pygame.display.set_caption("Lumemees")

screen.fill([0, 0, 0])
pygame.draw.circle(screen, [255, 255, 255], [150,70], 31, 100)
pygame.draw.circle(screen, [255, 255, 255], [150,135], 39, 100)
pygame.draw.circle(screen, [255, 255, 255], [150,220], 52, 100)
pygame.draw.polygon(screen, [255, 121, 0], [[149,90],[144,75],[154,75]], 0)
pygame.draw.circle(screen, [0, 0, 0], [158,65], 4.5, 3)
pygame.draw.circle(screen, [0, 0, 0], [140,65], 4.5, 3)
pygame.draw.circle(screen, [0, 0, 0], [150,120], 4, 3)
pygame.draw.circle(screen, [0, 0, 0], [150,170], 4, 3)
pygame.draw.circle(screen, [0, 0, 0], [150,220], 4, 3)
pygame.draw.line(screen, [128, 128, 128], [182, 115], [218, 95], 3)
pygame.draw.line(screen, [128, 128, 128], [118.5, 115], [82, 95], 3)
pygame.draw.line(screen, [128, 128, 128], [82, 95], [82, 105], 3)
pygame.draw.line(screen, [128, 128, 128], [82, 95], [82, 86], 3)
pygame.draw.line(screen, [128, 128, 128], [82, 95], [70, 90], 3)

pygame.display.flip()











running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if running == False:
      pygame.quit()