#!/usr/bin/env python

import pygame
import sys

# Constants
MAX_FPS = 30
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)


def main():
    # Initialization
    pygame.init()
    size = width, height = 640, 360
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    widget_color = WHITE

    while True:
        mouse_clicked = False

        # Handle global events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Got quit event!")
                quit()
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_clicked = True

        # Get mouse stuff
        mouse_pos = pygame.mouse.get_pos()

        # Clear the screen
        screen.fill(BLACK)

        # Draw buttons
        blue_button_rect = [60, 210, 90, 40]
        red_button_rect = [490, 210, 90, 40]
        white_button_rect = [275, 210, 90, 40]
        pygame.draw.rect(screen, BLUE, blue_button_rect)
        pygame.draw.rect(screen, RED, red_button_rect)
        pygame.draw.rect(screen, WHITE, white_button_rect)

        # Check for clicks on buttons
        if is_clicked(blue_button_rect, mouse_pos, mouse_clicked):
            widget_color = BLUE
        elif is_clicked(red_button_rect, mouse_pos, mouse_clicked):
            widget_color = RED
        elif is_clicked(white_button_rect, mouse_pos, mouse_clicked):
            widget_color = WHITE

        # Draw the widget
        pygame.draw.rect(screen, widget_color, [290, 40, 60, 40])

        # Complete the frame
        pygame.display.update()
        clock.tick(MAX_FPS)


def is_clicked(button_rect, mouse_pos, mouse_clicked):
    # mouse x between rect x pos and x pos + width
    # mouse y between rect y pos and y pos + height

    m_x = mouse_pos[0]
    m_y = mouse_pos[1]

    b_w = button_rect[2]   # button width
    b_h = button_rect[3]   # button height
    b_x1 = button_rect[0]  # button x1
    b_x2 = b_x1 + b_w      # button x2
    b_y1 = button_rect[1]  # button y1
    b_y2 = b_y1 + b_h      # button y2

    in_x_bound = (m_x >= b_x1 and m_x <= b_x2)
    in_y_bound = (m_y >= b_y1 and m_y <= b_y2)

    return (mouse_clicked and in_x_bound and in_y_bound)


def quit(status=0):
    """
    Quits the game
    """
    print("Quitting!")
    pygame.quit()
    sys.exit(status)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        quit()
