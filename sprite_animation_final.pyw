import pygame, sys
from pygame import image


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.attack_animation = False
        self.sprites = [
            image.load("assets/Run__000.png").convert_alpha(),
            image.load("assets/Run__001.png").convert_alpha(),
            image.load("assets/Run__002.png").convert_alpha(),
            image.load("assets/Run__003.png").convert_alpha(),
            image.load("assets/Run__004.png").convert_alpha(),
            image.load("assets/Run__005.png").convert_alpha(),
            image.load("assets/Run__006.png").convert_alpha(),
            image.load("assets/Run__007.png").convert_alpha(),
            image.load("assets/Run__008.png").convert_alpha(),
            image.load("assets/Run__009.png").convert_alpha()]
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.is_animating = False
        self.rect.topleft = [pos_x, pos_y]

    def animate(self):
        self.is_animating = True

    def stop(self):
        self.is_animating = False

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.33
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
            self.image = self.sprites[int(self.current_sprite)]


# Inicializar
pygame.init()
clock = pygame.time.Clock()

# Ventana
screen_width = 600
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite Animation")
background = image.load("background.png").convert()

# Crando los sprites y grupos
player = Player(150, 100)
moving_sprites = pygame.sprite.Group()
moving_sprites.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            player.animate()

        if event.type == pygame.KEYUP:
            player.stop()

    # Dibujando
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    moving_sprites.draw(screen)
    moving_sprites.update()
    pygame.display.flip()
    clock.tick(60)
