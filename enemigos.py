import math
import random
import pygame

ANCHO, ALTO = 800, 600


class Meteorito(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        # Tamaño aleatorio para variedad visual
        self.radio = random.randint(20, 45)
        self.diametro = self.radio * 2

        # Generar superficie base del meteorito
        self.image_original = self.crear_meteorito_vectorial(self.radio)
        self.image = self.image_original.copy()
        self.rect = self.image.get_rect()

        # Posición inicial aleatoria fuera de la pantalla
        self.rect.x = random.randint(0, ANCHO - self.rect.width)
        self.rect.y = random.randint(-150, -50)

        # Velocidades y rotación aleatorias
        self.velocidad_y = random.randint(3, 7)
        self.velocidad_x = random.choice([-1, 0, 1])
        self.angulo = 0
        self.velocidad_rotacion = random.randint(-4, 4)
        if self.velocidad_rotacion == 0:
            self.velocidad_rotacion = 2

    def crear_meteorito_vectorial(self, radio):
        """Genera una roca con bordes irregulares, textura y cráteres."""
        superficie = pygame.Surface((radio * 2, radio * 2), pygame.SRCALPHA)

        # 1. Generar puntos irregulares alrededor del centro (forma de asteroide)
        puntos = []
        num_puntos = random.randint(8, 12)
        centro = (radio, radio)

        for i in range(num_puntos):
            angulo = (i / num_puntos) * 2 * math.pi
            variacion = random.uniform(0.7, 1.0)
            distancia = radio * variacion
            x = centro[0] + distancia * math.cos(angulo)
            y = centro[1] + distancia * math.sin(angulo)
            puntos.append((x, y))

        # 2. Dibujar cuerpo principal (Gris/Marrón rocoso)
        color_base = (
            random.randint(100, 130),
            random.randint(80, 100),
            random.randint(70, 90),
        )
        pygame.draw.polygon(superficie, color_base, puntos)

        # 3. Dibujar sombra/borde oscuro
        color_borde = (
            max(0, color_base[0] - 40),
            max(0, color_base[1] - 40),
            max(0, color_base[2] - 40),
        )
        pygame.draw.polygon(superficie, color_borde, puntos, width=2)

        # 4. Agregar cráteres aleatorios
        num_crateres = random.randint(2, 4)
        for _ in range(num_crateres):
            cx = random.randint(int(radio * 0.5), int(radio * 1.5))
            cy = random.randint(int(radio * 0.5), int(radio * 1.5))
            c_radio = random.randint(3, max(4, radio // 5))
            pygame.draw.circle(superficie, color_borde, (cx, cy), c_radio)

        return superficie

    def update(self):
        # Movimiento vertical y lateral
        self.rect.y += self.velocidad_y
        self.rect.x += self.velocidad_x

        # Rotación realista continua
        self.angulo = (self.angulo + self.velocidad_rotacion) % 360
        centro_anterior = self.rect.center
        self.image = pygame.transform.rotate(self.image_original, self.angulo)
        self.rect = self.image.get_rect(center=centro_anterior)

        # Si el meteorito sale por abajo, reaparece arriba re-generado
        if self.rect.top > ALTO:
            self.reiniciar_posicion()

    def reiniciar_posicion(self):
        self.rect.x = random.randint(0, ANCHO - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.velocidad_y = random.randint(3, 7)
        self.velocidad_x = random.choice([-1, 0, 1])