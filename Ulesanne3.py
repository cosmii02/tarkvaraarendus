import pygame #impordib pygame mooduli
pygame.init() #alustab pygame mooduli

screen = pygame.display.set_mode((640, 480)) # määrab ekraani suuruse
pygame.display.set_caption("Ülesanne 3") # määrab akna nime
# Make background green
background = pygame.Surface(screen.get_size())
background.fill((152, 255, 159))
background = background.convert()
screen.blit(background, (0, 0))
ruutu_suurus = str(input("Sisesta ruudu suurus: ")) # Ask user for integer value for ruutsuurus
if ruutu_suurus == '': # If user didn't enter anything
    ruutu_suurus=20
# convert ruutu_suurus to integer
ruutu_suurus = int(ruutu_suurus)
red = str(input("Sisesta punase kogus 0-255: ")) # Ask user for integer value for red
# if red == '' make red 255
if red == '':
    red = 255
# convert red to integer
red = int(red)
green = str(input("Sisesta rohelise kogus 0-255: ")) # Ask user for integer value for green
# if green == '' make green 255
if green == '':
    green = 0
# convert green to integer
green = int(green)
blue = str(input("Sisesta sinise kogus 0-255: ")) # Ask user for integer value for blue
# if blue == '' make blue 255
if blue == '':
    blue = 0
# convert blue to integer
blue = int(blue)
# Draw square grid
for x in range(0, 640, ruutu_suurus):
    pygame.draw.line(screen, (red, green, blue), (x, 0), (x, 480))
for y in range(0, 480, ruutu_suurus):
    pygame.draw.line(screen, (red, green, blue), (0, y), (640, y))

pygame.display.flip() #värskendab ekraani

# Make pygame not exit automatically
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()