"""Generuje tło slajdu tytułowego (tlo.png).

Portret fazowy (domain coloring) funkcji
    f(z) = (z^2 - 1)(z - 2 - i)^2 / (z^2 + 2 + 2i).
Kolor koduje argument f(z), jasność - poziomice log_2 |f(z)|.

Użycie:  python scripts/tlo.py   (zapisuje tlo.png w bieżącym katalogu)
Wymaga: numpy, matplotlib, pillow.
"""
import numpy as np
import matplotlib.colors as mc
from PIL import Image

W, H = 1600, 900


def render(f, xr, yr, name):
    x = np.linspace(*xr, W)
    y = np.linspace(*yr, H)[::-1]
    Z = x[None, :] + 1j * y[:, None]
    F = f(Z)
    arg = (np.angle(F) / (2 * np.pi)) % 1.0
    frac = (np.log(np.abs(F) + 1e-12) / np.log(2)) % 1.0
    v = 0.70 + 0.30 * frac
    s = np.full_like(arg, 0.75)
    rgb = mc.hsv_to_rgb(np.dstack([arg, s, v]))
    Image.fromarray((rgb * 255).astype(np.uint8)).save(name)


if __name__ == "__main__":
    render(lambda z: (z**2 - 1) * (z - 2 - 1j) ** 2 / (z**2 + 2 + 2j),
           (-3.2, 3.2), (-1.8, 1.8), "tlo.png")
