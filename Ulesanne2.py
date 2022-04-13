import pygame #impordib pygame mooduli
pygame.init() #alustab pygame mooduli

screen = pygame.display.set_mode((640, 480)) # määrab ekraani suuruse
pygame.display.set_caption("Ülesanne 2") # määrab akna nime
bg = pygame.image.load("img.png")
char = pygame.image.load("img_1.png")
char = pygame.transform.scale(char, (253, 304))
textb = pygame.image.load("img_2.png")
# Make img3 16% smaller
textb = pygame.transform.scale(textb, (int(textb.get_width() * 0.85), int(textb.get_height() * 0.85)))
screen.blit(bg, (0, 0)) # Lisab ekraani keskele pildi
screen.blit(char, (104, 159)) # Lisab ekraanile karakteri pildi
screen.blit(textb, (245, 66))
font = pygame.font.SysFont("Arial", 20)
text = font.render("Tere, olen nimi", True, (255, 255, 255))
screen.blit(text, (280, 140))


pygame.display.flip() #värskendab ekraani

# Make pygame not exit automatically
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()