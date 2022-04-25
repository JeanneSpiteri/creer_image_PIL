
from PIL import Image, ImageDraw, ImageFont
from screeninfo import get_monitors

img = Image.new(mode="RGB", size=(get_monitors()[0].width, get_monitors()[0].height), color=(0, 0, 0))

print(img.size)
height = str(img.height) # img.size[1]
width = str(img.width)# img.size[0]
print(f"La hauteur est {height}")
print(f"La longueur est {width}")

WHITE = (255, 255, 255, 0)

draw = ImageDraw.Draw(img)
draw.line((11*img.size[0]/24, img.size[1]/2, 13*img.size[0]/24, img.size[1]/2), fill=WHITE, width=5)
draw.line((img.size[0]/2, img.size[1]/2 - img.size[0]/24, img.size[0]/2, img.size[1]/2 + img.size[0]/24), fill=WHITE, width=5)

img.save(f"img/img_test_cross.png")
