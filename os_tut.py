import os
import shutil
print(os.getcwd())

if not os.path.exists("movies"):
    os.mkdir("movies")

if not os.path.exists("new.py"):
    open("new.py","x").close

# os.chdir("D:\Python Practice\FirstProgram")
if not os.path.exists("movies"):
    os.mkdir("movies")
# print(os.listdir(r"D:\javascript"))

for file in os.listdir(r"D:\javascript"):
    pass
    # print(file)
    # print(os.path.join(os.getcwd(),file))

# os.chdir("D:\Python Practice")
# shutil.move("wall2.jpg","FirstProgram\wall.jpg")
# os.remove("new.py")
# os.chdir("D:\Python Practice")
# print(os.getcwd())
# os.remove("new.py")
# folderIter=os.walk("D:\Python Practice")
# for current_dir,folders,files in folderIter:
#     print("Current Directory: ",current_dir)
#     print("Folders: ",folders)
#     print("Files: ",files)
os.rename("movies","songs")



