from PIL import Image, ImageDraw

image = Image.new('RGB', (500, 500), color='red')
draw = ImageDraw.Draw(image)

#image.save('image.png')
image.show()