# Guía Completa de PIL (Pillow)

## Tabla de Contenidos
1. [Introducción](#introducción)
2. [Instalación](#instalación)
3. [Conceptos Básicos](#conceptos-básicos)
    - [Abrir y Mostrar una Imagen](#abrir-y-mostrar-una-imagen)
    - [Guardar una Imagen](#guardar-una-imagen)
    - [Redimensionar una Imagen](#redimensionar-una-imagen)
    - [Recortar una Imagen](#recortar-una-imagen)
    - [Rotar y Voltear una Imagen](#rotar-y-voltear-una-imagen)
    - [Aplicar Filtros](#aplicar-filtros)
    - [Ajustar Brillo, Contraste y Otros](#ajustar-brillo-contraste-y-otros)
    - [Convertir a Escala de Grises](#convertir-a-escala-de-grises)
    - [Crear Thumbnails](#crear-thumbnails)
    - [Superponer Imágenes](#superponer-imágenes)
    - [Añadir Texto](#añadir-texto)
    - [Convertir a Otros Formatos](#convertir-a-otros-formatos)
    - [Manejar Transparencia](#manejar-transparencia)
    - [Crear Nuevas Imágenes](#crear-nuevas-imágenes)
4. [Compresión de Imágenes](#compresión-de-imágenes)
    - [Compresión JPEG](#compresión-jpeg)
    - [Compresión PNG](#compresión-png)
    - [Compresión WebP](#compresión-webp)
5. [Formatos Compatibles](#formatos-compatibles)
    - [Formatos Soportados para Abrir y Manipular](#formatos-soportados-para-abrir-y-manipular)
    - [Formatos a los que se Puede Convertir](#formatos-a-los-que-se-puede-convertir)
    - [Formatos que se Pueden Comprimir](#formatos-que-se-pueden-comprimir)
6. [Curiosidades y Funcionalidades Avanzadas](#curiosidades-y-funcionalidades-avanzadas)
    - [Modo Thumbnail con Antialiasing](#modo-thumbnail-con-antialiasing)
    - [Crear GIFs Animados](#crear-gifs-animados)
    - [Filtros Personalizados](#filtros-personalizados)
    - [Trabajar con Exif](#trabajar-con-exif)
    - [Mosaicos y Collages](#mosaicos-y-collages)
7. [Recursos Adicionales](#recursos-adicionales)

## Introducción

Pillow es una biblioteca de Python para abrir, manipular y guardar archivos de imagen. Es una bifurcación amigable de PIL (Python Imaging Library). Esta guía te ayudará a comenzar con Pillow, cubriendo los conceptos básicos y algunos trucos avanzados.

## Instalación

Para instalar Pillow, utiliza `pip`:

```bash
pip install pillow
```

## Conceptos Básicos

### Abrir y Mostrar una Imagen

Para abrir una imagen, utiliza el método `open`:

```python
from PIL import Image

imagen = Image.open("ruta/a/tu/imagen.jpg")
imagen.show()
```

### Guardar una Imagen

Para guardar una imagen en un nuevo archivo, usa el método `save`:

```python
imagen.save("ruta/a/guardar/nueva_imagen.jpg")
```

### Redimensionar una Imagen

Para cambiar el tamaño de una imagen, usa el método `resize`:

```python
nueva_imagen = imagen.resize((300, 300))
nueva_imagen.show()
```

### Recortar una Imagen

Para recortar una imagen, utiliza el método `crop`:

```python
# Definir el área a recortar: (left, upper, right, lower)
area_recorte = (100, 100, 400, 400)
imagen_recortada = imagen.crop(area_recorte)
imagen_recortada.show()
```

### Rotar y Voltear una Imagen

Para rotar una imagen, usa el método `rotate`:

```python
imagen_rotada = imagen.rotate(45)  # Rotar 45 grados
imagen_rotada.show()
```

Para voltear una imagen, usa `transpose`:

```python
imagen_volteada = imagen.transpose(Image.FLIP_LEFT_RIGHT)  # Voltear horizontalmente
imagen_volteada.show()
```

### Aplicar Filtros

Para aplicar filtros, usa el método `filter` junto con los filtros disponibles en `ImageFilter`:

```python
from PIL import ImageFilter

imagen_con_filtro = imagen.filter(ImageFilter.BLUR)  # Aplicar desenfoque
imagen_con_filtro.show()
```

### Ajustar Brillo, Contraste y Otros

Usa `ImageEnhance` para ajustar el brillo, contraste, nitidez, etc.:

```python
from PIL import ImageEnhance

enhancer = ImageEnhance.Brightness(imagen)
imagen_brillante = enhancer.enhance(1.5)  # Aumentar el brillo en un 50%
imagen_brillante.show()

enhancer = ImageEnhance.Contrast(imagen)
imagen_contraste = enhancer.enhance(2)  # Duplicar el contraste
imagen_contraste.show()
```

### Convertir a Escala de Grises

Para convertir una imagen a escala de grises, usa `convert`:

```python
imagen_grises = imagen.convert("L")
imagen_grises.show()
```

### Crear Thumbnails

Para crear miniaturas rápidamente:

```python
imagen.thumbnail((128, 128))
imagen.show()
```

### Superponer Imágenes

Usa `paste` para superponer una imagen sobre otra:

```python
fondo = Image.open("ruta/a/fondo.jpg")
superposicion = Image.open("ruta/a/superposicion.png")
fondo.paste(superposicion, (50, 50), superposicion)  # El tercer argumento es la máscara de transparencia
fondo.show()
```

### Añadir Texto

Usa `ImageDraw` y `ImageFont` para añadir texto:

```python
from PIL import ImageDraw, ImageFont

imagen = Image.open("ruta/a/tu/imagen.jpg")
draw = ImageDraw.Draw(imagen)
fuente = ImageFont.truetype("ruta/a/fuente.ttf", 40)
draw.text((10, 10), "Hola, Mundo!", font=fuente, fill="white")
imagen.show()
```

### Convertir a Otros Formatos

Para convertir una imagen a otro formato:

```python
imagen.save("ruta/a/nueva_imagen.png", format="PNG")
```

### Manejar Transparencia

Para trabajar con imágenes con transparencia (canal alfa):

```python
imagen_rgba = Image.open("ruta/a/imagen_con_transparencia.png").convert("RGBA")
imagen_rgba.show()
```

### Crear Nuevas Imágenes

Para crear una nueva imagen desde cero:

```python
nueva_imagen = Image.new("RGB", (300, 300), color="red")
nueva_imagen.show()
```

## Compresión de Imágenes

### Compresión JPEG

Para guardar una imagen JPEG con compresión ajustada:

```python
imagen.save("ruta/a/comprimida_imagen.jpg", "JPEG", quality=85)
```

El parámetro `quality` varía de 1 a 95 (por defecto es 75). Un valor más bajo reduce la calidad y el tamaño del archivo.

### Compresión PNG

Para guardar una imagen PNG optimizada:

```python
imagen.save("ruta/a/comprimida_imagen.png", "PNG", optimize=True)
```

El parámetro `optimize` ayuda a reducir el tamaño del archivo.

### Compresión WebP

Para guardar una imagen WebP con compresión ajustada:

```python
imagen.save("ruta/a/comprimida_imagen.webp", "WebP", quality=85)
```

El parámetro `quality` varía de 1 a 100. Un valor más bajo reduce la calidad y el tamaño del archivo.

## Formatos Compatibles

### Formatos Soportados para Abrir y Manipular

- BMP
- DIB
- EPS
- GIF
- ICNS
- ICO
- IM
- JPEG
- JPG
- MSP
- PCX
- PNG
- PPM
- SGI
- SPIDER
- TGA
- TIFF
- WebP
- XBM

### Formatos a los que se Puede Convertir

- BMP
- DIB
- EPS
- GIF
- ICNS
- ICO
- IM
- JPEG
- JPG
- MSP
- PCX
- PNG
- PPM
- SGI
- TGA
- TIFF
- WebP
- XBM

### Formatos que se Pueden Comprimir

- **JPEG**
  ```python
  imagen.save("ruta/a/comprimida_imagen.jpg", "JPEG", quality=85)
  ```
- **PNG**
  ```python
  imagen.save("ruta/a/comprimida_imagen.png", "PNG", optimize=True)
  ```
- **WebP**
  ```python
  imagen.save("ruta/a/comprimida_imagen.webp", "WebP", quality=85)
  ```

## Curiosidades y Funcionalidades Avanzadas

```markdown
### Modo Thumbnail con Antialiasing

Para crear miniaturas con antialiasing (mejor calidad):

```python
imagen.thumbnail((128, 128), Image.ANTIALIAS)
imagen.show()
```

### Crear GIFs Animados

Para crear un GIF animado a partir de múltiples imágenes:

```python
imagenes = [Image.open(f"ruta/a/imagen_{i}.png") for i in range(10)]
imagenes[0].save("ruta/a/animacion.gif", save_all=True, append_images=imagenes[1:], duration=100, loop=0)
```

### Filtros Personalizados

Para crear y aplicar un filtro personalizado:

```python
from PIL import ImageFilter

class MiFiltro(ImageFilter.BuiltinFilter):
    name = "MiFiltro"
    filterargs = (3, 3), 1, 0, (
        -1, -1, -1,
        -1,  8, -1,
        -1, -1, -1
    )

imagen_con_filtro_personalizado = imagen.filter(MiFiltro())
imagen_con_filtro_personalizado.show()
```

### Trabajar con Exif

Para leer y modificar datos EXIF (metadata de las imágenes):

```python
exif_data = imagen._getexif()
for tag, value in exif_data.items():
    print(f"{tag}: {value}")
```

### Mosaicos y Collages

Para crear un mosaico o collage de imágenes:

```python
imagenes = [Image.open(f"ruta/a/imagen_{i}.jpg") for i in range(4)]
anchura_total = sum(imagen.size[0] for imagen in imagenes)
altura_max = max(imagen.size[1] for imagen in imagenes)

mosaico = Image.new('RGB', (anchura_total, altura_max))

x_offset = 0
for imagen in imagenes:
    mosaico.paste(imagen, (x_offset, 0))
    x_offset += imagen.size[0]

mosaico.show()
```

## Recursos Adicionales

Para más información, consulta la [documentación oficial de Pillow](https://pillow.readthedocs.io/en/stable/).

---

Este README proporciona una guía detallada para comenzar a usar Pillow en Python, cubriendo desde los conceptos básicos hasta las funcionalidades más avanzadas. Con esta guía, deberías ser capaz de abrir, manipular, guardar y comprimir imágenes, así como explorar algunas de las capacidades más avanzadas de Pillow.