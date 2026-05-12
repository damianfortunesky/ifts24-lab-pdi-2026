"""Genera recursos para la Parte 2 del TP de fotografía digital.

El script toma las fotos `img_p2_0*.jpg` guardadas en
`006_fotografia_digital/imagenes/originales/` y produce imágenes listas para
armar las diapositivas 4, 5 y 6 de la presentación:

- simplicidad visual: versión en escala de grises de la última foto;
- reencuadre: dos recortes de la primera foto y una copia con regiones marcadas;
- punto de vista: comparación entre dos tomas del mismo sujeto.

La diapositiva 7 no se procesa porque la consigna solicitó resolver la Parte 2
menos "Fotografía basada en la luz".
"""

from __future__ import annotations

import argparse
import shutil
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageDraw, ImageOps

BASE_DIR = Path(__file__).resolve().parents[1]
ORIGINALES_DIR = BASE_DIR / "imagenes" / "originales"
PROCESADAS_DIR = BASE_DIR / "imagenes" / "procesadas"
PATRON_IMAGENES_PARTE_2 = "img_p2_0*"
EXTENSIONES_VALIDAS = {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tif", ".tiff"}


@dataclass(frozen=True)
class CajaRelativa:
    """Caja de recorte expresada como porcentajes de ancho y alto."""

    izquierda: float
    arriba: float
    derecha: float
    abajo: float

    def a_pixeles(self, ancho: int, alto: int) -> tuple[int, int, int, int]:
        """Convierte la caja relativa a coordenadas enteras de Pillow."""
        return (
            int(ancho * self.izquierda),
            int(alto * self.arriba),
            int(ancho * self.derecha),
            int(alto * self.abajo),
        )


# Recortes iniciales pensados para un sujeto centrado en un sillón.
# Si una toma queda desplazada, se pueden ajustar estas proporciones desde el código.
CROP_A_ROSTRO_CUERPO = CajaRelativa(0.22, 0.10, 0.78, 0.82)
CROP_B_SILLON_MANTA = CajaRelativa(0.08, 0.08, 0.92, 0.92)


def listar_imagenes_parte_2(carpeta: Path) -> list[Path]:
    """Busca las imágenes originales de Parte 2 y las devuelve ordenadas."""
    imagenes = sorted(
        ruta
        for ruta in carpeta.glob(PATRON_IMAGENES_PARTE_2)
        if ruta.is_file() and ruta.suffix.lower() in EXTENSIONES_VALIDAS
    )
    if not imagenes:
        extensiones = ", ".join(sorted(EXTENSIONES_VALIDAS))
        raise FileNotFoundError(
            f"No se encontraron imágenes '{PATRON_IMAGENES_PARTE_2}' en {carpeta}. "
            "Guardá allí las fotos de la Parte 2, por ejemplo img_p2_01.jpg, "
            f"img_p2_02.jpg, etc. Extensiones aceptadas: {extensiones}."
        )
    return imagenes


def abrir_rgb(ruta: Path) -> Image.Image:
    """Abre una imagen y normaliza el modo a RGB."""
    return Image.open(ruta).convert("RGB")


def guardar_escala_grises(entrada: Path, salida: Path) -> None:
    """Convierte una imagen a escala de grises y la guarda como RGB."""
    imagen = abrir_rgb(entrada)
    gris = ImageOps.grayscale(imagen).convert("RGB")
    gris.save(salida)


def recortar(entrada: Path, caja: CajaRelativa, salida: Path) -> tuple[int, int, int, int]:
    """Recorta la imagen según una caja relativa y devuelve la caja en píxeles."""
    imagen = abrir_rgb(entrada)
    caja_px = caja.a_pixeles(*imagen.size)
    imagen.crop(caja_px).save(salida)
    return caja_px


def guardar_original_con_marcas(
    entrada: Path,
    caja_a: tuple[int, int, int, int],
    caja_b: tuple[int, int, int, int],
    salida: Path,
) -> None:
    """Dibuja las regiones de reencuadre sobre la foto amplia original."""
    imagen = abrir_rgb(entrada)
    dibujo = ImageDraw.Draw(imagen)
    ancho_linea = max(4, imagen.width // 180)

    dibujo.rectangle(caja_a, outline=(255, 70, 70), width=ancho_linea)
    dibujo.text((caja_a[0] + 10, caja_a[1] + 10), "Recorte A", fill=(255, 70, 70))

    dibujo.rectangle(caja_b, outline=(70, 140, 255), width=ancho_linea)
    dibujo.text((caja_b[0] + 10, caja_b[1] + 40), "Recorte B", fill=(70, 140, 255))

    imagen.save(salida)


def guardar_comparacion_horizontal(imagenes: list[Path], titulos: list[str], salida: Path) -> None:
    """Crea una lámina horizontal simple para comparar imágenes."""
    abiertas = [abrir_rgb(ruta) for ruta in imagenes]
    alto_objetivo = 900
    margen = 40
    alto_titulo = 70

    redimensionadas: list[Image.Image] = []
    for imagen in abiertas:
        escala = alto_objetivo / imagen.height
        nuevo_ancho = int(imagen.width * escala)
        redimensionadas.append(imagen.resize((nuevo_ancho, alto_objetivo), Image.Resampling.LANCZOS))

    ancho_total = sum(img.width for img in redimensionadas) + margen * (len(redimensionadas) + 1)
    alto_total = alto_objetivo + alto_titulo + margen * 2
    lienzo = Image.new("RGB", (ancho_total, alto_total), "white")
    dibujo = ImageDraw.Draw(lienzo)

    x = margen
    for imagen, titulo in zip(redimensionadas, titulos, strict=True):
        dibujo.text((x, margen // 2), titulo, fill="black")
        lienzo.paste(imagen, (x, alto_titulo))
        x += imagen.width + margen

    lienzo.save(salida)


def copiar_imagen(entrada: Path, salida: Path) -> None:
    """Copia una imagen original preservando su contenido."""
    shutil.copy2(entrada, salida)


def seleccionar_vista_b(imagenes: list[Path]) -> Path:
    """Elige la cuarta foto si existe; si no, la última disponible."""
    if len(imagenes) >= 4:
        return imagenes[3]
    return imagenes[-1]


def procesar_parte_2(carpeta_entrada: Path, carpeta_salida: Path) -> list[Path]:
    """Genera todos los recursos solicitados para las diapositivas 4, 5 y 6."""
    imagenes = listar_imagenes_parte_2(carpeta_entrada)
    carpeta_salida.mkdir(parents=True, exist_ok=True)

    foto_amplia = imagenes[0]
    foto_simplicidad = imagenes[-1]
    foto_vista_b = seleccionar_vista_b(imagenes)

    salida_simplicidad_original = carpeta_salida / "p2_diap_04_simplicidad_original.jpg"
    salida_simplicidad_gris = carpeta_salida / "p2_diap_04_simplicidad_final_grises.jpg"

    salida_reencuadre_marcado = carpeta_salida / "p2_diap_05_original_con_recortes.jpg"
    salida_crop_a = carpeta_salida / "p2_diap_05_recorte_a_gato.jpg"
    salida_crop_b = carpeta_salida / "p2_diap_05_recorte_b_contexto.jpg"
    salida_reencuadre_comparacion = carpeta_salida / "p2_diap_05_comparacion_reencuadres.jpg"

    salida_vista_a = carpeta_salida / "p2_diap_06_vista_a_desde_arriba.jpg"
    salida_vista_b = carpeta_salida / "p2_diap_06_vista_b_contextual.jpg"
    salida_vistas_comparacion = carpeta_salida / "p2_diap_06_comparacion_punto_de_vista.jpg"

    copiar_imagen(foto_simplicidad, salida_simplicidad_original)
    guardar_escala_grises(foto_simplicidad, salida_simplicidad_gris)

    caja_a = recortar(foto_amplia, CROP_A_ROSTRO_CUERPO, salida_crop_a)
    caja_b = recortar(foto_amplia, CROP_B_SILLON_MANTA, salida_crop_b)
    guardar_original_con_marcas(foto_amplia, caja_a, caja_b, salida_reencuadre_marcado)
    guardar_comparacion_horizontal(
        [salida_reencuadre_marcado, salida_crop_a, salida_crop_b],
        ["Original con marcas", "Recorte A: gato", "Recorte B: contexto"],
        salida_reencuadre_comparacion,
    )

    copiar_imagen(foto_amplia, salida_vista_a)
    copiar_imagen(foto_vista_b, salida_vista_b)
    guardar_comparacion_horizontal(
        [salida_vista_a, salida_vista_b],
        ["Vista A: superior/cercana", "Vista B: frontal o contextual"],
        salida_vistas_comparacion,
    )

    return [
        salida_simplicidad_original,
        salida_simplicidad_gris,
        salida_reencuadre_marcado,
        salida_crop_a,
        salida_crop_b,
        salida_reencuadre_comparacion,
        salida_vista_a,
        salida_vista_b,
        salida_vistas_comparacion,
    ]


def crear_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Genera recursos procesados para Parte 2, diapositivas 4 a 6."
    )
    parser.add_argument(
        "--entrada-dir",
        type=Path,
        default=ORIGINALES_DIR,
        help="Carpeta con img_p2_0*.jpg/png/etc.",
    )
    parser.add_argument(
        "--salida-dir",
        type=Path,
        default=PROCESADAS_DIR,
        help="Carpeta donde se guardan las imágenes procesadas.",
    )
    return parser


def main() -> None:
    args = crear_parser().parse_args()
    archivos = procesar_parte_2(args.entrada_dir, args.salida_dir)

    print("Procesamiento de Parte 2 completado.")
    print("Archivos generados:")
    for archivo in archivos:
        print(f"- {archivo}")


if __name__ == "__main__":
    main()
