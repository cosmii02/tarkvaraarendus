import pygame #Impordib pygame mooduli
pygame.init()

screen=pygame.display.set_mode([300,300]) # määrab akna resolutsiooni
pygame.display.set_caption("Lumemees") # Määrab akna nime



screen.fill([0, 0, 0]) # Teeb tausta mustaks

pygame.draw.circle(screen, [255, 255, 255], [150,70], 31, 100) # Joonistab keskmise ringi
pygame.draw.circle(screen, [255, 255, 255], [150,135], 39, 100) # Joonistab ülemise ringi
pygame.draw.circle(screen, [255, 255, 255], [150,220], 52, 100) # Joonistab alumise ringi
pygame.draw.polygon(screen, [255, 121, 0], [[149,90],[144,75],[154,75]], 0) # Joonistab porgandi nina
pygame.draw.circle(screen, [0, 0, 0], [158,65], 4.5, 3) # Joonistab parempoolse silma
pygame.draw.circle(screen, [0, 0, 0], [140,65], 4.5, 3) # Joonistab vasakpoolse silma
pygame.display.flip()











running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if running == False:
      pygame.quit()