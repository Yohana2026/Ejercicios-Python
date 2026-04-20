print ("Canción favorita")

tituloFav = input("Título de la canción: ")
artista = input("Artista: ")
album = input("Álbum: ")
annoLanzamiento = input("Año de lanzamiento: ")
duracionSegundos = input("Duración - segundos: ")
videoclip = input("¿Tiene videoclip? (Verdadero/Falso): ")

def tieneVideo(videoclip):
    if videoclip.lower() == "verdadero":
        return "tiene videoclip."
    else:
        return "no tiene videoclip."
    
print ("Su canción favorita es " + tituloFav + ". El artista es " + artista + ". Tu canción favorita pertenece al álbum " + album + ". Su año de lanzamiento fue " + annoLanzamiento + ". Tu canción favorita tiene una duración en segundos de " + duracionSegundos + ". Tu canción favorita " + tieneVideo(videoclip))

print ("Canción que menos te gusta")

tituloNoFav = input("Título de la canción: ")
artista = input("Artista: ")
album = input("Álbum: ")
annoLanzamiento = input("Año de lanzamiento: ")
duracionSegundos = input("Duración - segundos: ")
videoclip = input("¿Tiene videoclip? (Verdadero/Falso): ")

def tieneVideo(videoclip):
    if videoclip.lower() == "verdadero":
        return "tiene videoclip."
    else:
        return "no tiene videoclip."

    
print ("La canción que menos te gusta es " + tituloNoFav + ". El artista es " + artista + ". Esta canción pertenece al álbum " + album + ". Su año de lanzamiento fue " + annoLanzamiento + ". Tiene una duración en segundos de " + duracionSegundos + ". Esta canción " + tieneVideo(videoclip))

