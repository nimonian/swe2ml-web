from PIL import Image
from pathlib import Path
from pycode.models.vector import Vector

images = Path(__file__).parent / "images"

im9a = Image.open(images / "mnist_9a.png")
im9b = Image.open(images / "mnist_9b.png")
im5 = Image.open(images / "mnist_5.png")

v9a = Vector(*im9a.getdata())
v9b = Vector(*im9b.getdata())
v5 = Vector(*im5.getdata())

print(v9a)
