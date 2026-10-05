import pygame

ANCHO, ALTO = 800, 600


class FondoEspacial:

    def __init__(self):
        # Cargas cualquier JPG o PNG descargado
        imagen_raw = pygame.image.load("espacio.png").convert()
        self.imagen = pygame.transform.scale(imagen_raw, (ANCHO, ALTO))

        self.y1 = 0
        self.y2 = -ALTO
        self.velocidad = 2  # Velocidad del movimiento hacia abajo

    def actualizar_y_dibujar(self, pantalla):
        # Mover las dos copias hacia abajo
        self.y1 += self.velocidad
        self.y2 += self.velocidad

        # Repetir el bucle cuando salgan de pantalla
        if self.y1 >= ALTO:
            self.y1 = -ALTO
        if self.y2 >= ALTO:
            self.y2 = -ALTO

        pantalla.blit(self.imagen, (0, self.y1))
        pantalla.blit(self.imagen, (0, self.y2))