import pygame #impordib pygame mooduli
pygame.init() #alustab pygame mooduli

screen = pygame.display.set_mode((640, 480)) # määrab ekraani suuruse
pygame.display.set_caption("Ülesanne 2") # määrab akna nime
bg = pygame.image.load("img.png") # Laeb img.png taustaks
char = pygame.image.load("img_1.png") # Määrab muutujale char pildi img_1.png
char = pygame.transform.scale(char, (253, 304)) #muudab pildi suuruse
textb = pygame.image.load("img_2.png") # laeb pildi muutujale
vikklogo = pygame.image.load("VIKK logo2.png") #laeb pildi muutujale
vikklogo = pygame.transform.scale(vikklogo, (int(vikklogo.get_width()*0.75), int(vikklogo.get_height()*0.75)))
cake= pygame.image.load("cake.png") # laeb pildi muutujale
cake = pygame.transform.scale(cake, (int(cake.get_width() * 0.13), int(cake.get_height() * 0.13))) # Teeb pildi 87% väiksemaks
mook = pygame.image.load("mook.png") # laeb pildi muutujale
mook = pygame.transform.scale(mook, (int(mook.get_width() * 0.20), int(mook.get_height() * 0.20))) #Teeb pildi 85% väiksemaks
textb = pygame.transform.scale(textb, (int(textb.get_width() * 0.85), int(textb.get_height() * 0.85))) # Teeb pildi 15% väiksemaks
mook = pygame.transform.rotate(mook, -45) # pöörab mõõga pilti 45 kraadi vasakule
screen.blit(bg, (0, 0)) # Lisab ekraani keskele pildi
screen.blit(char, (104, 159)) # Lisab ekraanile karakteri pildi
screen.blit(textb, (245, 66)) # Lisab musta tekstikasti pildi
screen.blit(vikklogo, (0, 0)) # Lisab ekraanile vikki logo
screen.blit(cake, (460, 190)) # Lisab ekraanile koogi pildi
screen.blit(mook, (460 + cake.get_width() + -70, 100)) # Paneb mõõga koogi kõrvale
font = pygame.font.SysFont("Arial", 20) # Määrab fonti
text = font.render("Tere, olen Kenneth Tuisk", True, (255, 255, 255)) # Teksti kirjutamine eelmääratud fondiga
screen.blit(text, (280, 140)) # Lisab ekraanile muutuja texti


pygame.display.flip() #värskendab ekraani

# Make pygame not exit automatically
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()