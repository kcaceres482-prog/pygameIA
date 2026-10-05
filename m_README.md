# Space Survival 2D

Un juego sencillo en 2D desarrollado en Python usando Pygame. El objetivo es controlar una nave espacial para esquivar los meteoritos que van cayendo y aguantar el mayor tiempo posible para sumar puntos.

## 🛠️ Ficha Técnica

* **Lenguaje:** Python 3
* **Librería:** Pygame
* **Archivos del proyecto:**
  * `main.py`: Archivo principal que ejecuta el juego, controla los estados (Inicio, Jugando, Game Over) y dibuja todo en pantalla.
  * `jugador.py`: Maneja la nave (movimiento con flechas/A-D y tamaño).
  * `enemigos.py`: Crea los meteoritos con formas irregulares, tamaños variados y movimiento con rotación.
  * `fondo.py`: Controla el fondo del espacio en movimiento continuo.
  * `estados.py`: Dibuja el texto en pantalla (puntos y mensajes de inicio/Game Over).

---

## 📝 Bitácora de Prompts (Prompt Log)

Para el desarrollo del juego se utilizaron las siguientes instrucciones principales con IA:

1. **Corrección de renderizado:** Solicitud para corregir el bucle de `main.py` agregando los meteoritos al grupo de dibujo para que aparezcan en pantalla.
2. **Ajuste de la nave:** Solicitud para agrandar el tamaño del sprite del jugador y quitarle el recuadro de fondo gris/blanco mediante transparencia.
3. **Fondo animado:** Implementación de un scroll infinito vertical en `fondo.py` para simular el avance de la nave por el espacio.
4. **Diseño de meteoritos:** Cambio de los cuadros rojos iniciales por asteroides creados mediante código vectorial, agregando sombras, cráteres y rotación.