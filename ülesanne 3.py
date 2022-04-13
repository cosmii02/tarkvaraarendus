import pygame #impordib pygame mooduli
pygame.init() #alustab pygame mooduli

screen = pygame.display.set_mode((640, 480)) # määrab ekraani suuruse
pygame.display.set_caption("Ülesanne 2") # määrab akna nime
bg = pygame.image.load("img.png")












pygame.display.flip() #värskendab ekraani

# Make pygame not exit automatically
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()