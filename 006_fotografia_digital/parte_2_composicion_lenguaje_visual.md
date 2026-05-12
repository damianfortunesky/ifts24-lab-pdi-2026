# Parte 2 — Composición y lenguaje visual

Esta resolución cubre las diapositivas **4, 5 y 6** de la guía del TP. La diapositiva 7, **Fotografía basada en la luz**, queda fuera de esta resolución porque se solicitó resolver la Parte 2 **menos el punto 7**.

## Imágenes de entrada

Guardar en `006_fotografia_digital/imagenes/originales/` las fotografías de la serie con estos nombres:

```text
img_p2_01.jpg
img_p2_02.jpg
img_p2_03.jpg
img_p2_04.jpg
img_p2_05.jpg
...
```

El script `codigo/composicion_parte_2.py` busca automáticamente `img_p2_0*` y genera versiones procesadas en `imagenes/procesadas/`.

Ejecución recomendada desde la raíz del repositorio:

```bash
python "006_fotografia_digital/codigo/composicion_parte_2.py"
```

## Diapositiva 4 — Simplicidad visual

**Material a usar**

- Imagen original: `imagenes/procesadas/p2_diap_04_simplicidad_original.jpg`.
- Imagen final: `imagenes/procesadas/p2_diap_04_simplicidad_final_grises.jpg`.

**Decisión compositiva**

Se usa la última fotografía de la serie como imagen final porque permite trabajar una lectura simple: el gato funciona como sujeto principal y se separa del sillón oscuro por contraste tonal. La conversión a escala de grises reduce información cromática secundaria y concentra la lectura en forma, postura, mirada y relación sujeto/fondo.

**Texto sugerido para la diapositiva**

> La imagen trabaja la simplicidad visual mediante la separación entre sujeto y fondo. El gato, de pelaje claro, se distingue del sillón oscuro, lo que permite reconocerlo rápidamente como sujeto principal. La versión en escala de grises reduce el peso del color y concentra la atención en la postura y la mirada del animal.

**Preguntas guía respondidas**

- **Elementos que distraían:** color y detalles secundarios del entorno doméstico.
- **Qué se elimina o simplifica:** la lectura cromática y parte de la competencia visual del fondo.
- **Cambio en escala de grises:** aumenta la importancia de las diferencias de luminosidad y de la silueta del gato.

## Diapositiva 5 — Reencuadre y reinterpretación

**Material a usar**

- Original con marcas: `imagenes/procesadas/p2_diap_05_original_con_recortes.jpg`.
- Recorte A: `imagenes/procesadas/p2_diap_05_recorte_a_gato.jpg`.
- Recorte B: `imagenes/procesadas/p2_diap_05_recorte_b_contexto.jpg`.
- Comparación lista para diapositiva: `imagenes/procesadas/p2_diap_05_comparacion_reencuadres.jpg`.

**Decisión compositiva**

Se parte de la primera fotografía como plano amplio. El **recorte A** concentra la atención en el gato y vuelve la imagen más íntima. El **recorte B** conserva más sillón y manta, por lo que la escena gana contexto y una lectura más narrativa del espacio doméstico.

**Texto sugerido para la diapositiva**

> A partir de una fotografía amplia se realizaron dos reencuadres. El primer recorte concentra la atención en el gato y genera una lectura más íntima. El segundo conserva más contexto, incluyendo la manta y el sillón, por lo que la imagen se vuelve más narrativa y muestra el entorno doméstico.

**Preguntas guía respondidas**

- **Qué se vuelve importante después del crop:** en el recorte A, el cuerpo y la expresión del gato; en el recorte B, la relación entre el gato, el sillón y la manta.
- **Qué información desaparece:** al cerrar el encuadre se pierden referencias del ambiente completo.
- **Cambio del sujeto:** el sujeto principal sigue siendo el gato, pero en el recorte B comparte protagonismo con el entorno.
- **Narrativa o abstracción:** el recorte A es más directo e íntimo; el recorte B es más contextual y narrativo.

## Diapositiva 6 — Punto de vista y construcción narrativa

**Material a usar**

- Vista A: `imagenes/procesadas/p2_diap_06_vista_a_desde_arriba.jpg`.
- Vista B: `imagenes/procesadas/p2_diap_06_vista_b_contextual.jpg`.
- Comparación lista para diapositiva: `imagenes/procesadas/p2_diap_06_comparacion_punto_de_vista.jpg`.

**Decisión compositiva**

La vista A usa la primera foto como punto de vista superior o cercano. La vista B usa la cuarta foto si está disponible; si no, toma la última de la serie. La comparación permite observar cómo cambia la escala aparente del gato y cuánta información del sillón y del ambiente entra en la imagen.

**Texto sugerido para la diapositiva**

> Al cambiar el punto de vista cambia la relación con el sujeto. Desde arriba, el gato parece más pequeño y contenido dentro del espacio del sillón. Desde una posición más frontal o lateral, el sujeto gana presencia y se percibe con mayor estabilidad. El cambio de cámara modifica la escala, el vínculo emocional y la información visual disponible.

**Preguntas guía respondidas**

- **Información que aparece desde el nuevo ángulo:** más referencias de volumen, apoyo del cuerpo y relación del gato con el sillón.
- **Cambio en la percepción del sujeto:** la vista superior lo presenta más contenido; la vista frontal o lateral lo vuelve más presente.
- **Relación emocional:** el acercamiento desde arriba puede sentirse más observacional; el punto de vista frontal o lateral genera una relación más directa.

## Archivos generados por el script

```text
imagenes/procesadas/p2_diap_04_simplicidad_original.jpg
imagenes/procesadas/p2_diap_04_simplicidad_final_grises.jpg
imagenes/procesadas/p2_diap_05_original_con_recortes.jpg
imagenes/procesadas/p2_diap_05_recorte_a_gato.jpg
imagenes/procesadas/p2_diap_05_recorte_b_contexto.jpg
imagenes/procesadas/p2_diap_05_comparacion_reencuadres.jpg
imagenes/procesadas/p2_diap_06_vista_a_desde_arriba.jpg
imagenes/procesadas/p2_diap_06_vista_b_contextual.jpg
imagenes/procesadas/p2_diap_06_comparacion_punto_de_vista.jpg
```

## Nota de ajuste fino

Los recortes del script están definidos como porcentajes relativos sobre la primera imagen. Si el gato no queda centrado en `img_p2_01.jpg`, ajustar las constantes `CROP_A_ROSTRO_CUERPO` y `CROP_B_SILLON_MANTA` dentro de `codigo/composicion_parte_2.py` antes de generar las imágenes definitivas.
