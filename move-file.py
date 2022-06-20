from pickletools import optimize
from statistics import quantiles
from PIL import Image
import os

folderAmover = r"C:/Users/Estuardo/Documents/Softwares/Move-File/ArchivosAMover/" # Carpeta fuente
folderImagenesMovidas = r"C:/Users/Estuardo/Documents/Softwares/Move-File/CarpetaImagenesMovidas/" # Carpeta donde se moveran los archivos png|jpg|jpeg|webp
folderAudiosMovidos = r"C:/Users/Estuardo/Documents/Softwares/Move-File/CarpetaAudiosMovidos/" # Carpeta donde se moveran los archivos mp3
folderTXTMovidos = r"C:/Users/Estuardo/Documents/Softwares/Move-File/CarpetaTXTMovidos/" #Carpeta donde se moveran los archvios TXT

# Se moveran las extensiones .png|.jpg|.jpeg.webp a la carpeta asignada en folderImagenesMovidas
def moverImagenes():
    for filename in os.listdir(folderAmover):
        name, extension = os.path.splitext(folderAmover + filename)

        if extension in [".png", ".jpg", ".jpeg", ".webp"]:
            picture = Image.open(folderAmover + filename)
            picture.save(folderImagenesMovidas + filename, optimize=True, quality=60)
            os.remove(folderAmover + filename)
            print(name + ": " + extension)    

# Se moveran los archivos de audio a la carpeta folderAudiosMovidos
def moverAudios():
    for filename in os.listdir(folderAmover):
        name, extension = os.path.splitext(folderAmover + filename)
        
        if extension in [".mp3"]:
            os.rename(folderAmover + filename, folderAudiosMovidos + filename)
            print(name + ": " + extension)

# Se moveran los archivos TXT a la carpeta folderTXTMovidos
def moverTXT():
    for filename in os.listdir(folderAmover):
        name, extension = os.path.splitext(folderAmover + filename)
        
        if extension in [".txt"]:
            os.rename(folderAmover + filename, folderTXTMovidos + filename)
            print(name + ": " + extension)

if __name__ == "__main__":
    moverImagenes()
    moverAudios()
    moverTXT()