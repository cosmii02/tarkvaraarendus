import pygame, sys, random

pygame.init()

# initialize display at 640x480
screen = pygame.display.set_mode((640, 480)) # set screen size
pygame.display.set_caption("Animeerimine") # set window title
clock = pygame.time.Clock() # create clock object

Score = 0 # initialize score

bg = pygame.image.load("bg_rally.jpg") # load background image


f1_blue = pygame.image.load("f1_blue.png") # load car image
f1_blue = pygame.transform.rotate(f1_blue, 180) # rotate car image

f2_blue = pygame.image.load("f1_blue.png") # load car image
f2_blue = pygame.transform.rotate(f2_blue, 180) # rotate car image


f1_red = pygame.image.load("f1_red.png") # load car image

# speed and position

BspeedY = 3 # initialize car speed

BposY = random.randint(0, 100)
B2posY = random.randint(0, 100)
RposX, RposY = 298, 390 # initialize car position
RspeedY = 0 # initialize car speed
gameover = False # initialize gameover flag
BposX = random.randint(260, 460)  # initialize car position
B2posX = random.randint(260, 460) # initialize 2nd car position

while not gameover:
    # fps
    clock.tick(120)
    # mängu sulgemine ristist
    events = pygame.event.get()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            quit()
            sys.exit()

    # pildi lisamine ekraanile
    screen.blit(bg, (0, 0))
    screen.blit(f1_blue, (BposX, BposY))
    screen.blit(f2_blue, (B2posX, B2posY))
    BposY += BspeedY
    B2posY += BspeedY+1

    screen.blit(f1_red, (RposX, RposY))
    RposY += RspeedY
    screen.blit(pygame.font.Font(None, 30).render(f"Score: {Score}", True, [255, 255, 255]), [10, 460])

    if BposY >= 480:
        BposY = -120
        Score += 1
        BposX = random.randint(0, 210)

    if B2posY >= 480:
        B2posY = -120
        Score += 1
        B2posX = random.randint(220, 420)

    if RposY >= 480:
        RposY = -120

        # end game if f1_blue or f2_blue hits f1_red
    if B2posY <= RposY + 58 and B2posY >= RposY - 58:
        if B2posX <= RposX + 55 and B2posX >= RposX - 55:
            gameover = True

    if BposY <= RposY + 58 and BposY >= RposY - 58:
        if BposX <= RposX + 55 and BposX >= RposX - 55:
            gameover = True

    pygame.display.flip() # update display

    # make game quit on exit
    for event in events:
        if event.type == pygame.QUIT:
            gameover = True
            pygame.quit()