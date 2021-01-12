# rectangle_practice.py
# apply objects/classes

import pygame

# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
WIDTH = 800
HEIGHT = 600
TITLE = "Rectangle Practice"


class Rectangle():
    def __init__(self):
        self.x = 0
        self.y = 0

        self.width = 10
        self.length = 10

        self.colour = (0, 255, 0)


def main():
    pygame.init()

    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)

    # ----- LOCAL VARIABLES
    done = False
    clock = pygame.time.Clock()

    rectangle = Rectangle()
    rectangle.x = 395
    rectangle.y = 295

    # CREATE ANOTHER RECTANGLE
    #   CHANGE ist properties
    #   reminder to sue .notation to change properties
    #   i.e. rectangle_two.x = 100
    blue_rectangle = Rectangle()
    blue_rectangle.x = 325
    blue_rectangle.y = 275
    blue_rectangle.width = 150
    blue_rectangle.length = 50
    blue_rectangle.colour = SKY_BLUE

    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----- LOGIC

        # ----- DRAW
        screen.fill(BLACK)
        pygame.draw.rect(screen, blue_rectangle.colour, (blue_rectangle.x, blue_rectangle.y, blue_rectangle.width, blue_rectangle.length))
        pygame.draw.rect(screen, rectangle.colour, (rectangle.x, rectangle.y, rectangle.width, rectangle.length))
        pygame.draw.circle(screen, (0, 255, 0), (100, 100), 50)

        # ----- UPDATE
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()