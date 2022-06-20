from pickletools import optimize
from statistics import quantiles
from PIL import Image
import os

folderAmover = "Users/Estuardo/Documents/Software/Move-File/ArchivosAMover/" # Carpeta fuente
folderImagenesMovidas = "Users/Estuardo/Documents/Software/Move-File/CarpetaImagenesMovidas/" # Carpeta donde se moveran los archivos png|jpg|jpeg|webp
folderAudiosMovidos = "Users/Estuardo/Documents/Software/Move-File/CarpetaAudiosMovidos/" # Carpeta donde se moveran los archivos mp3
folderTXTMovidos = "Users/Estuardo/Documents/Software/Move-File/CarpetaTXTMovidos/" #Carpeta donde se moveran los archvios TXT

if __name__ == "__main__":
    for filename in os.listdir(folderAmover):
        name, extension = os.path.splitext(folderAmover + filename)

        # Se moveran las extensiones .png|.jpg|.jpeg.webp a la carpeta asignada en folderImagenesMovidas
        if extension in [".png", ".jpg", ".jpeg", ".webp"]:
            picture = Image.open(folderAmover + filename)
            picture.save(folderImagenesMovidas + "compressed_" + filename, optimize=True, quality=60)
            os.remove(folderAmover + filename)
            print(name + ": " + extension)