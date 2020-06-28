from PIL import Image,ImageFilter

img = Image.open('pokedez\pikachu.jpg')
box = (100,100,200,200)
filtered_img = img.crop(box)
croked = filtered_img.rotate(90)
croked.save(r"pokedez\truned","png")