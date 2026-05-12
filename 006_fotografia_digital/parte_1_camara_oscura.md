# Parte 1 — Cámara oscura y procesamiento digital

Este archivo resume qué hay que mostrar y cómo explicar la primera parte del TP.
La idea es que el proceso sea fácil de defender oralmente: primero se registra el
artefacto, después se procesa la imagen que produjo la cámara oscura y por último
se justifican las decisiones técnicas.

## Archivos que se deben usar

Guardar las fotos originales en `006_fotografia_digital/imagenes/originales/` con
estos nombres:

- `camara_oscura_1`: fotografía del dispositivo construido.
- `camara_oscura_2`: otra fotografía del artefacto, idealmente mostrando mejor la
  apertura o el interior.
- `img_camara_oscura_2`: imagen resultante capturada con la cámara oscura. Esta es
  la imagen que procesa el script.

Las extensiones pueden ser `.jpg`, `.jpeg`, `.png`, `.webp`, `.bmp`, `.tif` o
`.tiff`. Por ejemplo: `img_camara_oscura_2.jpg`.

## Qué hace el script

El script `codigo/ecualizacion_hsv.py` sigue la consigna de manera literal:

1. Lee `img_camara_oscura_2` desde la carpeta de originales.
2. Convierte la imagen de BGR a HSV.
3. Separa los canales `H`, `S` y `V`.
4. Ecualiza solamente el canal `V`.
5. Une otra vez `H`, `S` y `V ecualizado`.
6. Convierte el resultado de HSV a BGR.
7. Guarda la imagen final, los canales separados, una comparación y el histograma
   antes/después.

Comando recomendado desde la raíz del repositorio:

```bash
python "006_fotografia_digital/codigo/ecualizacion_hsv.py"
```

Si la foto está en otra ruta:

```bash
python "006_fotografia_digital/codigo/ecualizacion_hsv.py" \
  --entrada "006_fotografia_digital/imagenes/originales/img_camara_oscura_2.jpg"
```

## Archivos que genera

En `006_fotografia_digital/imagenes/procesadas/` se generan:

- `img_camara_oscura_2_ecualizada_hsv_v.png`: imagen final procesada.
- `img_camara_oscura_2_histograma_v_antes_despues.png`: histograma del canal V
  antes y después.
- `img_camara_oscura_2_comparacion_original_ecualizada.png`: comparación lista
  para usar en la presentación.
- `img_camara_oscura_2_canal_h.png`: canal H, tono/color base.
- `img_camara_oscura_2_canal_s.png`: canal S, saturación.
- `img_camara_oscura_2_canal_v_antes.png`: brillo original.
- `img_camara_oscura_2_canal_v_despues.png`: brillo ecualizado.

## Justificación simple para la presentación

### Principio óptico

Una cámara oscura funciona porque la luz se propaga en línea recta. Los rayos que
pasan por una abertura pequeña se proyectan sobre un plano interno y forman una
imagen invertida. Si la abertura es más chica, suele mejorar la nitidez porque
entran rayos más controlados, pero también entra menos luz. Si la abertura es más
grande, entra más luz, pero la imagen puede verse menos nítida.

### Por qué se ecualiza el canal V

En HSV, el canal `V` representa principalmente el brillo. Al ecualizar solo ese
canal se mejora el contraste y se aprovecha mejor el rango de luces sin cambiar de
forma directa el tono (`H`) ni la saturación (`S`). Esto respeta mejor los colores
originales que ecualizar los canales RGB por separado, porque modificar RGB canal
por canal puede desplazar colores y producir resultados poco naturales.

### Qué puede mejorar

La ecualización del canal `V` puede hacer que aparezcan detalles que antes estaban
muy oscuros o con bajo contraste. En una imagen de cámara oscura esto es útil
porque la captura suele tener poca luz, bajo contraste y pérdida de nitidez.

### Qué información se puede perder

La ecualización no recupera información que no fue capturada. Si una zona quedó
quemada, totalmente negra, movida o muy borrosa, el procesamiento puede remarcar el
problema, pero no reconstruir detalle real. También puede aumentar el ruido visible
en sombras.

### Limitaciones de la cámara oscura

Las limitaciones principales son: entra poca luz, la imagen queda invertida, la
nitidez depende mucho del tamaño de la abertura y cualquier movimiento puede hacer
que el resultado se vea borroso. Por eso el postproceso ayuda a mejorar la lectura,
pero no reemplaza una buena captura.
