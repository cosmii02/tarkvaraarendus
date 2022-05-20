import pygame, sys

pygame.init()

# initialize display at 640x480
screen = pygame.display.set_mode((640, 480)) # set screen size
pygame.display.set_caption("Animeerimine") # set window title
clock = pygame.time.Clock() # create clock object

Score = 0 # initialize score

bg = pygame.image.load("bg_rally.jpg") # load background image


f1_blue = pygame.image.load("f1_blue.png") # load car image
f1_blue = pygame.transform.rotate(f1_blue, 180) # rotate car image

f1_red = pygame.image.load("f1_red.png") # load car image
f1_red = pygame.transform.rotate(f1_red, 180) # rotate car image

# speed and position

BspeedY = 30 # initialize car speed
BposX, BposY = 420, 0  # initialize car position
RposX, RposY = 298, 390 # initialize car position
RspeedY = 0 # initialize car speed
gameover = False # initialize gameover flag
while not gameover:
    # fps
    clock.tick(60)
    # mängu sulgemine ristist
    events = pygame.event.get()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            quit()
            sys.exit()

    # pildi lisamine ekraanile
    screen.blit(bg, (0, 0))
    screen.blit(f1_blue, (BposX, BposY))
    BposY += BspeedY

    screen.blit(f1_red, (RposX, RposY))
    RposY += RspeedY

    screen.blit(pygame.font.Font(None, 30).render(f"Score: {Score}", True, [255, 255, 255]), [10, 460])

    if BposY >= 480:
        BposY = -120
        Score += 1

    if RposY >= 480:
        RposY = -120

    pygame.display.flip() # update display

    # make game quit on exit
    for event in events:
        if event.type == pygame.QUIT:
            gameover = True
            pygame.quit()