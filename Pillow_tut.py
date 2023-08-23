from PIL import Image

img=Image.open(r"D:\Python Practice\wall.jpg")
# img.show()
# img=Image.new("RGB",(400,400),(255,255,0))
# img.show()
# img=img.rotate(angle=60,expand=True,fillcolor="green")
print(img.height,img.width)
img.show()
img=img.resize((int(img.width/2),int(img.height/2)))
print(img.height,img.width)
img.show()

