
print ("Informacion sobre tu pelicula favorita")

peliculaFavorita = input("Título de la película: ")

directorPelicula = input("Director de la película: ")

annoLanzamiento = input("Año de lanzamiento: ")

genero = input("Género: ")

duracion = input("Duración - minutos: ")

premios = input("¿Tiene premios? (verdadero o falso): ")

def tienePremio(premios):
    if premios.lower() == "verdadero":
        return "tiene premios"
    else:
        return "no tiene premio"



print ( "Tu película favorita es " + peliculaFavorita + ". El director es " + directorPelicula + ". Su año de lanzamiento fue " + annoLanzamiento + ". El género de tu película favorita es " + genero + ". Su duración en minutos es " + duracion + ". Tu película favorita " + tienePremio(premios))

#ERROR: La orden del ejercicio dice que luego de entrar la información se debe mostrar y no muestra nada. 
print ("Information about your favorite movie")

peliculaFavorita = input("Movie title: ")

directorPelicula = input("Film Director: ")

annoLanzamiento = input("Year of release: ")

genero = input("Genre: ")

duracion = input("Duration - minutes: ")

premios = input("Does it have any awards? (true or false): ")

def tienePremio(premios):
    if premios.lower() == "true":
        return "has awards"
    else:
        return "has no awards"

print ( "Your favorite movie is " + peliculaFavorita + ". The director is " + directorPelicula + ". Its release year was " + annoLanzamiento + ". The genre of your favorite movie is " + genero + ". Its duration in minutes is " + duracion + ". Your favorite movie " + tienePremio(premios))

