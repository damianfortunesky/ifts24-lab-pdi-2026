# Plan de accion para resolver el TFI 1 (mejora y restauracion de imagenes)

Este documento traduce la consigna y la rubrica a un plan operativo para trabajar de forma ordenada dentro del notebook `TFI_1 - mejora y restauracion de imagenes.ipynb`.

---

## 0) Como identificar correctamente los tipos de imagen pedidos

La confusion es normal: en la consigna, “medio grafico” se refiere a imagenes que vienen de un **material impreso o publicado** (revista, diario, folleto, afiche, fotocopia, pagina escaneada), no a una foto cualquiera de camara.

### 2) Imagen de medio grafico color

Es una imagen de origen grafico/impreso que **conserva informacion de color**.

Ejemplos validos:

- foto de una pagina de revista a color;
- etiqueta o folleto impreso a color;
- afiche color fotografiado o escaneado;
- pagina de libro con ilustraciones a color.

Pistas visuales tipicas:

- tramas de impresion (puntitos CMYK);
- deformacion de perspectiva por foto con celular;
- dominante de luz (amarillenta/azulada);
- colores “lavados” o desbalanceados por captura.

### 3) Imagen de medio grafico blanco/negro

Es una imagen de origen grafico/impreso donde el objetivo principal suele ser la **legibilidad en tonos de gris o binario** (texto, lineas, formularios, fotocopias).

Ejemplos validos:

- hoja de apuntes/fotocopia en blanco y negro;
- pagina de diario con texto y poco contraste;
- documento escaneado con fondo gris;
- formulario impreso con ruido o sombras.

Pistas visuales tipicas:

- fondo sucio/grisaceo;
- sombras no uniformes;
- trazos cortados o letras poco legibles;
- ruido de escaneo o compresion.

### Regla practica para decidir rapido

- Si el problema principal es **color/cromaticidad/perspectiva de pieza color** → caso 2 (medio grafico color).
- Si el problema principal es **legibilidad de texto o trazos en escala de grises** → caso 3 (medio grafico blanco/negro).

---

## 1) Que significa “procedimiento” en este TFI

En este trabajo, un **procedimiento** es una estrategia reproducible para atacar un problema visual, definida por:

1. **Objetivo tecnico** (que defecto intenta corregir).
2. **Secuencia acotada de operaciones** (2 a 4 operaciones principales, segun recomienda la consigna).
3. **Parametros explicitos** (valores concretos o criterio para elegirlos).
4. **Criterio de evaluacion** (como se decide si mejoro o no).
5. **Limites esperables** (que no puede recuperar ese enfoque).

> En terminos de la rubrica, los procedimientos son la unidad que se compara entre “estrategia 1” y “estrategia 2” de cada caso.

### Plantilla minima para describir cada procedimiento

- **Nombre corto:**
- **Problema objetivo:**
- **Pipeline (pasos):**
- **Parametros clave:**
- **Por que deberia funcionar:**
- **Indicadores de mejora:**
- **Riesgos / limites:**

---

## 2) Criterio comun para comparar procedimientos (en los 3 casos)

Para poder comparar de forma justa (y no “a ojo”), usen esta misma estructura en cada caso:

1. **Mismo input**: ambas estrategias parten de la misma imagen original.
2. **Misma meta declarada**: definir en una frase el objetivo principal.
3. **Misma escala de evidencia**:
   - comparacion visual lado a lado;
   - 2-3 observaciones tecnicas concretas;
   - al menos 1 limitacion remanente.
4. **Decision final argumentada**:
   - que estrategia resuelve mejor el problema principal;
   - que trade-off acepta (ej: mas contraste pero mas ruido).

### Matriz corta de comparacion (copiable al notebook)

| Caso | Procedimiento | Que mejora | Que empeora o no resuelve | Decision |
|---|---|---|---|---|
| Camara oscura | A / B | ... | ... | Elijo ... |
| Medio grafico color | A / B | ... | ... | Elijo ... |
| Medio grafico B/N | A / B | ... | ... | Elijo ... |

---

## 3) Plan de accion general (paso a paso)

## Paso 0. Preparacion de materiales

- Crear/verificar carpetas:
  - `imagenes_tfi/` (entradas)
  - `salidas_tfi/` (resultados finales)
- Seleccionar 1 imagen por caso:
  - camara oscura;
  - medio grafico color;
  - medio grafico blanco/negro.
- Criterio de seleccion: que el defecto principal sea visible y permita justificar decisiones.

## Paso 1. Diagnostico inicial por caso

Para cada imagen, completar en notebook:

- **Defecto principal** (uno prioritario).
- **Defectos secundarios** (si existen).
- **Objetivo de mejora medible en terminos visuales**.

Frases guia:

- “El problema principal es ___ porque se observa ___.”
- “El objetivo del pipeline es ___ sin degradar ___.”

## Paso 2. Disenar dos procedimientos comparables por caso

- Procedimiento A: enfoque principal.
- Procedimiento B: variante realmente distinta (no solo cambiar un numero).

Regla: maximo 4 operaciones principales por procedimiento, salvo justificacion fuerte.

## Paso 3. Ejecutar y documentar cada procedimiento

En cada estrategia registrar:

- pasos exactos;
- parametros y por que se eligieron;
- salida intermedia o final;
- comentario tecnico corto.

## Paso 4. Comparar A vs B en cada caso

Responder en texto:

1. ¿Que problema resolvio mejor A/B?
2. ¿Que artefactos introdujo A/B?
3. ¿Cual preserva mejor la informacion importante?

## Paso 5. Elegir version final de cada caso

Completar:

- variable `imagen_*_final`;
- `justificacion_*_final` con argumento tecnico (no estetico);
- guardado en `salidas_tfi/`.

## Paso 6. Cierre transversal del integrador

Comparar los 3 casos:

- por que no conviene el mismo pipeline para todo;
- que relacion hubo entre tipo de degradacion y tipo de operacion;
- limites comunes de restauracion.

## Paso 7. Registro de uso de IA

Completar la tabla de IA con una entrada por caso:

- que sugerencia se adopto;
- que se descarto;
- que criterio propio se aplico.

---

## 4) Procedimientos sugeridos por caso (para arrancar rapido)

> Son propuestas base para iterar, no recetas cerradas.

## Caso 1: Camara oscura

### Procedimiento A (contraste local controlado)

1. Recorte ROI (si hay fondo inutil).
2. Conversion a LAB.
3. CLAHE sobre canal L.
4. Suavizado leve (gaussiano o mediana).

**Cuando conviene:** imagen opaca y plana, con detalles poco visibles.

**Riesgo:** levantar ruido en zonas oscuras.

### Procedimiento B (ajuste global + denoise)

1. Ajuste brillo/contraste (`convertScaleAbs`).
2. Suavizado mediana.
3. (Opcional) pequeno ajuste final de contraste.

**Cuando conviene:** oscuridad general homogenea.

**Riesgo:** saturar altas luces o “lavar” texturas.

---

## Caso 2: Medio grafico color

### Procedimiento A (geometria primero)

1. Rectificacion de perspectiva (4 puntos).
2. Correccion de color/contraste en LAB o HSV.
3. Ajuste de nitidez moderado (si hace falta).

**Cuando conviene:** texto/figuras inclinadas o deformadas.

**Riesgo:** mala seleccion de puntos genera distorsion nueva.

### Procedimiento B (color y dano local)

1. Correccion cromatica (HSV/LAB).
2. CLAHE suave en luminancia.
3. Inpainting en manchas localizadas (si existen).

**Cuando conviene:** geometria aceptable pero color apagado/manchas.

**Riesgo:** inpainting puede borrar detalle real si mascara mala.

---

## Caso 3: Medio grafico blanco/negro

### Procedimiento A (Otsu robusto)

1. Escala de grises.
2. Suavizado gaussiano corto.
3. Umbral Otsu.
4. Morfologia (apertura o clausura segun defecto).

**Cuando conviene:** histograma razonablemente separable.

**Riesgo:** falla con iluminacion muy desigual.

### Procedimiento B (adaptativo para iluminacion irregular)

1. Escala de grises.
2. `adaptiveThreshold`.
3. Limpieza morfologica puntual.

**Cuando conviene:** fondo no uniforme/sombras.

**Riesgo:** ruido granular o bordes serruchados si bloque/C no son adecuados.

---

## 5) Como fundamentar por escrito (estructura de redaccion)

Para cada caso usar este esquema breve:

1. **Diagnostico:** “Se observa ___, por lo tanto priorizamos ___.”
2. **Hipotesis A:** “Si aplicamos ___ esperamos ___ porque ___.”
3. **Hipotesis B:** “Probamos ___ para contrastar ___.”
4. **Comparacion:** “A mejora ___ pero empeora ___; B mejora ___ pero limita ___.”
5. **Decision:** “Elegimos ___ porque optimiza ___, aunque mantiene ___.”

---

## 6) Checklist alineado a la rubrica (antes de entregar)

- [ ] Los 3 casos estan resueltos.
- [ ] Hay 2 estrategias reales por caso.
- [ ] Se explicita el diagnostico inicial por caso.
- [ ] Hay comparacion tecnica (no solo estetica).
- [ ] La eleccion final esta justificada por criterio.
- [ ] Se muestran antes/despues.
- [ ] Se guardan 3 salidas finales.
- [ ] Hay cierre comparativo transversal.
- [ ] Se incluye reflexion sobre limites.
- [ ] Se completa el registro de uso de IA.

---

## 7) Siguiente iteracion (para trabajar conmigo)

Cuando elijas la primera imagen, avanzamos asi:

1. Definimos **diagnostico tecnico** en 3-5 lineas.
2. Te propongo **procedimiento A y B** con parametros iniciales.
3. Ejecutas, compartis resultados.
4. Ajustamos parametros con criterio.
5. Redactamos justificacion final lista para el notebook.
