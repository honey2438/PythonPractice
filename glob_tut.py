import glob
from PIL import Image

path=f"D:\MagicVsCode\input-sample"

files = glob.glob(path + '/*.jpg')

print(files)

for img in files:
    Image.open(img).rotate(angle=90,expand=True).show()
    