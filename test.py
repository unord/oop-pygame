#!/usr/bin/env python

import sys
import pygame


MAX_FPS = 30


def main():
    pygame.init()

    size = width, height = 640, 360
    screen = pygame.display.set_mode(size)

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Got quit event.")
                quit()

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 255, 255), [0, 0, 20, 20])

        pygame.display.update()
        clock.tick(MAX_FPS)


def quit(status=0):
    print("Quitting!")
    pygame.quit()
    sys.exit(status)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        quit()
