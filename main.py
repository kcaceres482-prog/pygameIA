import sys
import pygame

from enemigos import Meteorito
from estados import dibujar_interfaz
from fondo import FondoEspacial
from jugador import Jugador

pygame.init()
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Space Survival 2D")

reloj = pygame.time.Clock()
FPS = 60


def reiniciar_juego():
    global todos_los_sprites, meteoritos, jugador, puntuacion
    todos_los_sprites = pygame.sprite.Group()
    meteoritos = pygame.sprite.Group()

    jugador = Jugador()
    todos_los_sprites.add(jugador)

    for _ in range(10):
        m = Meteorito()
        meteoritos.add(m)
        todos_los_sprites.add(m)

    puntuacion = 0


# 2. CREAR LA INSTANCIA DEL FONDO
fondo = FondoEspacial()

estado_juego = "INICIO"
reiniciar_juego()

ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

        if evento.type == pygame.KEYDOWN:
            if estado_juego == "INICIO" and evento.key == pygame.K_SPACE:
                estado_juego = "JUGANDO"
            elif estado_juego == "GAMEOVER" and evento.key == pygame.K_r:
                reiniciar_juego()
                estado_juego = "JUGANDO"

    if estado_juego == "JUGANDO":
        todos_los_sprites.update()
        puntuacion += 1

        if pygame.sprite.spritecollide(jugador, meteoritos, False):
            estado_juego = "GAMEOVER"

    # 3. DIBUJAR EL FONDO EN MOVIMIENTO
    # Dibujamos el fondo primero para que todo lo demás (sprites e interfaz) quede encima
    fondo.actualizar_y_dibujar(pantalla)

    if estado_juego == "JUGANDO":
        todos_los_sprites.draw(pantalla)

    # Dibujar interfaz (menú de inicio, puntos, game over)
    dibujar_interfaz(pantalla, estado_juego, puntuacion)

    pygame.display.flip()
    reloj.tick(FPS)

pygame.quit()
sys.exit()