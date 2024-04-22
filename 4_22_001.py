from PIL import Image
from PIL import ImageDraw

# 画像を円形に切り取る
img1 = Image.open("img.png")
img2 = Image.new("RGB", img1.size, (0xbb, 0xdd, 0xff))
mask = Image.new("1", img1.size, 1)
draw = ImageDraw.Draw(mask)
draw.ellipse((0,0,img1.size[0]-1,img1.size[1]-1), fill=0)
del draw
img3 = Image.composite(img2, img1, mask);

img3.save("circle.png")
