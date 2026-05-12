#!/usr/bin/env python3
"""
Parte 1 — Cámara oscura y procesamiento digital.

Este script procesa la imagen capturada con la cámara oscura siguiendo la
consigna del TP:

1. Lee la imagen original de cámara oscura.
2. Convierte de BGR a HSV.
3. Separa los canales H, S y V.
4. Ecualiza únicamente el canal V, que representa el brillo/valor.
5. Recompone la imagen en HSV.
6. Vuelve a BGR para guardar el resultado.
7. Genera histogramas antes/después del canal V.

Nombres esperados para la Parte 1:
- camara_oscura_1: foto del dispositivo construido.
- camara_oscura_2: segunda foto del dispositivo/artefacto.
- img_camara_oscura_2: imagen producida por la cámara oscura que se procesa.

Ejemplo de uso desde la raíz del repositorio:
python "006_fotografia_digital/codigo/ecualizacion_hsv.py"

Si el archivo tiene otro nombre o extensión:
python "006_fotografia_digital/codigo/ecualizacion_hsv.py" \
  --entrada "006_fotografia_digital/imagenes/originales/img_camara_oscura_2.jpg"
"""

from __future__ import annotations

import argparse
from pathlib import Path

import cv2
import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt


BASE_DIR = Path(__file__).resolve().parents[1]
ORIGINALES_DIR = BASE_DIR / "imagenes" / "originales"
PROCESADAS_DIR = BASE_DIR / "imagenes" / "procesadas"
NOMBRE_IMAGEN_CAMARA_OSCURA = "img_camara_oscura_2"
EXTENSIONES_VALIDAS = (".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tif", ".tiff")


def buscar_imagen_por_nombre(carpeta: Path, nombre_base: str) -> Path:
    """Busca una imagen por nombre base aceptando extensiones habituales."""
    for extension in EXTENSIONES_VALIDAS:
        ruta = carpeta / f"{nombre_base}{extension}"
        if ruta.exists():
            return ruta

    extensiones = ", ".join(EXTENSIONES_VALIDAS)
    raise FileNotFoundError(
        f"No se encontró '{nombre_base}' en {carpeta}. "
        f"Guardá la foto como {nombre_base}.jpg/png/etc. "
        f"Extensiones aceptadas: {extensiones}."
    )


def leer_imagen_bgr(ruta: Path) -> np.ndarray:
    """Lee una imagen con OpenCV y valida que el archivo sea usable."""
    imagen = cv2.imread(str(ruta), cv2.IMREAD_COLOR)
    if imagen is None:
        raise ValueError(f"OpenCV no pudo leer la imagen: {ruta}")
    return imagen


def ecualizar_valor_hsv(imagen_bgr: np.ndarray) -> dict[str, np.ndarray]:
    """Ecualiza solo el canal V y devuelve las etapas necesarias para explicar el proceso."""
    hsv = cv2.cvtColor(imagen_bgr, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    v_ecualizado = cv2.equalizeHist(v)
    hsv_ecualizado = cv2.merge([h, s, v_ecualizado])
    imagen_ecualizada_bgr = cv2.cvtColor(hsv_ecualizado, cv2.COLOR_HSV2BGR)

    return {
        "h": h,
        "s": s,
        "v_antes": v,
        "v_despues": v_ecualizado,
        "imagen_ecualizada_bgr": imagen_ecualizada_bgr,
    }


def guardar_canales(etapas: dict[str, np.ndarray], carpeta_salida: Path, prefijo: str) -> None:
    """Guarda los canales H, S y V para el anexo técnico de la presentación."""
    cv2.imwrite(str(carpeta_salida / f"{prefijo}_canal_h.png"), etapas["h"])
    cv2.imwrite(str(carpeta_salida / f"{prefijo}_canal_s.png"), etapas["s"])
    cv2.imwrite(str(carpeta_salida / f"{prefijo}_canal_v_antes.png"), etapas["v_antes"])
    cv2.imwrite(str(carpeta_salida / f"{prefijo}_canal_v_despues.png"), etapas["v_despues"])


def guardar_histograma(v_antes: np.ndarray, v_despues: np.ndarray, ruta_salida: Path) -> None:
    """Genera un histograma comparativo del canal V antes y después."""
    plt.figure(figsize=(10, 5))
    plt.hist(v_antes.ravel(), bins=256, range=(0, 255), alpha=0.60, label="V original")
    plt.hist(v_despues.ravel(), bins=256, range=(0, 255), alpha=0.60, label="V ecualizado")
    plt.title("Histograma del canal V antes y después de ecualizar")
    plt.xlabel("Intensidad de brillo (0 = negro, 255 = blanco)")
    plt.ylabel("Cantidad de píxeles")
    plt.legend()
    plt.grid(alpha=0.25)
    plt.tight_layout()
    plt.savefig(ruta_salida, dpi=150)
    plt.close()


def guardar_comparacion(imagen_original_bgr: np.ndarray, imagen_ecualizada_bgr: np.ndarray, ruta_salida: Path) -> None:
    """Guarda una comparación lado a lado para usar directamente en la diapositiva."""
    original_rgb = cv2.cvtColor(imagen_original_bgr, cv2.COLOR_BGR2RGB)
    ecualizada_rgb = cv2.cvtColor(imagen_ecualizada_bgr, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.imshow(original_rgb)
    plt.title("Original cámara oscura")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(ecualizada_rgb)
    plt.title("Ecualizada en HSV, solo canal V")
    plt.axis("off")

    plt.tight_layout()
    plt.savefig(ruta_salida, dpi=150)
    plt.close()


def procesar_imagen(entrada: Path, salida_dir: Path, prefijo: str) -> list[Path]:
    """Ejecuta el flujo completo de la Parte 1 y devuelve los archivos generados."""
    salida_dir.mkdir(parents=True, exist_ok=True)

    imagen_bgr = leer_imagen_bgr(entrada)
    etapas = ecualizar_valor_hsv(imagen_bgr)

    salida_ecualizada = salida_dir / f"{prefijo}_ecualizada_hsv_v.png"
    salida_histograma = salida_dir / f"{prefijo}_histograma_v_antes_despues.png"
    salida_comparacion = salida_dir / f"{prefijo}_comparacion_original_ecualizada.png"

    cv2.imwrite(str(salida_ecualizada), etapas["imagen_ecualizada_bgr"])
    guardar_canales(etapas, salida_dir, prefijo)
    guardar_histograma(etapas["v_antes"], etapas["v_despues"], salida_histograma)
    guardar_comparacion(imagen_bgr, etapas["imagen_ecualizada_bgr"], salida_comparacion)

    return [
        salida_ecualizada,
        salida_histograma,
        salida_comparacion,
        salida_dir / f"{prefijo}_canal_h.png",
        salida_dir / f"{prefijo}_canal_s.png",
        salida_dir / f"{prefijo}_canal_v_antes.png",
        salida_dir / f"{prefijo}_canal_v_despues.png",
    ]


def crear_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Ecualiza el canal V de una imagen de cámara oscura en HSV."
    )
    parser.add_argument(
        "--entrada",
        type=Path,
        default=None,
        help=(
            "Ruta de la imagen a procesar. Si se omite, busca "
            f"{NOMBRE_IMAGEN_CAMARA_OSCURA}.* en {ORIGINALES_DIR}."
        ),
    )
    parser.add_argument(
        "--salida-dir",
        type=Path,
        default=PROCESADAS_DIR,
        help="Carpeta donde se guardan la imagen procesada, canales e histogramas.",
    )
    parser.add_argument(
        "--prefijo",
        default=NOMBRE_IMAGEN_CAMARA_OSCURA,
        help="Prefijo para nombrar los archivos generados.",
    )
    return parser


def main() -> None:
    args = crear_parser().parse_args()
    entrada = args.entrada or buscar_imagen_por_nombre(ORIGINALES_DIR, NOMBRE_IMAGEN_CAMARA_OSCURA)
    archivos_generados = procesar_imagen(entrada, args.salida_dir, args.prefijo)

    print("Procesamiento completado.")
    print(f"Imagen de entrada: {entrada}")
    print("Archivos generados:")
    for archivo in archivos_generados:
        print(f"- {archivo}")


if __name__ == "__main__":
    main()
