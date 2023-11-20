import random
#Funciones Solicitadas
def generar_lista_de_atletas():
    lista_atletas = []
    nombres = ('Daniel', 'Alejandro', 'Pablo', 'Hugo', 'Álvaro', 'Adrián', 'David', 'Sergio', 'Diego')
    apellidos = ('García', 'Rodríguez', 'González', 'Fernández', 'López', 'Martínez', 'Sanchez', 'Pérez')   
    for i in range(1, 21):
        atleta = {
            "nombre": random.choice(nombres) + " " + random.choice(apellidos),
            "numero": i,
            "tiempo_llegada": random.random() * 120
        }
        lista_atletas.append(atleta)
    return lista_atletas

#Mostrar atletas
def imprimir_atletas(lista_atletas):
    for atleta in lista_atletas:
        print(f"{atleta['numero']} - {atleta['nombre']}: ({atleta['tiempo_llegada']:.2f} segundos)")

#Obtener un ganador
def obtener_ganador(lista_atletas):
    ganador = min(lista_atletas, key=lambda x: x['tiempo_llegada'])
    return ganador['numero']

#Obtener datos de atletas
def obtener_datos_atleta(lista_atletas, numero_atleta):
    for atleta in lista_atletas:
        if atleta['numero'] == numero_atleta:
            return atleta

#Obtener ganadores
def obtener_podio(lista_atletas):
    podio = sorted(lista_atletas, key=lambda x: x['tiempo_llegada'])[:3]
    return tuple(atleta['numero'] for atleta in podio)

# Llamar a todas las funciones
lista_atletas = generar_lista_de_atletas()
print("Lista de atletas generada:")
imprimir_atletas(lista_atletas)

numero_ganador = obtener_ganador(lista_atletas)
print(f"\nEl ganador es el atleta número {numero_ganador}.")

numero_atleta_consulta = 5  # Puedes cambiar este número según el atleta que desees consultar
datos_atleta = obtener_datos_atleta(lista_atletas, numero_atleta_consulta)
print(f"\nDatos del atleta número {numero_atleta_consulta}: {datos_atleta}")

numeros_podio = obtener_podio(lista_atletas)
print(f"\nNúmeros de los atletas en el podio: {numeros_podio}")