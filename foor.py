import pygame #Impordib pygame mooduli
pygame.init()

screen=pygame.display.set_mode([300,300]) # määrab akna resolutsiooni
pygame.display.set_caption("Foor") # Määrab akna nime

# Teeb tausta mustaks
screen.fill([0, 0, 0])
# Joonistab hallid ääred
pygame.draw.rect(screen, [80, 80, 80], [100, 15, 100, 270], 2)
# Joonistab punase ringi
pygame.draw.circle(screen, [255, 0, 0], [150,64], 40, 100)
# Joonistab kollase ringi
pygame.draw.circle(screen, [255, 255, 0], [150,150], 40, 100)
# Joonistab rohelise ringi
pygame.draw.circle(screen, [0, 255, 0], [150,235], 40, 100)
pygame.display.flip()















running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if running == False:
      pygame.quit()