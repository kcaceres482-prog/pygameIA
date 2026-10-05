import pygame

ANCHO, ALTO = 800, 600
BLANCO = (255, 255, 255)
AZUL = (0, 180, 255)
ROJO = (240, 60, 60)
AMARILLO = (255, 215, 0)

pygame.font.init()
fuente_grande = pygame.font.SysFont("Arial", 48, bold=True)
fuente_media = pygame.font.SysFont("Arial", 28)

def mostrar_texto(pantalla, texto, fuente, color, x, y):
    superficie = fuente.render(texto, True, color)
    rect = superficie.get_rect(center=(x, y))
    pantalla.blit(superficie, rect)

def dibujar_interfaz(pantalla, estado_juego, puntuacion):
    if estado_juego == "INICIO":
        mostrar_texto(pantalla, "SPACE SURVIVAL 2D", fuente_grande, AZUL, ANCHO // 2, ALTO // 3)
        mostrar_texto(pantalla, "Usa A/D o Flechas para moverte", fuente_media, BLANCO, ANCHO // 2, ALTO // 2)
        mostrar_texto(pantalla, "Presiona ESPACIO para comenzar", fuente_media, AMARILLO, ANCHO // 2, ALTO // 2 + 60)

    elif estado_juego == "JUGANDO":
        mostrar_texto(pantalla, f"Puntos: {puntuacion}", fuente_media, BLANCO, 90, 30)

    elif estado_juego == "GAMEOVER":
        mostrar_texto(pantalla, "GAME OVER", fuente_grande, ROJO, ANCHO // 2, ALTO // 3)
        mostrar_texto(pantalla, f"Puntuación final: {puntuacion}", fuente_media, BLANCO, ANCHO // 2, ALTO // 2)
        mostrar_texto(pantalla, "Presiona 'R' para reiniciar", fuente_media, AMARILLO, ANCHO // 2, ALTO // 2 + 60)