print ("Canción favorita")

tituloFav = input("Título de la canción: ")

artista = input("Artista: ")

album = input("Álbum: ")

annoLanzamiento = input("Año de lanzamiento: ")

duracionSegundos = input("Duración - segundos: ")

videoclip = input("¿Tiene videoclip? (Verdadero/Falso): ")

def tieneVideo(videoclip):
    if videoclip.lower() == "verdadero":
        return "tiene premios."
    else:
        return "no tiene premio."
    
print ("Su canción favorita es " + tituloFav + ". El artista es " + artista + ". Tu canción favorita pertenece al álbum " + album + ". Su año de lanzamiento fue " + annoLanzamiento + ". Tu canción favorita tiene una duración en segundos de " + duracionSegundos + ". Tu canción favorita " + tieneVideo(videoclip))



print ("Canción que menos te gusta")

tituloNoFav = input("Título de la canción: ")

artista = input("Artista: ")

album = input("Álbum: ")

annoLanzamiento = input("Año de lanzamiento: ")

duracionSegundos = input("Duración - segundos: ")

noVideoclip = input("¿Tiene videoclip? (Verdadero/Falso): ")

def noTieneVideo(noVideoclip):
    if noVideoclip.lower() == "verdadero":
        return "tiene premios"
    else:
        return "no tiene premio."
    
    
print ("Su canción favorita es " + tituloNoFav + ". El artista es " + artista + ". Tu canción favorita pertenece al álbum " + album + ". Su año de lanzamiento fue " + annoLanzamiento + ". Tu canción favorita tiene una duración en segundos de " + duracionSegundos + ". Tu canción favorita " + noTieneVideo(noVideoclip))

