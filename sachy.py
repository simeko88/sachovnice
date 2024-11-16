import pygame

# Inicializace Pygame
pygame.init()

# Velikost okna a polí
velikost_pole = 80
okno = pygame.display.set_mode((velikost_pole * 8, velikost_pole * 8))  # Okno pro 8x8 polí, každé o velikosti 80x80 px
pygame.display.set_caption("Šachovnice")

# Barvy pro šachovnici
svetla_barva = (222, 184, 135)  # Světlá hnědá
tmava_barva = (139, 69, 19)     # Tmavá hnědá

# Načtení obrázku pěšce
try:
    white_pesec = pygame.image.load("c:/Nová složka/Olda Python pokus/obrazky/white_pesec.png")  # Ujisti se, že obrázek je ve správné cestě
    white_pesec = pygame.transform.scale(white_pesec, (80, 80))  # Změna velikosti obrázku na velikost políčka
except pygame.error as e:
    print(f"Chyba při načítání obrázku: {e}")
    pygame.quit()
    exit()

try:
    white_vez = pygame.image.load("c:/Nová složka/Olda Python pokus/obrazky/white_vez.png")  # Ujisti se, že obrázek je ve správné cestě
    white_vez = pygame.transform.scale(white_vez, (80, 80))  # Změna velikosti obrázku na velikost políčka
except pygame.error as e:
    print(f"Chyba při načítání obrázku: {e}")
    pygame.quit()
    exit()

# Umístění obrázku na A1 a H1
# A1 (0, 0)
x_a1 = 0 * velikost_pole  # x souřadnice pro A1
y_a1 = 0 * velikost_pole  # y souřadnice pro A1
okno.blit(white_vez, (x_a1, y_a1))  # Umístění obrázku na A1

# H1 (7, 0)
x_h1 = 7 * velikost_pole  # x souřadnice pro H1
y_h1 = 0 * velikost_pole  # y souřadnice pro H1
okno.blit(white_vez, (x_h1, y_h1))  # Umístění obrázku na H1


























# Funkce pro vykreslení šachovnice
def vykresli_sachovnici():
    for row in range(8):  # Pro každý řádek
        for col in range(8):  # Pro každý sloupec
            barva = svetla_barva if (row + col) % 2 == 0 else tmava_barva  # Střídání barev
            pygame.draw.rect(okno, barva, (col * velikost_pole, row * velikost_pole, velikost_pole, velikost_pole))  # Vykreslení políčka

# Vykreslení šachovnice
vykresli_sachovnici()

# Vykreslení pěšců na políčka A2 až H2
for col in range(8):  # Pro každý sloupec od A do H
    x = col * velikost_pole  # x souřadnice pro sloupce A až H
    y = 6 * velikost_pole    # y souřadnice pro řádek 2 (A2 až H2)
    okno.blit(white_pesec, (x, y))  # Vykreslení obrázku pěšce na políčko

# Aktualizace okna
pygame.display.flip()

# Čekání, než se zavře
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

pygame.quit()
