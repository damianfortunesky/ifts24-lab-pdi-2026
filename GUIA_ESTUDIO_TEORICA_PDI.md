# Guía teórica exhaustiva de estudio — Procesamiento Digital de Imágenes y Visión por Computadora

> Materia: Laboratorio de Fundamentos de Procesamiento Digital de Imágenes, Visión por Computadora, VLMs y Agentic AI.  
> Repositorio: `ifts24-lab-pdi-2026`.  
> Propósito: reunir, ordenar y profundizar los conceptos teóricos abordados en los notebooks y consignas del repositorio para estudiar, repasar y preparar trabajos prácticos, integradores y defensas orales.

---

## 1. Cómo usar esta guía

Esta guía está pensada como un documento de estudio integral. No reemplaza los notebooks: los organiza conceptualmente y agrega explicaciones, relaciones entre temas, criterios de decisión y preguntas de repaso.

Se recomienda leerla en este orden:

1. **Fundamentos de imagen digital**: qué es una imagen como matriz, qué significan píxel, resolución y profundidad de bits.
2. **Representación del color**: RGB, BGR, escala de grises, HSV y canales.
3. **Operaciones básicas**: lectura, visualización, recortes, canales, aritmética, brillo, contraste e histogramas.
4. **Muestreo, cuantización y formatos**: qué información se conserva o se pierde al adquirir, reducir, comprimir o guardar imágenes.
5. **Mejora y restauración**: ecualización, CLAHE, suavizado, reducción de ruido e inpainting.
6. **Segmentación y máscaras**: umbralización, Otsu, umbral adaptativo, segmentación por color y limpieza morfológica.
7. **Geometría y contornos**: transformaciones, perspectiva, detección de contornos y propiedades geométricas.
8. **Detección y reconocimiento básico**: coincidencia por plantilla y detección de rostros con Haar.
9. **Criterios de pipeline**: cómo combinar técnicas con diagnóstico, comparación y justificación.
10. **Git, reproducibilidad y comunicación técnica**: cómo documentar y entregar el trabajo.

---

## 2. Mapa de contenidos del repositorio

### 2.1 Unidad inicial con py5

La carpeta `001 - py5/` introduce el trabajo visual programado con scripts de py5. Los temas principales son:

- Coordenadas y lienzo.
- Color RGB y HSV.
- Carga de imágenes.
- Acceso a píxeles.
- Filtros simples.
- Interacción con mouse.
- Dibujo y experimentación visual.

La carpeta `002 - py5/` profundiza los fundamentos de imagen digital, con versiones para Colab y entorno local, prácticas guiadas y laboratorio. Funciona como puente entre la programación visual creativa y el procesamiento digital de imágenes formal.

### 2.2 Fundamentos con NumPy, OpenCV y librerías de PDI

La carpeta `003 - librerias_fundamentos_pdi/` introduce el ecosistema técnico principal:

- Entorno Python y librerías: NumPy, OpenCV, Matplotlib, Pillow y scikit-image.
- Imágenes en color y canales.
- Operaciones básicas con OpenCV.
- Muestreo y cuantización.
- Práctica guiada de procesamiento.
- Segmentación simple por color.
- Recuperación y preprocesamiento de imágenes propias.
- Actividad integradora de segmentación por color.

### 2.3 Computer Vision parte 1

La carpeta `004 - computer_vision_parte_1/` desarrolla una secuencia más específica de visión por computadora:

- Introducción a OpenCV y espacios de color.
- Formatos de archivo de imagen.
- Mejora de imagen y ecualización básica.
- Comparación de estrategias de ecualización.
- Operaciones básicas con imágenes.
- Transformaciones geométricas y cambio de perspectiva.
- Operaciones gráficas.
- Filtros de suavizado y reducción de ruido.
- Umbralización global, Otsu y adaptive threshold.
- Morfología matemática para limpieza de máscaras.
- Restauración e inpainting.
- Detección de contornos.
- Propiedades geométricas de contornos.
- Coincidencia por plantilla.
- Detección de rostros con clasificadores Haar.
- Laboratorio exploratorio sobre color, paleta y segmentación.
- Utilidades y plantillas para trabajar de manera reproducible.

### 2.4 Trabajo Final Integrador 1

La carpeta `005 - TFI_1/` orienta la aplicación autónoma de los contenidos. El eje es construir tres pipelines de mejora y restauración para:

1. Imagen obtenida mediante cámara oscura.
2. Imagen de medio gráfico color.
3. Imagen de medio gráfico blanco y negro.

El foco evaluativo no es aplicar muchos filtros, sino diagnosticar un problema visual, comparar estrategias y defender una decisión técnica con evidencia.

---

## 3. Conceptos fundamentales de imagen digital

### 3.1 Imagen digital

Una imagen digital es una representación discreta de una escena o señal visual. En lugar de ser continua, se organiza como una grilla de elementos llamados **píxeles**. Cada píxel almacena uno o varios valores numéricos.

Formalmente, una imagen en escala de grises puede representarse como una función discreta:

```text
I(x, y) -> intensidad
```

donde `x` e `y` son coordenadas discretas y la intensidad suele tomar valores entre 0 y 255 si se usa una profundidad de 8 bits.

Una imagen color puede representarse como:

```text
I(x, y) -> (R, G, B)
```

o, en OpenCV, frecuentemente como:

```text
I(x, y) -> (B, G, R)
```

### 3.2 Píxel

Un píxel es la unidad mínima direccionable de una imagen digital. No es necesariamente un punto físico: es una muestra de información visual. Su significado depende del tipo de imagen:

- En una imagen binaria: 0 o 1, fondo u objeto.
- En escala de grises: intensidad luminosa.
- En color: combinación de canales.
- En una máscara: pertenencia o no pertenencia a una región.
- En una imagen médica o científica: puede representar magnitudes físicas específicas.

### 3.3 Resolución espacial

La resolución espacial indica cuántas muestras tiene la imagen. Se expresa como:

```text
ancho × alto
```

Por ejemplo, una imagen de `1920 × 1080` contiene 2.073.600 píxeles. Mayor resolución suele permitir mayor detalle, pero también implica:

- Más memoria.
- Más tiempo de procesamiento.
- Mayor costo de almacenamiento.
- Mayor necesidad de cómputo para filtros, segmentación o detección.

### 3.4 Profundidad de bits

La profundidad de bits indica cuántos niveles puede representar cada píxel o canal.

| Profundidad | Niveles | Uso típico |
|---:|---:|---|
| 1 bit | 2 | Imagen binaria |
| 8 bits | 256 | Escala de grises o canal color |
| 24 bits | 16.777.216 | RGB con 8 bits por canal |
| 32 bits flotante | Continuo aproximado | Procesamiento científico o intermedio |

Con 8 bits por canal, los valores posibles van de 0 a 255. Si una operación produce valores fuera de ese rango, hay que decidir si se recortan, normalizan o se trabaja temporalmente en otro tipo de dato.

### 3.5 Tipos de datos

En OpenCV y NumPy, una imagen no es solo una matriz: también tiene un tipo de dato.

Ejemplos comunes:

- `uint8`: enteros sin signo de 0 a 255. Muy común en imágenes.
- `float32`: flotantes, útiles para cálculos intermedios.
- `bool`: máscaras binarias.

Cuidado: en `uint8`, algunas operaciones pueden saturar, truncar o desbordar si no se manejan correctamente. Por eso muchas funciones de OpenCV, como `cv2.convertScaleAbs`, ayudan a aplicar transformaciones manteniendo rangos válidos.

---

## 4. Formación de la imagen: muestreo y cuantización

### 4.1 Escena continua versus imagen discreta

El mundo físico es continuo: la luz varía en el espacio, el tiempo y la longitud de onda. Una cámara transforma esa información continua en una matriz discreta. Ese proceso implica pérdida y simplificación.

### 4.2 Muestreo

El muestreo divide la escena en posiciones discretas. Cada posición corresponde a un píxel.

Si se reduce la resolución, se toman menos muestras. Esto puede producir:

- Pérdida de detalle fino.
- Bordes escalonados.
- Texturas menos reconocibles.
- Aliasing si no hay filtrado previo.

El muestreo responde a la pregunta:

```text
¿En cuántos puntos observo la escena?
```

### 4.3 Cuantización

La cuantización asigna valores discretos a intensidades que originalmente pueden variar de forma continua.

Responde a la pregunta:

```text
¿Cuántos niveles numéricos uso para representar cada muestra?
```

Con pocos niveles aparecen bandas, posterización o pérdida de gradientes suaves. En una imagen de 8 bits hay 256 niveles por canal; en una imagen binaria solo hay dos.

### 4.4 Relación entre muestreo, cuantización y calidad

- Mucho muestreo y buena cuantización: más detalle y gradaciones suaves.
- Mucho muestreo pero mala cuantización: muchos píxeles, pero tonos pobres.
- Poco muestreo pero buena cuantización: buen rango tonal, pero poco detalle espacial.
- Poco muestreo y mala cuantización: imagen pobre en detalle y en tonos.

---

## 5. Modelos de color y espacios de representación

### 5.1 RGB

RGB es un modelo aditivo de color. Cada color se forma combinando rojo, verde y azul.

Ejemplos con valores de 8 bits:

```text
(255, 0, 0)     rojo
(0, 255, 0)     verde
(0, 0, 255)     azul
(0, 0, 0)       negro
(255, 255, 255) blanco
```

Es el modelo más intuitivo para pantallas y visualización.

### 5.2 BGR en OpenCV

OpenCV carga imágenes color en orden **BGR**, no RGB. Esto es una fuente frecuente de errores.

Si se usa Matplotlib para mostrar una imagen cargada con OpenCV, debe convertirse:

```python
img_bgr = cv2.imread("imagen.jpg")
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
```

Si no se convierte, rojos y azules aparecerán intercambiados.

### 5.3 Escala de grises

Una imagen en escala de grises tiene un solo canal. No representa color, sino intensidad luminosa.

La conversión desde RGB/BGR no suele ser un promedio simple. Se ponderan los canales porque el sistema visual humano no percibe igual todos los colores. Una aproximación común es dar más peso al verde, luego al rojo y menos al azul.

Usos típicos:

- Ecualización de histograma.
- Detección de bordes.
- Umbralización.
- Contornos.
- Plantillas.
- Clasificadores Haar.

### 5.4 HSV

HSV separa el color en tres componentes:

- **Hue / Matiz**: tipo de color.
- **Saturation / Saturación**: pureza del color.
- **Value / Valor o brillo**: intensidad luminosa.

Es útil para segmentación por color porque permite aislar rangos de matiz de forma más directa que en RGB. Por ejemplo, para detectar objetos rojos, verdes o azules suele ser más robusto trabajar en HSV que comparar directamente canales RGB.

En OpenCV, el canal H no va de 0 a 360 sino de 0 a 179 para imágenes de 8 bits. Esto es importante al definir rangos.

### 5.5 LAB y otros espacios perceptuales

Aunque no siempre se profundiza en todos los notebooks, aparece como criterio técnico la idea de mejorar luminancia separada del color. Espacios como LAB permiten tratar la luminosidad en un canal separado de los componentes cromáticos. Esto es útil para mejorar contraste sin distorsionar demasiado los colores.

### 5.6 Separación de canales

Separar canales sirve para analizar qué información aporta cada componente. Por ejemplo:

- En RGB/BGR: intensidad de rojo, verde o azul.
- En HSV: matiz, saturación y brillo.
- En LAB: luminosidad y componentes cromáticos.

Preguntas útiles al observar canales:

- ¿El objeto se diferencia del fondo en un canal específico?
- ¿La iluminación afecta más al brillo que al color?
- ¿Conviene segmentar por matiz, por intensidad o por combinación de canales?

---

## 6. Lectura, visualización y estructura de imágenes en Python

### 6.1 Imagen como arreglo NumPy

En Python, una imagen cargada con OpenCV es un arreglo NumPy.

- Imagen en grises: forma `(alto, ancho)`.
- Imagen color: forma `(alto, ancho, canales)`.
- En color BGR típico: canales = 3.

Ejemplo conceptual:

```python
alto, ancho, canales = img.shape
pixel = img[y, x]
```

La coordenada del arreglo usa primero fila y luego columna, es decir:

```text
img[y, x]
```

No `img[x, y]`.

### 6.2 Mostrar imágenes

Con OpenCV, `cv2.imshow` abre ventanas locales. En notebooks se suele usar Matplotlib:

```python
plt.imshow(img_rgb)
plt.axis("off")
```

Para grises:

```python
plt.imshow(img_gray, cmap="gray")
plt.axis("off")
```

### 6.3 Recortes o regiones de interés

Un recorte se obtiene por slicing:

```python
roi = img[y1:y2, x1:x2]
```

La región de interés permite:

- Reducir fondo innecesario.
- Enfocar el análisis en una zona relevante.
- Disminuir costo computacional.
- Evitar que el histograma o la segmentación sean dominados por regiones irrelevantes.

### 6.4 Copias y vistas

En NumPy, algunas operaciones devuelven vistas, no copias. Si se modifica una vista, puede cambiar la imagen original. Para evitar efectos no deseados:

```python
roi = img[y1:y2, x1:x2].copy()
```

---

## 7. Operaciones básicas sobre píxeles

### 7.1 Transformaciones punto a punto

Una transformación punto a punto modifica cada píxel según una regla que no depende de sus vecinos.

Ejemplos:

- Sumar brillo.
- Multiplicar contraste.
- Invertir intensidades.
- Umbralizar.
- Aplicar una curva de corrección.

### 7.2 Brillo

Aumentar el brillo implica sumar una constante:

```text
I'(x, y) = I(x, y) + beta
```

donde `beta` es positivo para aclarar y negativo para oscurecer.

Riesgo: saturación. Si muchos valores llegan a 255, se pierde detalle en zonas claras.

### 7.3 Contraste

Ajustar contraste implica multiplicar por un factor:

```text
I'(x, y) = alpha * I(x, y)
```

- `alpha > 1`: aumenta contraste.
- `0 < alpha < 1`: reduce contraste.

Una forma combinada es:

```text
I'(x, y) = alpha * I(x, y) + beta
```

En OpenCV:

```python
resultado = cv2.convertScaleAbs(img, alpha=1.3, beta=20)
```

### 7.4 Inversión

La inversión transforma claros en oscuros y viceversa:

```text
I'(x, y) = 255 - I(x, y)
```

Puede servir para inspeccionar detalles, preparar máscaras o adaptar una imagen a algoritmos que esperan objetos claros sobre fondo oscuro.

### 7.5 Operaciones entre imágenes

Cuando se combinan imágenes, deben tener dimensiones y tipos compatibles.

Operaciones frecuentes:

- Suma ponderada.
- Diferencia absoluta.
- Máscaras bit a bit.
- Superposición de anotaciones.

Ejemplo de mezcla:

```python
mezcla = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)
```

---

## 8. Histograma y análisis tonal

### 8.1 Qué es un histograma

Un histograma cuenta cuántos píxeles tienen cada valor de intensidad. En una imagen de 8 bits en grises, hay 256 posibles intensidades.

Permite diagnosticar:

- Imagen oscura: valores concentrados a la izquierda.
- Imagen clara: valores concentrados a la derecha.
- Bajo contraste: valores concentrados en un rango estrecho.
- Alto contraste: valores distribuidos en gran parte del rango.
- Saturación: acumulación fuerte en 0 o 255.

### 8.2 Histograma por canal

En imágenes color, puede analizarse un histograma por canal. Esto ayuda a detectar dominantes de color o canales poco informativos.

### 8.3 Limitaciones del histograma

El histograma no contiene información espacial. Dos imágenes distintas pueden tener histogramas parecidos. Por eso el histograma debe combinarse con observación visual, recortes y métricas si corresponde.

---

## 9. Formatos de archivo de imagen

### 9.1 Formato versus contenido

Un formato de archivo define cómo se guarda la imagen en disco. No debe confundirse con la matriz de píxeles que se procesa en memoria.

### 9.2 Formatos frecuentes

| Formato | Compresión | Características | Uso típico |
|---|---|---|---|
| JPEG/JPG | Con pérdida | Buen tamaño, puede generar artefactos | Fotografía |
| PNG | Sin pérdida | Conserva bordes, puede tener transparencia | Gráficos, capturas, máscaras |
| TIFF | Puede ser sin pérdida | Flexible, usado en ámbitos profesionales | Archivo, escaneo, ciencia |
| BMP | Poca o nula compresión | Archivos grandes | Uso simple o histórico |

### 9.3 Compresión con pérdida

JPEG reduce tamaño descartando información menos perceptible. Puede producir:

- Bloques visibles.
- Bordes con artefactos.
- Pérdida de textura fina.
- Cambios que afectan segmentación o análisis de detalle.

Para procesamiento donde importan bordes, texto o máscaras, PNG suele ser más adecuado.

### 9.4 Guardado de resultados

Al guardar resultados es importante:

- Usar nombres claros.
- No sobrescribir originales.
- Guardar salidas intermedias si son relevantes para justificar decisiones.
- Conservar una carpeta de imágenes originales y otra de resultados.

---

## 10. Mejora de imagen

### 10.1 Mejora versus restauración

- **Mejora**: busca que una imagen sea más útil o interpretable. Puede ser subjetiva o dependiente de la tarea.
- **Restauración**: intenta corregir degradaciones conocidas o estimadas, como ruido, manchas o daños.

Ejemplo: aumentar contraste para leer mejor un texto es mejora; reconstruir zonas dañadas con inpainting es restauración.

### 10.2 Diagnóstico previo

Antes de aplicar filtros hay que diagnosticar:

- ¿La imagen está oscura o clara?
- ¿Tiene bajo contraste?
- ¿Hay ruido?
- ¿La iluminación es desigual?
- ¿Existe deformación geométrica?
- ¿Hay manchas o daños localizados?
- ¿Qué parte de la imagen importa para la tarea?

Un buen pipeline nace de un diagnóstico, no de una lista de funciones.

### 10.3 Ajuste lineal de brillo y contraste

Es simple, rápido e interpretable. Sirve cuando la imagen requiere un desplazamiento o estiramiento tonal global.

Limitaciones:

- Puede saturar altas luces o sombras.
- No resuelve iluminación desigual.
- Puede amplificar ruido.

### 10.4 Ecualización global de histograma

La ecualización redistribuye intensidades para usar mejor el rango disponible. En OpenCV se aplica típicamente sobre grises:

```python
eq = cv2.equalizeHist(gray)
```

Ventajas:

- Aumenta contraste global.
- Puede revelar detalles ocultos.
- Es automática.

Limitaciones:

- Puede exagerar ruido.
- Puede producir aspecto artificial.
- Si se aplica mal en color, puede distorsionar cromaticidad.
- No siempre respeta diferencias locales.

### 10.5 Ecualización sobre luminancia

En imágenes color, suele ser mejor convertir a HSV o LAB, mejorar solo el canal de brillo/luminancia y volver al espacio original.

Ventaja: mejora iluminación sin alterar tanto los colores.

### 10.6 CLAHE

CLAHE significa **Contrast Limited Adaptive Histogram Equalization**. Es una ecualización adaptativa limitada por contraste.

Idea central:

- Divide la imagen en regiones pequeñas.
- Ecualiza localmente.
- Limita la amplificación para evitar exagerar ruido.

Parámetros típicos:

- `clipLimit`: controla cuánto se limita el contraste.
- `tileGridSize`: tamaño de la grilla local.

Uso típico:

```python
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
resultado = clahe.apply(gray)
```

Conviene para:

- Imágenes con iluminación no uniforme.
- Cámara oscura.
- Documentos o medios gráficos con zonas desparejas.
- Casos donde la ecualización global falla.

### 10.7 Comparar estrategias de mejora

Para comparar no alcanza con decir “se ve mejor”. Conviene responder:

- ¿Qué problema resolvió?
- ¿Qué detalle recuperó o hizo más visible?
- ¿Qué artefacto introdujo?
- ¿Qué parámetro fue crítico?
- ¿Qué versión conserva mejor la información importante?

---

## 11. Ruido y filtros de suavizado

### 11.1 Qué es el ruido

El ruido es variación indeseada en la imagen. Puede originarse en el sensor, la iluminación, la compresión, el escaneo o la transmisión.

Tipos frecuentes:

- **Ruido gaussiano**: variaciones pequeñas distribuidas alrededor del valor real.
- **Sal y pimienta**: píxeles aislados blancos o negros.
- **Ruido de compresión**: artefactos por formatos con pérdida.
- **Ruido de escaneo o textura de papel**: variaciones en fondos impresos.

### 11.2 Filtro promedio

Reemplaza cada píxel por el promedio de sus vecinos.

Ventajas:

- Simple.
- Reduce variaciones pequeñas.

Desventajas:

- Desenfoca bordes.
- Puede perder detalles.

### 11.3 Filtro gaussiano

Promedia vecinos con pesos gaussianos: los píxeles cercanos pesan más.

```python
suave = cv2.GaussianBlur(img, (5, 5), 0)
```

Es útil para ruido gaussiano y como preprocesamiento antes de umbralización o detección de bordes.

### 11.4 Filtro mediana

Reemplaza cada píxel por la mediana de sus vecinos.

```python
suave = cv2.medianBlur(img, 5)
```

Es especialmente útil para ruido sal y pimienta porque elimina valores extremos sin promediar tanto los bordes.

### 11.5 Filtro bilateral

Suaviza preservando bordes al considerar distancia espacial y diferencia de intensidad. Es más costoso, pero útil cuando se quiere reducir ruido sin perder contornos.

### 11.6 Criterios de elección

| Problema | Filtro recomendado | Motivo |
|---|---|---|
| Ruido fino gaussiano | Gaussiano | Suaviza variaciones locales |
| Puntos blancos/negros aislados | Mediana | Rechaza extremos |
| Suavizar preservando bordes | Bilateral | Considera similitud tonal |
| Preprocesar para umbral | Gaussiano o mediana | Reduce falsos cortes |

---

## 12. Umbralización y segmentación binaria

### 12.1 Segmentación

Segmentar es separar una imagen en regiones significativas. Puede ser por color, intensidad, textura, forma o modelos aprendidos.

En el curso, una estrategia central es generar **máscaras binarias**.

### 12.2 Máscara binaria

Una máscara es una imagen donde los píxeles indican pertenencia a una región:

```text
255 -> pertenece al objeto
0   -> fondo
```

Se usa para:

- Aislar objetos.
- Medir áreas.
- Encontrar contornos.
- Limpiar regiones.
- Aplicar operaciones solo en zonas seleccionadas.

### 12.3 Umbral global manual

Define un valor fijo `T`:

```text
si I(x, y) >= T -> 255
si I(x, y) < T  -> 0
```

En OpenCV:

```python
_, mask = cv2.threshold(gray, T, 255, cv2.THRESH_BINARY)
```

Ventajas:

- Simple.
- Interpretable.
- Rápido.

Limitaciones:

- Falla con iluminación desigual.
- Requiere elegir `T`.
- Puede no separar bien si histograma de objeto y fondo se superponen.

### 12.4 Otsu

Otsu elige automáticamente un umbral buscando separar dos clases de intensidades. Funciona bien cuando el histograma es aproximadamente bimodal: una clase para fondo y otra para objeto.

```python
_, mask = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
```

Ventajas:

- Automático.
- Buen punto de partida.

Limitaciones:

- No funciona bien si hay iluminación variable.
- Supone separación tonal razonable.
- Puede fallar si hay más de dos clases importantes.

### 12.5 Umbral adaptativo

Calcula umbrales locales para regiones de la imagen.

```python
mask = cv2.adaptiveThreshold(
    gray, 255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    blockSize=31,
    C=5
)
```

Conviene cuando:

- El fondo no es uniforme.
- Hay sombras.
- El documento o imagen tiene iluminación irregular.

Parámetros clave:

- `blockSize`: tamaño de la vecindad local. Debe ser impar.
- `C`: constante que ajusta el umbral local.

### 12.6 Umbralización inversa

A veces el objeto aparece oscuro sobre fondo claro. En ese caso se usa `THRESH_BINARY_INV` para obtener objeto blanco y fondo negro, lo que facilita contornos y morfología.

---

## 13. Segmentación por color

### 13.1 Idea general

La segmentación por color busca píxeles cuyo color cae dentro de un rango.

En HSV:

```python
hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, lower, upper)
```

### 13.2 Por qué HSV suele ser mejor que RGB

En RGB, cambios de iluminación afectan simultáneamente los tres canales. En HSV, el matiz puede mantenerse más estable frente a cambios moderados de brillo.

Esto permite definir rangos como:

```text
H entre h1 y h2
S mayor que cierto mínimo
V mayor que cierto mínimo
```

### 13.3 El caso del rojo

En OpenCV, el matiz rojo queda cerca de 0 y también cerca del extremo superior de H. Por eso suele requerir dos rangos:

```text
rojo bajo: H cerca de 0
rojo alto: H cerca de 179
```

Luego se combinan máscaras.

### 13.4 Limitaciones

La segmentación por color falla o se complica cuando:

- El objeto y el fondo tienen colores parecidos.
- Hay sombras fuertes.
- Hay reflejos.
- La cámara altera balance de blancos.
- El color del objeto varía mucho.
- El rango elegido es demasiado estrecho o demasiado amplio.

---

## 14. Morfología matemática

### 14.1 Para qué sirve

La morfología matemática trabaja sobre formas, generalmente en máscaras binarias. Sirve para limpiar ruido, cerrar huecos, separar objetos y mejorar regiones antes de medir o detectar contornos.

### 14.2 Elemento estructurante

Es una pequeña matriz que define la vecindad usada por la operación. Puede ser rectangular, elíptica o cruz.

```python
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
```

### 14.3 Erosión

Reduce regiones blancas. Elimina puntos pequeños y achica objetos.

```python
eros = cv2.erode(mask, kernel, iterations=1)
```

Útil para:

- Eliminar ruido blanco aislado.
- Separar objetos unidos por puentes finos.

Riesgo: puede destruir detalles del objeto.

### 14.4 Dilatación

Expande regiones blancas. Rellena pequeños huecos y agranda objetos.

```python
dil = cv2.dilate(mask, kernel, iterations=1)
```

Útil para:

- Conectar partes cercanas.
- Engrosar trazos.
- Recuperar regiones cortadas.

Riesgo: puede unir objetos separados.

### 14.5 Apertura

Erosión seguida de dilatación.

```python
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
```

Sirve para eliminar ruido blanco pequeño manteniendo la forma general de objetos más grandes.

### 14.6 Clausura

Dilatación seguida de erosión.

```python
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
```

Sirve para cerrar huecos pequeños y unir discontinuidades.

### 14.7 Gradiente morfológico

Diferencia entre dilatación y erosión. Resalta bordes de regiones binarias.

### 14.8 Criterio de uso

- Si sobran puntos blancos pequeños: apertura.
- Si faltan partes o hay huecos: clausura.
- Si los objetos se pegan: erosión moderada.
- Si los trazos se cortan: dilatación o clausura.

---

## 15. Restauración e inpainting

### 15.1 Restauración

La restauración intenta corregir degradaciones. A diferencia de la mejora general, suele partir de un defecto específico: rayón, mancha, zona dañada o ruido.

### 15.2 Inpainting

El inpainting rellena regiones dañadas usando información del entorno. Requiere una máscara que indique qué píxeles deben reconstruirse.

Flujo típico:

1. Cargar imagen.
2. Crear máscara del daño.
3. Aplicar inpainting.
4. Comparar con original.

Ejemplo:

```python
restaurada = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)
```

### 15.3 Limitaciones

El inpainting no recupera información real perdida: estima contenido plausible. Funciona mejor en daños pequeños, fondos continuos o texturas simples. Puede fallar en texto, rostros, patrones complejos o estructuras geométricas finas.

---

## 16. Transformaciones geométricas

### 16.1 Coordenadas

Las transformaciones geométricas cambian la posición de los píxeles. Pueden servir para corregir perspectiva, rotar, escalar o alinear imágenes.

### 16.2 Traslación

Desplaza la imagen en `x` e `y`.

### 16.3 Escalado

Cambia tamaño. Si se agranda, se interpolan valores; si se achica, se pierde información.

Interpolaciones frecuentes:

- `INTER_NEAREST`: rápida, puede pixelar.
- `INTER_LINEAR`: balance común.
- `INTER_AREA`: recomendada para reducir.
- `INTER_CUBIC`: puede dar mejor calidad al ampliar, con más costo.

### 16.4 Rotación

Gira la imagen alrededor de un punto. Puede requerir ampliar lienzo o aceptar recortes.

### 16.5 Transformación afín

Preserva paralelismo. Se define con tres puntos de origen y tres de destino. Permite rotación, escala, cizalla y traslación.

### 16.6 Transformación de perspectiva

Corrige deformaciones donde líneas paralelas en la escena convergen en la imagen, como una hoja fotografiada en ángulo.

Se define con cuatro puntos de origen y cuatro de destino:

```python
M = cv2.getPerspectiveTransform(src, dst)
rectificada = cv2.warpPerspective(img, M, (ancho, alto))
```

Usos:

- Rectificar cartas, documentos o medios gráficos.
- Preparar una imagen para OCR o análisis.
- Comparar regiones en vista frontal.

### 16.7 Criterios para elegir puntos

Los puntos deben corresponder a esquinas reales y estar ordenados consistentemente. Una mala selección puede producir deformaciones severas.

---

## 17. Contornos y propiedades geométricas

### 17.1 Qué es un contorno

Un contorno es una curva que delimita una región. En OpenCV se obtiene generalmente a partir de una máscara binaria.

```python
contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
```

### 17.2 Preprocesamiento necesario

La calidad de los contornos depende de la máscara. Antes de buscar contornos conviene:

- Convertir a grises o HSV.
- Umbralizar o segmentar.
- Limpiar con morfología.
- Eliminar ruido.

### 17.3 Modos de recuperación

- `RETR_EXTERNAL`: solo contornos externos.
- `RETR_TREE`: conserva jerarquía de contornos internos y externos.
- `RETR_LIST`: lista todos sin jerarquía completa.

### 17.4 Aproximación

- `CHAIN_APPROX_SIMPLE`: comprime puntos redundantes.
- `CHAIN_APPROX_NONE`: guarda todos los puntos.

### 17.5 Área

```python
area = cv2.contourArea(cnt)
```

Sirve para filtrar objetos pequeños o seleccionar el objeto principal.

### 17.6 Perímetro

```python
perimetro = cv2.arcLength(cnt, True)
```

El segundo argumento indica si el contorno es cerrado.

### 17.7 Bounding box

Rectángulo alineado con los ejes:

```python
x, y, w, h = cv2.boundingRect(cnt)
```

Sirve para recortar objetos detectados.

### 17.8 Rectángulo mínimo rotado

```python
rect = cv2.minAreaRect(cnt)
```

Útil cuando el objeto está inclinado.

### 17.9 Centroide y momentos

Los momentos permiten calcular centroide:

```python
M = cv2.moments(cnt)
cx = int(M["m10"] / M["m00"])
cy = int(M["m01"] / M["m00"])
```

Hay que evitar dividir por cero si el área es nula.

### 17.10 Circularidad y descriptores simples

Una medida simple de circularidad:

```text
circularidad = 4π * área / perímetro²
```

Valores cercanos a 1 indican formas más circulares. Es útil como descriptor geométrico básico.

---

## 18. Coincidencia por plantilla

### 18.1 Idea general

La coincidencia por plantilla busca una imagen pequeña dentro de una imagen mayor. Compara la plantilla con ventanas deslizantes de la imagen.

```python
res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
```

Luego se localiza el mejor valor:

```python
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
```

### 18.2 Usos

- Encontrar un patrón conocido.
- Detectar objetos rígidos con apariencia estable.
- Localizar logos, íconos o fragmentos.

### 18.3 Limitaciones

Falla si el objeto cambia mucho en:

- Escala.
- Rotación.
- Iluminación.
- Perspectiva.
- Deformación.
- Oclusión.

Para robustez mayor se requieren enfoques más avanzados, pero la coincidencia por plantilla es excelente para entender correlación visual y búsqueda por similitud.

---

## 19. Detección de rostros con Haar

### 19.1 Clasificadores Haar

Los clasificadores Haar usan características simples de contraste rectangular y una cascada de decisión entrenada. OpenCV incluye clasificadores preentrenados para rostros.

Flujo típico:

1. Cargar imagen.
2. Convertir a escala de grises.
3. Cargar clasificador.
4. Detectar rostros.
5. Dibujar rectángulos.

### 19.2 Parámetros importantes

- `scaleFactor`: cuánto se reduce la imagen en cada escala de búsqueda.
- `minNeighbors`: cuántas detecciones cercanas se requieren para aceptar una región.
- `minSize`: tamaño mínimo del rostro.

### 19.3 Limitaciones

- Sensible a pose, iluminación y oclusiones.
- Puede generar falsos positivos.
- Es menos robusto que detectores modernos basados en aprendizaje profundo.
- Funciona mejor con rostros frontales y condiciones relativamente controladas.

---

## 20. Operaciones gráficas y anotación

Las operaciones gráficas permiten comunicar resultados sobre la imagen:

- Dibujar líneas.
- Dibujar rectángulos.
- Dibujar círculos.
- Escribir texto.
- Marcar contornos.
- Señalar puntos de interés.

Ejemplo:

```python
cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
cv2.putText(img, "objeto", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)
```

Estas operaciones son importantes para informes y notebooks porque convierten resultados numéricos en evidencia visual comprensible.

---

## 21. Pipelines de procesamiento

### 21.1 Qué es un pipeline

Un pipeline es una secuencia razonada de operaciones. No es una acumulación arbitraria de filtros.

Ejemplo general:

```text
carga -> diagnóstico -> preprocesamiento -> segmentación/mejora -> limpieza -> medición -> visualización -> evaluación
```

### 21.2 Principios de diseño

Un buen pipeline debe ser:

- **Pertinente**: cada paso responde a un problema.
- **Acotado**: no incluye pasos innecesarios.
- **Reproducible**: se puede ejecutar de nuevo.
- **Explicable**: se justifica con criterios técnicos.
- **Comparable**: permite evaluar alternativas.
- **Honesto**: reconoce límites y artefactos.

### 21.3 Diagnóstico

Antes de elegir técnicas, describir:

- Problema principal.
- Región importante.
- Condiciones de iluminación.
- Ruido visible.
- Pérdida de contraste.
- Deformaciones geométricas.
- Objetivo final.

### 21.4 Comparación de estrategias

El repositorio enfatiza comparar al menos dos estrategias en trabajos integradores. Una comparación sólida puede organizarse así:

| Aspecto | Estrategia A | Estrategia B |
|---|---|---|
| Objetivo | Qué intenta resolver | Qué intenta resolver |
| Operaciones | Pasos principales | Pasos principales |
| Parámetros | Valores usados | Valores usados |
| Resultado | Qué mejora | Qué mejora |
| Problemas | Qué artefactos deja | Qué artefactos deja |
| Decisión | Se elige o descarta | Se elige o descarta |

### 21.5 Ejemplo de pipeline: cámara oscura

Problemas frecuentes:

- Imagen oscura.
- Bajo contraste.
- Ruido.
- Fondo inútil.

Posible estrategia A:

```text
recorte -> ajuste lineal de brillo/contraste -> suavizado gaussiano
```

Posible estrategia B:

```text
recorte -> CLAHE sobre luminancia -> mediana si hay puntos aislados
```

Criterio: si el problema es global, puede alcanzar ajuste lineal; si hay iluminación desigual, CLAHE suele ser más adecuado.

### 21.6 Ejemplo de pipeline: medio gráfico color

Problemas frecuentes:

- Perspectiva deformada.
- Colores apagados.
- Iluminación dominante.
- Manchas.

Posible estrategia A:

```text
rectificación de perspectiva -> mejora en HSV sobre V -> guardado
```

Posible estrategia B:

```text
rectificación -> CLAHE sobre luminancia -> inpainting de manchas localizadas
```

Criterio: si la geometría impide comparar o leer, corregir perspectiva antes de mejoras tonales.

### 21.7 Ejemplo de pipeline: medio gráfico blanco y negro

Problemas frecuentes:

- Fondo gris.
- Iluminación desigual.
- Ruido.
- Texto cortado.

Posible estrategia A:

```text
grises -> suavizado -> Otsu -> apertura
```

Posible estrategia B:

```text
grises -> adaptive threshold -> clausura
```

Criterio: Otsu si hay separación global clara; adaptativo si el fondo varía por sombras o escaneo irregular.

---

## 22. Reproducibilidad, notebooks y comunicación técnica

### 22.1 Notebook como informe ejecutable

Un notebook de la materia debe combinar:

- Introducción y objetivo.
- Carga de imágenes.
- Código ejecutable.
- Visualizaciones intermedias.
- Explicaciones breves.
- Comparación de resultados.
- Conclusión técnica.

### 22.2 Buenas prácticas

- Mantener imágenes originales sin modificar.
- Usar rutas relativas.
- Nombrar variables claramente.
- Mostrar antes/después.
- Explicar parámetros.
- Evitar celdas desordenadas o salidas irrelevantes.
- Guardar resultados finales en carpetas específicas.

### 22.3 Qué significa justificar

Justificar no es describir el código. Es explicar la relación entre problema, operación y resultado.

Malo:

```text
Apliqué GaussianBlur y quedó mejor.
```

Mejor:

```text
Apliqué GaussianBlur con kernel 5×5 porque el fondo presentaba ruido fino que generaba falsos positivos en la umbralización. El suavizado redujo puntos aislados, aunque también perdió algo de nitidez en bordes pequeños.
```

### 22.4 Uso responsable de IA

La IA puede ayudar a comparar alternativas, revisar errores y explicar conceptos, pero las decisiones finales deben ser del equipo. Si se usa IA, registrar:

- Caso.
- Objetivo de consulta.
- Pedido realizado.
- Qué se conservó.
- Qué se descartó.
- Qué se aprendió.

---

## 23. Git y organización del trabajo

### 23.1 Git

Git es un sistema de control de versiones. Permite guardar estados del proyecto, comparar cambios y trabajar ordenadamente.

Comandos básicos:

```bash
git status
git add .
git commit -m "mensaje claro"
git push origin main
git pull origin main
```

### 23.2 GitHub

GitHub permite publicar repositorios, compartir entregas mediante enlaces y mantener respaldo remoto.

### 23.3 Recomendaciones para la cursada

- Hacer `git pull` antes de empezar.
- Trabajar en carpetas ordenadas.
- No dejar notebooks o imágenes sueltas sin contexto.
- Usar mensajes de commit específicos.
- Verificar en GitHub que el archivo se publicó.
- Entregar enlaces directos al material correcto.

---

## 24. Glosario esencial

| Término | Definición |
|---|---|
| Píxel | Unidad mínima de información de una imagen digital. |
| Resolución | Cantidad de píxeles en ancho y alto. |
| Profundidad de bits | Cantidad de bits usados para representar intensidades o colores. |
| Canal | Componente de una imagen, como R, G, B, H, S o V. |
| BGR | Orden de canales usado por OpenCV para imágenes color. |
| RGB | Modelo aditivo de color rojo, verde y azul. |
| HSV | Espacio de color que separa matiz, saturación y brillo. |
| Histograma | Conteo de píxeles por intensidad o valor de canal. |
| Máscara | Imagen binaria que selecciona regiones. |
| Umbral | Valor usado para separar píxeles en clases. |
| Otsu | Método automático de umbralización basado en separación de clases. |
| Morfología | Operaciones sobre formas en máscaras binarias. |
| Erosión | Achica regiones blancas. |
| Dilatación | Agranda regiones blancas. |
| Apertura | Erosión seguida de dilatación; elimina ruido pequeño. |
| Clausura | Dilatación seguida de erosión; cierra huecos. |
| Contorno | Curva que delimita una región. |
| CLAHE | Ecualización adaptativa limitada por contraste. |
| Inpainting | Relleno de regiones dañadas usando contexto. |
| Pipeline | Secuencia razonada de procesamiento. |
| ROI | Región de interés. |
| Interpolación | Estimación de valores al transformar geometría. |

---

## 25. Preguntas de repaso por unidad

### 25.1 Imagen digital

1. ¿Por qué una imagen digital puede pensarse como una matriz?
2. ¿Qué diferencia hay entre resolución espacial y profundidad de bits?
3. ¿Qué información se pierde al reducir resolución?
4. ¿Qué información se pierde al reducir niveles de cuantización?
5. ¿Por qué el tipo `uint8` requiere cuidado al hacer operaciones aritméticas?

### 25.2 Color

1. ¿Por qué OpenCV usa BGR y por qué eso importa al mostrar con Matplotlib?
2. ¿Cuándo conviene usar HSV en lugar de RGB?
3. ¿Por qué el rojo suele necesitar dos rangos de H en OpenCV?
4. ¿Qué canal modificarías para mejorar brillo sin alterar demasiado el color?
5. ¿Qué se puede aprender mirando canales por separado?

### 25.3 Mejora

1. ¿Cuándo alcanza con brillo y contraste lineal?
2. ¿Qué riesgo tiene la ecualización global?
3. ¿Qué problema intenta resolver CLAHE?
4. ¿Por qué conviene comparar histograma y resultado visual?
5. ¿Qué significa que una mejora sea dependiente de la tarea?

### 25.4 Ruido

1. ¿Qué filtro usarías para ruido sal y pimienta?
2. ¿Qué filtro usarías para ruido gaussiano?
3. ¿Qué desventaja común tienen los filtros de suavizado?
4. ¿Por qué un suavizado previo puede ayudar a una umbralización?
5. ¿Cómo justificarías el tamaño de kernel?

### 25.5 Segmentación

1. ¿Qué es una máscara binaria?
2. ¿Cuándo usarías umbral global manual?
3. ¿Cuándo usarías Otsu?
4. ¿Cuándo usarías adaptive threshold?
5. ¿Qué problemas aparecen si el objeto y el fondo tienen intensidades parecidas?

### 25.6 Morfología

1. ¿Qué diferencia hay entre erosión y dilatación?
2. ¿Para qué sirve la apertura?
3. ¿Para qué sirve la clausura?
4. ¿Qué rol cumple el elemento estructurante?
5. ¿Qué riesgo tiene aplicar demasiadas iteraciones?

### 25.7 Geometría y contornos

1. ¿Cuándo conviene rectificar perspectiva?
2. ¿Qué diferencia hay entre transformación afín y perspectiva?
3. ¿Por qué los contornos dependen de la calidad de la máscara?
4. ¿Cómo filtrarías contornos irrelevantes?
5. ¿Qué propiedades geométricas usarías para describir un objeto?

### 25.8 Pipelines

1. ¿Qué diferencia hay entre aplicar filtros y construir un pipeline?
2. ¿Por qué es obligatorio comparar estrategias en un trabajo integrador?
3. ¿Qué debe incluir un diagnóstico inicial?
4. ¿Cómo se argumenta una elección final?
5. ¿Qué límites conviene reconocer en una restauración?

---

## 26. Checklist para preparar una defensa oral

Antes de defender un trabajo, poder responder:

- ¿Cuál era el problema visual principal?
- ¿Qué evidencia mostraba ese problema?
- ¿Qué alternativas se probaron?
- ¿Qué parámetros fueron importantes?
- ¿Por qué se eligió el pipeline final?
- ¿Qué mejora concreta produjo?
- ¿Qué artefactos o límites quedaron?
- ¿Qué harías distinto con más tiempo?
- ¿Qué parte del resultado es objetiva y qué parte depende del criterio visual?
- ¿Cómo se puede reproducir el trabajo?

---

## 27. Plantilla de análisis para cualquier imagen

Puede usarse como guía antes de programar:

```text
1. Descripción de la imagen
   - Origen:
   - Formato:
   - Dimensiones:
   - Espacio de color:

2. Diagnóstico
   - Problema principal:
   - Problemas secundarios:
   - Región de interés:
   - Evidencia visual o histograma:

3. Objetivo
   - Qué quiero mejorar, segmentar, restaurar o medir:

4. Estrategia A
   - Pasos:
   - Parámetros:
   - Resultado:
   - Ventajas:
   - Límites:

5. Estrategia B
   - Pasos:
   - Parámetros:
   - Resultado:
   - Ventajas:
   - Límites:

6. Elección final
   - Estrategia elegida:
   - Justificación:
   - Qué problema resolvió:
   - Qué problema no resolvió:

7. Salidas
   - Imagen final guardada en:
   - Comparación antes/después incluida:
```

---

## 28. Errores frecuentes y cómo evitarlos

| Error | Consecuencia | Cómo evitarlo |
|---|---|---|
| Mostrar BGR como RGB | Colores incorrectos | Convertir con `cv2.cvtColor`. |
| Modificar el original | Se pierde referencia | Trabajar con copias. |
| Aplicar filtros sin diagnóstico | Pipeline débil | Explicar problema antes de operar. |
| No mostrar intermedios | No se entiende la decisión | Visualizar etapas clave. |
| Elegir umbral a ciegas | Máscara mala | Mirar histograma y probar alternativas. |
| Usar demasiada morfología | Deforma objetos | Ajustar kernel e iteraciones. |
| Guardar en JPEG una máscara | Artefactos de compresión | Guardar máscaras en PNG. |
| No justificar parámetros | Defensa débil | Relacionar parámetro con efecto observado. |
| Confundir `x,y` con `fila,columna` | Recortes incorrectos | Recordar `img[y, x]`. |
| Sobrescribir imágenes | Pérdida de evidencia | Separar originales y resultados. |

---

## 29. Síntesis final

La materia construye una progresión desde la comprensión de la imagen digital como matriz hasta la construcción de pipelines de visión por computadora. Los conceptos clave son:

- Toda imagen digital es una representación discreta y limitada de una escena.
- El color puede representarse en distintos espacios; elegir el espacio correcto simplifica el problema.
- El histograma ayuda a diagnosticar, pero no reemplaza la observación espacial.
- La mejora de imagen debe responder a un objetivo concreto.
- El ruido y la iluminación condicionan la elección de filtros y umbrales.
- Las máscaras son una herramienta central para segmentar, limpiar y medir.
- La morfología permite corregir errores estructurales en máscaras.
- Los contornos traducen regiones segmentadas en objetos analizables.
- Las transformaciones geométricas corrigen la relación espacial antes de analizar.
- Un pipeline sólido es breve, coherente, comparable y justificable.
- En trabajos integradores se evalúa tanto el resultado como la capacidad de explicar decisiones y límites.

Estudiar la materia implica no memorizar funciones aisladas, sino aprender a formular preguntas visuales, elegir representaciones adecuadas, probar alternativas y construir argumentos técnicos basados en evidencia.
