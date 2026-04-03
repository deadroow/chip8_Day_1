import pygame
pygame.init()
ecran=pygame.display.set_mode((640,320))
marche=True
touche={
    pygame.K_1: 0x1, pygame.K_2: 0x2, pygame.K_3: 0x3, pygame.K_4: 0xC,
    pygame.K_a: 0x4, pygame.K_z: 0x5, pygame.K_e: 0x6, pygame.K_r: 0xD,
    pygame.K_q: 0x7, pygame.K_s: 0x8, pygame.K_d: 0x9, pygame.K_f: 0xE,
    pygame.K_w: 0xA, pygame.K_x: 0x0, pygame.K_c: 0xB, pygame.K_v: 0xF
}
etat_touche=[False]*16


play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
            
        # Appui sur une touche
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: 
                play = False
                
            if event.key in touche:
                index = touche.get(event.key)
                etat_touche[index] = True
                print(f"Touche HEX {hex(index)} pressée")

        # Relâchement d'une touche
        if event.type == pygame.KEYUP:
            if event.key in touche:
                index = touche.get(event.key)
                etat_touche[index] = False
                print(f"Touche HEX {hex(index)} relâchée")

pygame.quit()









