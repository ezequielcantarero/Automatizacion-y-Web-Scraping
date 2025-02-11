import os
import shutil

# Ruta de origen (descargas)
origen = "C:/Users/ezequ/Downloads"

# Diccionario con extensiones y carpetas destino
destinos = {
    "pdf": "Documentos",
    "jpg": "Imágenes",
    "mp3": "Música"
}

# Recorre los archivos en la carpeta de origen
for archivo in os.listdir(origen):
    ext = archivo.split(".")[-1]  # Obtiene la extensión del archivo
    if ext in destinos:
        carpeta_destino = os.path.join(origen, destinos[ext])  # Ruta completa del destino
        
        # ✅ Si la carpeta no existe, la crea
        if not os.path.exists(carpeta_destino):
            os.makedirs(carpeta_destino)

        # ✅ Mueve el archivo a su carpeta correspondiente
        shutil.move(os.path.join(origen, archivo), os.path.join(carpeta_destino, archivo))

print("Archivos organizados correctamente 🚀")
