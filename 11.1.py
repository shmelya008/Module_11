from PIL import Image
from PIL import ImageEnhance

im = Image.open('_6gZWeFoDFE.jpg')


# Вывод информации об изображении:
print(im.format, im.size, im.mode)

im.show()

# Вырезание и поворот секции в изображении:
box = (80, 30, 400, 350)
region = im.crop(box)
region = region.transpose(Image.Transpose.ROTATE_180)

# Изменение режима отображения (RGB to L)
region = region.convert("L")
im.paste(region, box)

# Разделение и слияние полос (RGB) в изображении:
r, g, b = im.split()
im = Image.merge("RGB", (b, r, g))

# Изменение контраста изображения
enh = ImageEnhance.Contrast(im)
enh.enhance(1.2).show()

im.show()
