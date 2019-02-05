import pygame
from roulette import Roulette


pygame.init()


def main():

    size = (700, 700)

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Roulette")

    clock = pygame.time.Clock()

    roulette = Roulette(100, ("Bruno", "Vini", "Kevin", "Freire", "Caio", "Ola"))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
        screen.fill((100, 0, 0))
        roulette.draw(screen, (350, 350))
        #roulette.rotate(10)
        pygame.display.update()
        clock.tick(60)
        
    pygame.quit()

main()
