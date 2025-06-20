

import requests
import cairosvg
from PIL import Image
import io

# URL do SVG
svg_url = 'https://wellingtonpawlino.github.io/pandas/github-contribution-grid-snake.svg'

# Baixar o SVG
response = requests.get(svg_url)
svg_data = response.content

# Converter SVG para PNG
png_data = cairosvg.svg2png(bytestring=svg_data)

# Abrir PNG com Pillow
png_image = Image.open(io.BytesIO(png_data))

# Salvar como GIF
png_image.save("snake_animation.gif", save_all=True, append_images=[png_image], loop=0, duration=500)

print("GIF animado salvo como snake_animation.gif")

