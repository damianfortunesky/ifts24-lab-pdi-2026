# Trabajo Práctico 006 — Fotografía Digital

## Objetivo del trabajo

Completar una entrega que demuestre **intención visual, decisión técnica, lectura compositiva y postproceso consciente**. La entrega principal será `presentacion.pdf`, acompañada por fotografías originales/procesadas, descartes y scripts usados para el procesamiento digital.

## Estructura esperada de la carpeta

```text
006_fotografia_digital/
├── README.md
├── GUIA.txt
├── Introduccion a la fotografia.pdf
├── presentacion.pdf
├── imagenes/
│   ├── originales/
│   ├── procesadas/
│   └── descartes/
├── codigo/
│   ├── ecualizacion_hsv.py
│   ├── escala_grises.py
│   └── otros_scripts.py
└── recursos/
    └── referencias_opcionales/
```


## Resolución de la Parte 1

La resolución técnica de **Cámara oscura y procesamiento digital** está en:

- `parte_1_camara_oscura.md`: guía breve con nombres de archivos, explicación y justificación.
- `analisis_parte_1_camara_oscura.md`: conclusiones, fundamentos y estructura sugerida de diapositivas para defender los resultados de la Parte 1.
- `codigo/ecualizacion_hsv.py`: script que procesa `img_camara_oscura_2` en HSV, ecualiza solo el canal `V` y genera resultados para la presentación.

Uso recomendado desde la raíz del repositorio:

```bash
python "006_fotografia_digital/codigo/ecualizacion_hsv.py"
```

Antes de ejecutarlo, guardar en `imagenes/originales/` las fotos `camara_oscura_1`, `camara_oscura_2` y la captura a procesar `img_camara_oscura_2` con extensión `.jpg`, `.jpeg`, `.png`, `.webp`, `.bmp`, `.tif` o `.tiff`.

## Pasos para completar el trabajo práctico con éxito

### 1. Preparar materiales y organización

- [ ] Leer completa la guía del trabajo práctico (`GUIA.txt`).
- [ ] Mantener los archivos ordenados en la estructura solicitada.
- [ ] Guardar siempre las fotografías sin editar en `imagenes/originales/`.
- [ ] Guardar versiones editadas o procesadas en `imagenes/procesadas/`.
- [ ] Guardar intentos no elegidos en `imagenes/descartes/`, porque serán necesarios para la selección crítica.
- [ ] No usar imágenes generadas con IA, imágenes descargadas de internet, reemplazo de contenido ni fotomontajes complejos.

### 2. Construir y registrar la cámara oscura

- [ ] Construir una cámara oscura o dispositivo experimental simple.
- [ ] Fotografiar el dispositivo construido.
- [ ] Preparar un esquema sencillo que explique su funcionamiento.
- [ ] Explicar en la presentación:
  - propagación rectilínea de la luz;
  - proyección invertida;
  - plano de imagen;
  - relación entre apertura y nitidez.

### 3. Capturar una imagen con cámara oscura y procesarla en HSV

- [ ] Capturar una imagen usando la cámara oscura.
- [ ] Guardar la imagen original en `imagenes/originales/`.
- [ ] Crear `codigo/ecualizacion_hsv.py` para:
  - leer la imagen original;
  - convertir de BGR/RGB a HSV;
  - separar los canales H, S y V;
  - ecualizar únicamente el canal V;
  - recomponer la imagen;
  - guardar el resultado en `imagenes/procesadas/`;
  - generar histogramas antes/después.
- [ ] En la presentación, comparar original vs. ecualizada y responder:
  - qué mejoró visualmente;
  - qué información se perdió;
  - qué limitaciones tuvo la cámara oscura;
  - por qué conviene ecualizar V y no RGB directamente.

### 4. Producir una fotografía de simplicidad visual

- [ ] Tomar una fotografía donde el sujeto principal sea claro.
- [ ] Aplicar al menos una estrategia compositiva:
  - separación sujeto/fondo;
  - reducción de ruido visual;
  - profundidad de campo;
  - espacio negativo;
  - acercamiento;
  - conversión a blanco y negro o escala de grises.
- [ ] Crear `codigo/escala_grises.py` si se usa conversión a escala de grises.
- [ ] En la presentación, mostrar imagen original, imagen final y explicar:
  - qué elementos distraían;
  - qué se eliminó o simplificó;
  - cómo cambia la lectura si se usa escala de grises.

### 5. Trabajar reencuadres e interpretación

- [ ] Tomar una fotografía amplia.
- [ ] Producir al menos dos recortes distintos: `crop_a` y `crop_b`.
- [ ] Marcar en la imagen original las regiones recortadas.
- [ ] Comparar cómo cambia el significado al modificar el encuadre:
  - qué se vuelve importante;
  - qué información desaparece;
  - si cambia el sujeto;
  - si la imagen se vuelve más narrativa o más abstracta.

### 6. Explorar punto de vista y narrativa

- [ ] Elegir un mismo sujeto y fotografiarlo desde dos puntos de vista distintos.
- [ ] Asegurar que uno de los puntos de vista aporte información contextual nueva.
- [ ] Comparar en la presentación:
  - vista A;
  - vista B;
  - imagen final elegida;
  - explicación del cambio narrativo.

### 7. Realizar una fotografía basada en la luz

- [ ] Planificar una toma donde la luz sea el elemento estructural.
- [ ] Decidir conscientemente:
  - dirección de la luz;
  - calidad de la luz;
  - hora del día;
  - contraste;
  - sombras.
- [ ] Incluir un esquema simple de dirección de luz.
- [ ] Explicar si la luz revela, esconde, genera textura, volumen o atmósfera.

### 8. Seleccionar, descartar y justificar

- [ ] Tomar muchas fotografías para cada consigna.
- [ ] Comparar técnicamente y visualmente las alternativas.
- [ ] Mover las imágenes no elegidas a `imagenes/descartes/`.
- [ ] Preparar una diapositiva con miniaturas de descartes, imagen elegida y criterio de selección.
- [ ] Justificar por qué la imagen final funciona mejor que las descartadas.

### 9. Escribir la reflexión final

Responder brevemente en la presentación:

- [ ] ¿Qué aprendiste sobre mirar?
- [ ] ¿Qué diferencia hay entre registrar y construir una imagen?
- [ ] ¿Qué relación encontrás entre óptica, percepción y composición?
- [ ] ¿Cómo modifica el postproceso la lectura de una fotografía?

### 10. Preparar el anexo técnico

- [ ] Incluir fragmentos de código o pseudocódigo.
- [ ] Incluir histogramas y pruebas de procesamiento.
- [ ] Mostrar como mínimo:
  - conversión RGB/BGR ↔ HSV;
  - separación de canales H, S y V;
  - ecualización del canal V;
  - transformación a escala de grises.

### 11. Armar `presentacion.pdf`

La presentación debe funcionar como una **narrativa visual y técnica**, no como una acumulación de imágenes. Estructura sugerida:

1. Portada.
2. Construcción y registro de la cámara oscura.
3. Captura con cámara oscura + ecualización HSV.
4. Fotografía de simplicidad visual.
5. Reencuadre y reinterpretación.
6. Punto de vista y construcción narrativa.
7. Fotografía basada en la luz.
8. Selección crítica.
9. Reflexión final.
10. Anexo técnico.

### 12. Revisión final antes de entregar

- [ ] Confirmar que existe `presentacion.pdf` en `006_fotografia_digital/`.
- [ ] Confirmar que todas las imágenes usadas en la presentación están en el repositorio.
- [ ] Confirmar que los scripts mencionados están en `codigo/`.
- [ ] Revisar que cada diapositiva comunique una idea clara.
- [ ] Verificar que haya comparación entre originales, procesadas y descartes.
- [ ] Verificar que se expliquen decisiones técnicas y compositivas, no solo resultados estéticos.
- [ ] Revisar ortografía, nombres, comisión, fecha y título.
- [ ] Subir la entrega completa al repositorio GitHub.

## Prioridades de evaluación

Para maximizar el resultado, priorizar:

1. Comprensión óptica y cámara oscura.
2. Composición y lenguaje visual.
3. Procesamiento HSV correcto y explicado.
4. Uso consciente de la luz.
5. Reflexión crítica sobre decisiones, descartes y postproceso.
6. Organización clara del PDF y del repositorio.
