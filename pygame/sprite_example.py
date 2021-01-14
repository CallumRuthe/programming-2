# sprite_example.py
# Introduction to sprites

# Goals:
#   * introduce the sprite class
#   * subclass the sprite class

import pygame
import random

# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
WIDTH = 1024
HEIGHT = 768
TITLE = "Sprite Example"
NUM_BLOCKS = 75
NUM_ENEMIES = 10


class Block(pygame.sprite.Sprite):
    def __init__(self):
        # call the superclass constructor
        super().__init__()

        # Image
        self.image = pygame.Surface((35, 20))
        self.image.fill((0, 255, 0))

        # Rect (x, y, width, height)
        self.rect = self.image.get_rect()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # image
        self.image = pygame.image.load("./images/link.png")

        # rect
        self.rect = self.image.get_rect()

    def update(self):
        """Move the player with the mouse"""
        # pygame.mouse.get_pos() -> (x, y)
        self.rect.center = pygame.mouse.get_pos()


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.enemy = pygame.draw.circle(self.image, (255, 0, 0), (self.image.get_width()/2, self.image.get_height()/2), 10)
        self.rect = self.image.get_rect()
        self.x_vel = random.randrange(-10, 11)
        self.y_vel = random.randrange(-10, 11)

    def update(self):
        """updates the x- and y- location of the block
        based on ts x_vel and y_vel

        Returns: NONE
        """
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel

        if self.rect.x < 0 or self.rect.x + self.rect.width > WIDTH:
            self.x_vel *= -1

        if self.rect.y < 0 or self.rect.y + self.rect.height > HEIGHT:
            self.y_vel *= -1


def main():
    pygame.init()

    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)

    # ----- LOCAL VARIABLES
    done = False
    clock = pygame.time.Clock()
    score = 0

    # Create a group of sprites for all sprites
    all_sprites = pygame.sprite.Group()
    block_sprites = pygame.sprite.Group()
    enemy_sprites = pygame.sprite.Group()

    # make lots of blocks on the screen
    for i in range(NUM_BLOCKS):
        block = Block()
        block.rect.x = random.randrange(WIDTH-block.rect.width)
        block.rect.y = random.randrange(HEIGHT-block.rect.height)
        all_sprites.add(block)
        block_sprites.add(block)

    player = Player()
    all_sprites.add(player)

    for i in range(NUM_ENEMIES):
        enemy = Enemy()
        enemy.rect.x = random.randrange(WIDTH-enemy.rect.width)
        enemy.rect.y = random.randrange(HEIGHT-enemy.rect.height)
        all_sprites.add(enemy)
        enemy_sprites.add(enemy)

    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----- LOGIC
        all_sprites.update()

        # sprite group that has the sprites collided with
        blocks_hit_list = pygame.sprite.spritecollide(player, block_sprites, True)

        for block in blocks_hit_list:
            score += 1
            print(score)

        enemy_hit = pygame.sprite.spritecollide(player, enemy_sprites, False)

        # create a win and lose scenario
        # lose
        if len(enemy_hit) >= 1:
            player.kill()
            print("You lose :(")
            done = True
        # win
        elif score == 75:
            print("You win!!!")
            done = True

        # ----- DRAW
        screen.fill(BLACK)
        all_sprites.draw(screen)

        # ----- UPDATE
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
