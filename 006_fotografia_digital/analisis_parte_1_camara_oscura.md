# Análisis de resultados — Parte 1: cámara oscura y ecualización HSV

Este documento reúne conclusiones, fundamentos técnicos y textos breves para convertir el resultado de la Parte 1 en diapositivas de presentación. Está pensado para usarse junto con las imágenes generadas por `codigo/ecualizacion_hsv.py`.

## Materiales que se deben mostrar

Para defender la Parte 1 conviene ordenar la presentación en tres bloques:

1. **Registro del dispositivo:** fotos de `camara_oscura_1` y `camara_oscura_2`, mostrando la caja/dispositivo, la abertura y el plano donde se forma la imagen.
2. **Resultado óptico:** imagen original `img_camara_oscura_2` capturada con la cámara oscura, sin editar.
3. **Resultado digital:** comparación original/ecualizada, canales HSV e histograma del canal `V` antes y después.

## Fundamento óptico para explicar el resultado

La cámara oscura funciona por la **propagación rectilínea de la luz**. Cada punto de la escena emite o refleja rayos en muchas direcciones, pero la abertura pequeña deja pasar solo una porción limitada de esos rayos. Al cruzar por el orificio, los rayos provenientes de la parte superior de la escena llegan a la parte inferior del plano de imagen, y los rayos provenientes de la parte inferior llegan arriba. Por eso la imagen se forma **invertida**.

El resultado depende de un equilibrio físico:

- Una **abertura más pequeña** reduce la superposición de rayos y puede mejorar la nitidez, pero deja entrar menos luz.
- Una **abertura más grande** aumenta la luminosidad, pero también aumenta la mezcla de rayos y puede producir una imagen más borrosa.
- El **plano de imagen** debe recibir suficiente luz y estar estable; cualquier movimiento de cámara, escena o soporte vuelve más difícil distinguir detalles.

En una cámara oscura artesanal es esperable obtener una imagen con **bajo brillo, bajo contraste, pérdida de nitidez e inversión espacial**. Estos rasgos no son fallas aisladas del procesamiento digital: son consecuencias del sistema óptico construido y de la cantidad limitada de luz disponible.

## Análisis del procesamiento HSV

El script convierte la imagen original a HSV, separa los canales `H`, `S` y `V`, ecualiza solo `V` y recompone la imagen final. Esta decisión es importante porque separa la información de color de la información de brillo:

- `H` conserva el tono o familia de color.
- `S` conserva la saturación o intensidad cromática.
- `V` concentra el valor de brillo sobre el cual se mejora el contraste.

Al ecualizar el canal `V`, el histograma del brillo se redistribuye para ocupar mejor el rango disponible entre sombras, tonos medios y luces. En una captura de cámara oscura, donde la mayoría de los píxeles suele concentrarse en zonas oscuras o de bajo contraste, esta redistribución ayuda a que la imagen sea más legible.

## Qué mejoró visualmente

Después de ecualizar el canal `V`, el resultado debería mostrar:

- **Mayor contraste global:** se separan mejor las zonas oscuras, medias y claras.
- **Mejor lectura de formas:** bordes, siluetas y masas visuales pueden distinguirse con más claridad.
- **Aprovechamiento del rango tonal:** la imagen deja de estar concentrada en una franja estrecha de brillo.
- **Comparación más defendible:** el histograma antes/después permite explicar el cambio con evidencia visual y no solo con una opinión subjetiva.

Texto sugerido para la diapositiva:

> La ecualización del canal V aumentó la diferencia entre sombras y luces. Esto hizo que la imagen capturada con la cámara oscura resultara más legible, especialmente en zonas de bajo contraste.

## Qué información se perdió o no se pudo recuperar

La ecualización mejora la distribución del brillo, pero **no crea detalle nuevo**. Por eso hay límites claros:

- Si una zona quedó completamente negra, no hay textura real para recuperar.
- Si una zona quedó quemada o saturada, el detalle ya se perdió en la captura.
- Si hay desenfoque óptico o movimiento, el procesamiento puede hacerlo más visible, pero no reconstruye nitidez real.
- Si la imagen original tiene ruido en sombras, la ecualización puede aumentar su presencia visual.

Conclusión breve:

> El postproceso mejora la lectura de la imagen, pero no reemplaza una buena captura. La información que no fue registrada por el sistema óptico no puede recuperarse de manera auténtica con ecualización.

## Limitaciones observadas de la cámara oscura

Las principales limitaciones que se deben mencionar son:

1. **Poca entrada de luz:** obliga a trabajar con escenas luminosas o tiempos de exposición mayores.
2. **Imagen invertida:** es una propiedad esperada del sistema y debe explicarse como parte del fenómeno óptico.
3. **Nitidez limitada:** depende del diámetro de la abertura, de la distancia al plano de imagen y de la estabilidad del dispositivo.
4. **Bajo contraste:** la proyección interna puede verse tenue, especialmente si hay luz parásita dentro de la cámara o del ambiente.
5. **Sensibilidad al movimiento:** cualquier desplazamiento durante la captura afecta la lectura de formas.

Estas limitaciones ayudan a fundamentar por qué fue necesario aplicar un procesamiento posterior sobre el brillo.

## Por qué ecualizar V y no RGB directamente

Ecualizar los canales `R`, `G` y `B` por separado puede modificar cada componente de color con una intensidad distinta. Eso suele producir dominantes cromáticas, colores artificiales o desplazamientos de tono. En cambio, al trabajar en HSV se interviene principalmente el brillo mediante `V`, mientras `H` y `S` se conservan.

Fundamento para explicar oralmente:

> Elegimos HSV porque permite separar color y luminosidad. Como el problema principal de la captura era la falta de contraste y no la identidad del color, ecualizamos solo el canal V para mejorar el brillo sin alterar directamente el tono ni la saturación.

## Lectura del histograma antes/después

El histograma del canal `V` permite justificar el procesamiento de manera objetiva:

- **Antes:** si las barras están concentradas en una zona estrecha, la imagen tiene bajo contraste tonal.
- **Después:** si las barras se distribuyen en un rango más amplio, la imagen aprovecha mejor las intensidades disponibles.
- **Interpretación:** una distribución más amplia suele corresponderse con mayor separación visual entre sombras, medios tonos y luces.

No conviene afirmar que el resultado es “mejor” solo porque el histograma se expande. La conclusión correcta es que la ecualización **aumenta la legibilidad tonal**, aunque puede traer ruido o exagerar defectos de la captura.

## Conclusiones para usar en la presentación

- La cámara oscura permitió comprobar experimentalmente que la imagen se forma por rayos de luz que viajan en línea recta y se proyectan invertidos sobre un plano.
- El resultado original presentó limitaciones esperables: poca luminosidad, bajo contraste y nitidez condicionada por el tamaño de la abertura y la estabilidad del dispositivo.
- El procesamiento en HSV fue adecuado porque permitió intervenir el brillo sin modificar directamente la información de tono y saturación.
- La ecualización del canal `V` mejoró la lectura general de la imagen al redistribuir los niveles de brillo y hacer más visibles algunas formas.
- La mejora digital tuvo límites: no recuperó detalle inexistente, no corrigió completamente el desenfoque y pudo aumentar el ruido en zonas oscuras.
- La Parte 1 muestra la relación entre óptica y procesamiento digital: primero la cámara construye una imagen físicamente limitada, y luego el algoritmo reorganiza sus valores para hacerla más interpretable.

## Estructura sugerida de diapositivas

### Diapositiva 1 — Construcción de la cámara oscura

- Foto del dispositivo.
- Esquema de rayos de luz.
- Frase clave: “La imagen se invierte porque los rayos cruzan por una abertura pequeña”.

### Diapositiva 2 — Captura original

- Imagen `img_camara_oscura_2` sin editar.
- Marcar visualmente zonas de bajo contraste o poca nitidez.
- Frase clave: “El resultado evidencia las limitaciones físicas del dispositivo: entra poca luz y la nitidez depende de la abertura”.

### Diapositiva 3 — Procesamiento HSV

- Canales `H`, `S`, `V antes` y `V después`.
- Pseudocódigo breve: leer imagen → convertir a HSV → ecualizar V → recomponer → guardar.
- Frase clave: “Se modifica el brillo, no directamente el color”.

### Diapositiva 4 — Comparación y conclusiones

- Comparación original/ecualizada.
- Histograma antes/después.
- Cierre: “El postproceso aumenta la legibilidad, pero no inventa información que la cámara no capturó”.

## Texto final breve para defensa oral

La experiencia permitió unir un fenómeno óptico con una decisión de procesamiento digital. La cámara oscura produjo una imagen invertida, tenue y de bajo contraste debido a la entrada limitada de luz y a la relación entre abertura y nitidez. Luego, al convertir la imagen a HSV y ecualizar solo el canal `V`, se mejoró la distribución del brillo sin intervenir directamente el tono ni la saturación. El resultado final es más legible, pero conserva las limitaciones de la captura original: si no hubo detalle, foco o suficiente luz, el algoritmo no puede reconstruirlo de forma real. Por eso la conclusión principal es que el postproceso ayuda a interpretar la imagen, pero la calidad visual empieza en la captura y en las decisiones ópticas del dispositivo.
