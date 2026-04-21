# Laboratorio de Fundamentos de Procesamiento Digital de Imágenes, Visión por Computadora, VLMs y Agentic AI

**Hacia una Visión Técnico-Humanista: Procesamiento, Algoritmos y Sociedad**

**IFTS Nº 24 — Ciencia de Datos e Inteligencia Artificial**  
**3er año — 1er cuatrimestre 2026**  
**Martes 20:30–22:30 / Miércoles 18:30–22:30**

**Profesor Titular:** Matías Barreto — Especialista en Nuevos Medios e Interactividad  
[matiasbarreto@ifts24.edu.ar](mailto:matiasbarreto@ifts24.edu.ar)

**Ayudante de Trabajos Prácticos:** Cynthia Marcela Villagra

---

## Qué es este repositorio

Este repositorio contiene el material de laboratorio de la materia. El material se organiza en carpetas numeradas y tituladas (`001 - ...`, `002 - ...`, `003 - ...`, `004 - ...`) que se publican y actualizan a medida que avanza la cursada.

Cada carpeta corresponde a una unidad temática y contiene notebooks (`.ipynb`) y scripts (`.py`) para trabajar en clase y fuera de ella.

**Librerías principales del curso:**
- **OpenCV (cv2):** Procesamiento de imágenes y visión computacional
- **NumPy:** Manipulación de matrices y arrays
- **Matplotlib:** Visualización de imágenes y gráficos
- **Pillow (PIL):** Manipulación básica de imágenes
- **scikit-image:** Algoritmos avanzados de procesamiento
- **py5:** Introducción a conceptos visuales (unidades iniciales únicamente)

---

## Importante: No necesitás permisos de administrador

Si trabajás en una computadora de tu empleo o no tenés permisos de admin, **esto no es un problema**. Todo el software se instala dentro de una carpeta del proyecto usando un **entorno virtual de Python**.

El entorno virtual es una instalación aislada de Python que:
- No requiere permisos de administrador
- No modifica el Python del sistema
- Todo queda dentro de la carpeta del repositorio
- Podés borrarlo y recrearlo cuando quieras

---

## Requisitos previos

Antes de arrancar, asegurate de tener instalado en tu máquina:

1. **Python 3.10 o superior** — [Descarga oficial](https://www.python.org/downloads/)
   - Durante la instalación en Windows, marcá la opción **"Add Python to PATH"**
   - **No necesitás "Install for all users"** — la instalación para tu usuario actual funciona perfectamente
2. **Git** — [Descarga oficial](https://git-scm.com/downloads)
   - Elegí la opción "Git from the command line and also from 3rd-party software"
3. **Visual Studio Code** (recomendado) — [Descarga oficial](https://code.visualstudio.com/)
   - Instalá la extensión **Python** desde el marketplace de VS Code
   - Instalá la extensión **Jupyter** para trabajar con notebooks

**Alternativa si no podés instalar nada:** Usá [Google Colab](https://colab.research.google.com) directamente. Para los notebooks que usan imágenes locales, asegurate de subir también la carpeta `Imagenes/` correspondiente o de montar el repositorio completo.

---

## Setup inicial (una sola vez)

Abrí una terminal (en Windows: PowerShell o Git Bash) y ejecutá los siguientes comandos:

### 1. Clonar el repositorio

```bash
git clone https://github.com/mattbarreto/ifts24-lab-pdi-2026.git
cd ifts24-lab-pdi-2026
```

### 2. Crear el entorno virtual

```bash
python -m venv .venv
```

Esto crea una carpeta `.venv/` dentro del proyecto con una instalación limpia de Python.

### 3. Activar el entorno virtual

**Windows (PowerShell):**
```powershell
.venv\Scripts\Activate.ps1
```

**Windows (Git Bash / CMD):**
```bash
.venv\Scripts\activate
```

**macOS / Linux:**
```bash
source .venv/bin/activate
```

Si PowerShell muestra un error de permisos, ejecutá primero (solo una vez en tu usuario):
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Cuando el entorno esté activo, verás `(.venv)` al principio de la línea de la terminal.

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 5. Verificar la instalación

```bash
python -c "import cv2; import numpy; print('OpenCV y NumPy instalados correctamente')"
```

---

## Cómo actualizar cada semana

Cada vez que se publique material nuevo, desde la carpeta del repositorio ejecutá:

```bash
git pull
```

Si se agregan nuevas dependencias, se anunciará en clase. En ese caso, con el entorno activado:

```bash
pip install -r requirements.txt
```

---

## Estructura del repositorio

```
ifts24-lab-pdi-2026/
├── README.md                    <- Este archivo
├── requirements.txt             <- Dependencias del entorno
├── .gitignore                   <- Archivos ignorados por git
│
├── 001 - py5/                   <- Unidad inicial con ejercicios py5
│   ├── *.py
│   ├── img/
│   └── save/
│
├── 002 - py5/                   <- Fundamentos teóricos y laboratorio con py5
│   ├── 00_setup_colab.ipynb
│   ├── 02a_fundamentos_teoria_colab.ipynb
│   ├── 02a_fundamentos_teoria_local.ipynb
│   ├── 02b_fundamentos_practica_local.ipynb
│   └── 02c_laboratorio_fundamentos.ipynb
│
├── 003 - librerias_fundamentos_pdi/   <- NumPy, OpenCV y prácticas guiadas de PDI
│   ├── 001 - entorno y librerias.ipynb
│   ├── 002 - imagenes en color y canales.ipynb
│   ├── ...
│   └── 008 - actividad integradora - segmentacion por color.ipynb
│
├── 004 - openCV/                <- Bloque OpenCV reorganizado en secuencia plana
│   ├── 001 - introduccion a opencv y espacios de color.ipynb
│   ├── 002 - formatos de archivos de imagen.ipynb
│   ├── 003 - mejora de imagen y ecualizacion basica.ipynb
│   ├── 004 - comparacion de estrategias de ecualizacion.ipynb
│   ├── 004b - operaciones basicas con imagenes.ipynb
│   ├── 005 - transformaciones geometricas y cambio de perspectiva.ipynb
│   ├── 006 - operaciones graficas y anotacion visual.ipynb
│   ├── 006b - filtros de suavizado y reduccion de ruido.ipynb
│   ├── 006b2 - umbralizacion global, Otsu y adaptive threshold.ipynb
│   ├── 006c - morfologia matematica para limpieza de mascaras.ipynb
│   ├── 006d - restauracion y algoritmos de inpainting.ipynb
│   ├── 007 - deteccion de contornos.ipynb
│   ├── 008 - propiedades geometricas de contornos.ipynb
│   ├── 009 - coincidencia por plantilla.ipynb
│   ├── 010 - deteccion de rostros con haar.ipynb
│   ├── Utilidades_y_Plantillas.ipynb     <- Caja de herramientas reutilizable para la unidad y el TPI
│   └── Imagenes/
│
└── 005 - TFI_1/                 <- Trabajo final integrador de mejora y restauracion
    ├── TFI_1 - mejora y restauracion de imagenes.ipynb
    └── TFI_1_Consigna_y_Rubrica.md
```

---

## Cómo ejecutar los ejercicios

### Opción A: Trabajo local con VS Code (recomendado)

1. Abrí la carpeta del repositorio en VS Code: `Archivo > Abrir carpeta...`
2. Asegurate de tener el entorno virtual activado (ver `.venv` en la barra de estado de VS Code)
3. Abrí cualquier archivo `.py` o `.ipynb`
4. Para scripts `.py`: presioná `F5` o el botón de play
5. Para notebooks `.ipynb`: ejecutá las celdas con `Shift + Enter`

### Opción B: Google Colab (sin instalación)

1. Andá a [Google Colab](https://colab.research.google.com)
2. Subí el notebook `.ipynb` que querés ejecutar
3. Si el cuaderno usa recursos locales, subí también la carpeta `Imagenes/` de esa unidad
4. Los notebooks pueden requerir ajustar rutas según cómo quede montado el material en Colab

---

## Resolución de problemas frecuentes

### "No se puede cargar el script porque la ejecución de scripts está deshabilitada en este sistema"
Ejecutá en PowerShell como administrador (solo una vez):
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### "python no se reconoce como comando"
Python no se agregó al PATH. Reinstalá marcando "Add Python to PATH", o usá `py` en lugar de `python` en Windows.

### "No module named 'cv2'" / "No module named 'numpy'"
Verificá que el entorno virtual esté activado (debés ver `(.venv)` al inicio de la línea). Si lo está, reinstalá las dependencias:
```bash
pip install -r requirements.txt
```

### Las imágenes no se cargan (error al leer imágenes)
Verificá que:
1. Las imágenes estén en la carpeta correspondiente
2. Estés ejecutando el script desde la carpeta correcta
3. Usás rutas relativas: `img/mi_imagen.jpg` o `Imagenes/mi_imagen.jpg` en lugar de rutas absolutas

### py5 no abre la ventana o no muestra la imagen
En algunos sistemas operativos, py5 requiere un backend gráfico adicional. Instalá glfw:
```bash
pip install glfw
```
Si el problema persiste, consultá la [guía de instalación de py5](https://py5coding.org/content/install.html) que detalla los requisitos específicos para cada sistema operativo.

### Error de Java al ejecutar py5
py5 requiere Java para funcionar. Si ves un error relacionado con Java, instalá la versión apropiada según tu sistema operativo siguiendo las [instrucciones oficiales de instalación de py5](https://py5coding.org/content/install.html).

---

## Recursos adicionales

- [Documentación de OpenCV](https://docs.opencv.org/)
- [Documentación de NumPy](https://numpy.org/doc/)
- [Documentación de Matplotlib](https://matplotlib.org/)
- [Documentación de scikit-image](https://scikit-image.org/docs/)
- [Documentación de py5](https://py5coding.org/)
- [Guía de instalación de py5 (incluye requisitos de Java)](https://py5coding.org/content/install.html)
- [Google Colab Help](https://colab.research.google.com/notebooks/intro.ipynb)

---

## Licencia

Este material se distribuye bajo licencia [Creative Commons BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es): podés usarlo y adaptarlo con atribución, sin fines comerciales, y compartiendo bajo la misma licencia.
