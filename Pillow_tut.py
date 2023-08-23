from PIL import Image

img1=Image.open(r"D:\Python Practice\wall.jpg")
img2=Image.open(r"D:\Python Practice\wall2.jpg")
# img.show()
# img=Image.new("RGB",(400,400),(255,255,0))
# img.show()
# img=img.rotate(angle=60,expand=True,fillcolor="green")
# print(img.height,img.width)
# img.show()
# img=img.resize((int(img.width/2),int(img.height/2)))
# print(img.height,img.width)
# img=img.crop(box=(100,100,200,200))
img=Image.blend(img1,img2,alpha=0.5)
img.show()

