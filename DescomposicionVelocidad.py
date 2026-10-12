import math

rapidezInicial = int(input('rapidez? ')) #m/s
anguloGrados = int(input('grados? ')) #grados
alturaInicial = 0 #m

anguloRadianes = math.radians(anguloGrados)
#Descomposicion de velocidades

Vy = rapidezInicial * math.sin(anguloRadianes)
Vx = rapidezInicial * math.cos(anguloRadianes)

print(f"vy = {Vy:.3f} m/s")
print(f"vx = {Vx:3f} m/s")
