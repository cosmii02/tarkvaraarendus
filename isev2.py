import pygame
pygame.init()
#ekraani seaded
screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("Harjutamine")
screen.fill([204, 255, 204])

#lisame teksti
font = pygame.font.Font(None, 30)
text = font.render("Hello PyGame", True, [0,0,0])
screen.blit(text, [200,200])

pygame.display.flip()

# make game not quit
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#
# import pygame
# pygame.init()
# #ekraani seaded
# screen=pygame.display.set_mode([640,480])
# pygame.display.set_caption("Harjutamine")
# screen.fill([204, 255, 204])
#
# #lisame teksti
# font = pygame.font.Font(pygame.font.match_font('arial'), 50)
# text = font.render("Hello PyGame", True, [0,0,0])
#
# #tekstikasti suurus
# text_width = text.get_rect().width
# text_height = text.get_rect().height
#
# screen.blit(text, [320,240])
#
# pygame.display.flip()
#
# import pygame
# pygame.init()
# #ekraani seaded
# screen=pygame.display.set_mode([640,480])
# pygame.display.set_caption("Harjutamine")
# screen.fill([204, 255, 204])
#
#lisame teksti

#
# pygame.display.flip()

# import pygame
# pygame.init()
# #ekraani seaded
# screen=pygame.display.set_mode([640,480])
# pygame.display.set_caption("Harjutamine")
# screen.fill([204, 255, 204])
#
# #Lisame pildid
# bg = pygame.image.load("bg.jpg")
# screen.blit(bg,[0,0])
#
# font = pygame.font.Font(pygame.font.match_font('arial'), 50)
# font.set_underline(True)
# text = font.render("Sina võitsid?", True, [255,255,255])
#
# #tekstikasti suurus
# text_width = text.get_rect().width
# text_height = text.get_rect().height
#
# screen.blit(text, [320-text_width/2,240-text_height/2])
#
# pygame.display.flip()
#
# # make game not exit
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()