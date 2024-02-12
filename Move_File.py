import os
import shutil
fromdir="C:/Users/kk/Downloads/new"
todir="C:/Users/kk/Downloads/new"

listOfFiles=os.listdir("C:/Users/kk/Downloads")
print(listOfFiles)

for fileName in listOfFiles:
  name,extenction=os.path.splitext(fileName)
  if extenction == "":
    continue
  if extenction in [".gif",".png",".jpg",".jpeg",".jfif"]:
    path1=fromdir+"/"+fileName
    path2=todir+"/"+"imageFiles"
    path3=todir+"/"+"imageFiles"+"/"+fileName

    if os.path.exists(path2):
      print("moving"+fileName+"...")
      shutil.move(path1,path3)
    else:
      os.makedirs(path2)
      print("moving"+fileName+"...")
      shutil.move(path1,path3)
