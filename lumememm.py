import pygame #Impordib pygame mooduli
pygame.init()

screen=pygame.display.set_mode([300,300]) # määrab akna resolutsiooni
pygame.display.set_caption("Lumemees") # Määrab akna nime

screen.fill([0, 0, 0])
# Joonistab keskmise ringi
pygame.draw.circle(screen, [255, 255, 255], [150,150], 25, 100)
# Joonistab ülemise ringi
pygame.draw.circle(screen, [255, 255, 255], [150,110], 20, 100)
# Joonistab alumise ringi
pygame.draw.circle(screen, [255, 255, 255], [150,200], 30, 100)
# Joonistab porgandi nina
pygame.draw.polygon(screen, [255, 121, 0], [[147,115],[151,115],[150,120]], 2)
# Joonistab parempoolse silma
pygame.draw.circle(screen, [0, 0, 0], [154,110], 3, 3)
# Joonistab vasakpoolse silma
pygame.draw.circle(screen, [0, 0, 0], [146,110], 3, 3)
pygame.display.flip()













running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if running == False:
      pygame.quit()