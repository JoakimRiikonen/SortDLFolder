import os

# change path as necessary
PATH = 'C:\\Users\\Joakim Riikonen\\Downloads'

# folder names
appsFolder = "apps"
archivesFolder = "archives"
documentsFolder = "documents"
mediaFolder = "media"

# what goes where
appsFiles = (".exe", ".msi", ".air", ".bat", ".dll")
archivesFiles = (".zip", ".rar", ".7z", ".gz")
documentsFiles = (".csv", ".docx", ".html", ".pdf", ".txt")
mediaFiles = (".gif", ".jpg", ".png", ".webm", ".gifv")

try:
    os.chdir(PATH)
except FileNotFoundError:
    print("Download folder not found, check the user variable/set the path yourself")
    quit()

# get list of files
dirlist = os.listdir()

# ----Create folders if neccessary---

if(not appsFolder in dirlist):
    print("Creating folder apps")
    os.mkdir(appsFolder)

if(not archivesFolder in dirlist):
    print("Creating folder archives")
    os.mkdir(archivesFolder)

if(not documentsFolder in dirlist):
    print("Creating folder documents")
    os.mkdir(documentsFolder)

if(not mediaFolder in dirlist):
    print("Creating folder media")
    os.mkdir(mediaFolder)

# ----sort the files----

for name in dirlist:
    # apps
    if name.endswith(appsFiles):
        destination = appsFolder + "/" + name
        print(destination)
        os.rename(name, destination)
        continue

    # archives
    if name.endswith(archivesFiles):
        destination = archivesFolder + "/" + name
        print(destination)
        os.rename(name, destination)
        continue

    # documents
    if name.endswith(documentsFiles):
        destination = documentsFolder + "/" + name
        print(destination)
        os.rename(name, destination)
        continue

    # media
    if name.endswith(mediaFiles):
        destination = mediaFolder + "/" + name
        print(destination)
        os.rename(name, destination)
        continue

