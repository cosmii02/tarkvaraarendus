import pygame #Impordib pygame mooduli
pygame.init() # Initsialiseerib pygame funktsioonid

screen=pygame.display.set_mode([300,300]) # määrab akna resolutsiooni
pygame.display.set_caption("Lumemees") # Määrab akna nime

screen.fill([173,216,230]) # Teeb tausta mustaks
pygame.draw.circle(screen, [255, 255, 255], [150,70], 31, 100) # Joonistab keskmise ringi
pygame.draw.circle(screen, [255, 255, 255], [150,135], 39, 100) # Joonistab ülemise ringi
pygame.draw.circle(screen, [255, 255, 255], [150,220], 52, 100) # Joonistab alumise ringi
pygame.draw.polygon(screen, [255, 121, 0], [[149,90],[144,75],[154,75]], 0) # Joonistab porgandi nina
pygame.draw.circle(screen, [0, 0, 0], [158,65], 4.5, 3) # Joonistab parempoolse silma
pygame.draw.circle(screen, [0, 0, 0], [140,65], 4.5, 3) # Joonistab vasakpoolse silma
pygame.draw.circle(screen, [0, 0, 0], [150,120], 4, 3) # Joonistab ülemise nööbi
pygame.draw.circle(screen, [0, 0, 0], [150,170], 4, 3) # Joonistab keskmine nööbi
pygame.draw.circle(screen, [0, 0, 0], [150,220], 4, 3) # Joonistab alumise nööbi
pygame.draw.line(screen, [128, 128, 128], [182, 115], [218, 95], 3) # Joonistab parema käevarre
pygame.draw.line(screen, [128, 128, 128], [118.5, 115], [82, 95], 3) # Joonistab vasaku käevarre
pygame.draw.line(screen, [128, 128, 128], [82, 95], [82, 105], 3) # Joonistab vasaku käe alumise sõrme
pygame.draw.line(screen, [128, 128, 128], [82, 95], [82, 86], 3) # Joonistab vasaku käe ülemise sõrme
pygame.draw.line(screen, [128, 128, 128], [82, 95], [70, 90], 3) # Joonistab vasaku käe keskmise sõrme
pygame.draw.line(screen, [128, 128, 128], [210,115], [200, 85], 3) # Joonistab parema käe sõrmed
pygame.draw.line(screen, [255, 0, 255], [110,37], [200, 37], 3) # Joonistab mütsi noka
pygame.draw.line(screen, [255, 0, 255], [110,29], [160, 19], 40) # Joonistab mütsi enda
pygame.draw.line(screen, [0, 0, 255], [80, 220], [80, 65], 5) # Joonistab harjavarre
pygame.draw.line(screen, [0, 0, 255], [75, 60], [140, 70], 12) #Joonistab Harja
pygame.draw.circle(screen, [255,255,0], [290,10], 31, 100) # Joonistab päikese
pygame.draw.line(screen, [255, 255, 0], [289, 10], [205, 20], 5) # Joonistab ülemise päikesekiire
pygame.draw.line(screen, [255, 255, 0], [280, 20], [210, 60], 5) # Joonistab keskmise päikesekiire
pygame.draw.line(screen, [255, 255, 0], [281, 39], [229, 110], 5) # Joonistab alumise päikesekiire
pygame.display.flip()





def lumemees():

    run = True
    while run:

        for event in pygame.event.get():   #kontrollib pygame'i sündmusi
            if event.type == pygame.QUIT:  # Sellega sulgeb pygame'i/ saab sulgeda kui vajutada akna ülevalt paremalt X
                run = False
    pygame.quit()

if __name__ == "__main__": # teeb kindlaks, et käivitada ainult lumemees
    lumemees()
