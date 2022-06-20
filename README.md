# Move File
Move File es un automatizador para mover archivos según su extensión hacia la carpeta deseada, como por ejemplo:
`Mover archivos .png a /Pictures`
Con Move File los archivos con extensión `.png`  se moveran a la carpeta `/Pictures`

## Instrucciones de uso
Pasa el uso de nuestro sistema necesitaras seguir algunos cuantos pasos, pero te lo explicaremos brevemente.

1. Las variables del folder fuente se debe modificar a tu usuario y tu carpeta

Ejemplo: 
Mi directorio es: 
`C:/Users/Estuardo/Documents/Softwares/Move-File/ArchivosAMover/`
Deveras sustituir "/Estuardo/Documents/Softwares/Move-File/ArchivosAMover/" por tu carpeta donde se encuentran los archivos a mover

2. Las variables de los folders destino se debe modificar a tu usuario y tu carpeta

Ejemplo: 
Mi directorio es: 
`C:/Users/Estuardo/Documents/Softwares/Move-File/CarpetaImagenesMovidas/`
Deveras sustituir "/Estuardo/Documents/Softwares/Move-File/CarpetaImagenesMovidas/" por tu carpeta donde se moveran los archivos (Se debe de hacer con cada 1 de las variables)

## Agregar Formatos
Si se desean agregar nuevos formatos de archivos puedes hacer lo siguiente: 
Creas una variable con el destino:
`folderUbicacion = r"C:/Users/TuUsuario/Destino/Destino/`

Copias el siguiente bloque de codigo y cambias la extensión que veras y por ultimo lo mandas a llamar al ejecutor.

    def moverARCHIVO(): # Nombre de la funcion
        for filename in os.listdir(folderAmover):
            name, extension = os.path.splitext(folderAmover + filename)
            
            if extension in [".ARCHIVO"]: #Extension a cambiar
                os.rename(folderAmover + filename, TUVARIABLE + filename) #Reemplazar TUVARIABLE por tu variable
                print(name + ": " + extension)

Por ultimo lo mandas a llamar en "_main_"

### Consejos
Para evitarte declarar demasiadas funciones simplemente puedes agregar varias extensiones en una sola función creada por ti, siguiendo el ejemplo de la función para mover imagenes.

### Posibles problemas
Recuerda colocar siempre la `/` al final de las carpeta destino.
La dirección de tu carpeta destino puede variar con el OS que uses.