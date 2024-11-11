##################################################
############  Repositorio de la API  #############
# Github: https://github.com/yt-dlp/yt-dlp       #
##################################################

import subprocess
import sys

# Verificar si la librería yt-dlp está instalada, si no, instalarla
try:
    import yt_dlp
except ImportError:
    print("yt-dlp no está instalado. Instalando...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "yt-dlp"])
    import yt_dlp

def downloader(link, nombre):
    '''
    Función que descarga el audio de un video de YouTube en formato mp3.

    Parámetros:
        link: str
            URL de YouTube del video que se quiere descargar.
        nombre: str
            Nombre del archivo de salida (sin extensión).

    Retorno:
        None
    '''
    ydl_opts = {
        'format': 'bestaudio',  # Descargar solo el mejor formato de audio disponible
        'outtmpl': nombre + ".mp3"  # Definir el nombre del archivo de salida con extensión .mp3
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])  # Descargar el archivo desde el link de YouTube
    print('Download successful!')

if __name__ == "__main__":
    '''
    Ejemplo de uso:
        Link: URL del video de YouTube.
        Nombre: Nombre que se desea para el archivo de salida.

    Ejemplo:
        Link = 'https://www.youtube.com/watch?v=cmpRLQZkTb8&ab_channel=OasisVEVO'
        Nombre = 'dont look back in anger'
        downloader(Link, Nombre.replace(' ', '_'))

    Descripción:
        Este script descarga el audio de un video de YouTube y guarda el archivo en formato MP3 con el nombre proporcionado.
        Las mayúsculas se mantienen en el nombre, y los espacios en blanco se reemplazan por guiones bajos (_).
    '''
    # Definir el link y nombre del archivo a descargar
    Link = 'https://www.youtube.com/watch?v=Vw9MCNbFggI&ab_channel=2020Onwards'
    Nombre = 'max_cheer'
    
    # Ejecutar la función downloader con el nombre ajustado
    downloader(Link, Nombre.replace(' ', '_'))