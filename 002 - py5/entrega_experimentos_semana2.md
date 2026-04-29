# Entrega - Semana 2 (Fundamentos)

## Actividad 1 - Lupa de píxeles

Implementé el sketch `lupa.py` para leer el píxel bajo el mouse y mostrar:
- posición `(x, y)`
- valores `R, G, B`
- un cuadro ampliado con ese color.

### Experimentos realizados

1. **Color negativo**
   - Cambio aplicado: `py5.fill(255-r, 255-g, 255-b)`.
   - Resultado observado: rojo puro pasa a cian; blanco pasa a negro.

2. **Aislar canal rojo**
   - Cambio aplicado: `py5.fill(r, 0, 0)`.
   - Resultado observado: zonas verdes/azules se ven oscuras por tener poco rojo.

3. **Quitar protección de coordenadas**
   - Cambio aplicado: reemplazar `constrain()` por `mouse_x`/`mouse_y` directos.
   - Resultado observado: al salir del área de imagen se produce error por índice fuera de rango.

---

## Actividad 2 - Mezclador de canales con mouse

Implementé el sketch `canal_mouse.py` para modificar el canal rojo de cada píxel según `mouse_x`, mostrando original (izquierda) y resultado filtrado (derecha).

### Experimentos realizados

1. **Suprimir rojo**
   - Cambio aplicado: `r = 0`.
   - Resultado observado: la imagen queda en tonos frío (verde/azul) y baja intensidad en objetos rojos.

2. **Intercambiar rojo y azul**
   - Cambio aplicado: `py5.color(b, g, r)`.
   - Resultado observado: cielos azules se vuelven rojizos; objetos rojos se vuelven azulados.

3. **Controlar otro canal**
   - Cambio aplicado: aplicar factor al verde (`g = g * factor`).
   - Resultado observado: el desplazamiento horizontal controla la dominante verde.

4. **Control bidimensional (extra)**
   - Cambio aplicado: usar `mouse_x` para rojo y `mouse_y` para azul.
   - Resultado observado: se obtiene mezcla de color en tiempo real según la posición del mouse.

## Conclusión breve

Las pruebas confirman que una imagen digital es una matriz de valores numéricos y que modificar canales o rangos cambia directamente el resultado visual.
