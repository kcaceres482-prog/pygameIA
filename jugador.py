import pygame

ANCHO, ALTO = 800, 600


class Jugador(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        # 1. Cargar la imagen
        imagen_cargada = pygame.image.load("nave_real.png").convert()

        # 2. HACERLA MÁS GRANDE (la nave)
        self.image = pygame.transform.scale(imagen_cargada, (80, 85))

        
        self.image.set_colorkey(self.image.get_at((0, 0)))

        self.rect = self.image.get_rect()
        self.rect.centerx = ANCHO // 2
        self.rect.bottom = ALTO - 20
        self.velocidad = 8

    def update(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            self.rect.x -= self.velocidad
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            self.rect.x += self.velocidad

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > ANCHO:
            self.rect.right = ANCHO