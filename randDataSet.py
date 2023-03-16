# Generación de información aleatoria
import random
import datetime

# Configuración de variables
actividades = ['ENT', 'SAL', 'DATA']
origenados = ['123456789012', '12345678', '123']
duracion_nula = [3, 8]
receptor_actividad = {'ENT': ['SAL'], 'SAL': ['ENT', 'DATA'], 'DATA': ['SAL']}
imei_sal_data = '123456789012345'
latitud = [19.403464]
longitud = [-99.175982]
azimuth = [180]
calles = ['AV. TEPEYAC/AV. PATRIA', 'AV. JUAREZ/AV. HIDALGO', 'AV. INSURGENTES/AV. REVOLUCION']
colonias = ['Centro', 'Del Valle', 'Polanco']
municipios = ['Ciudad de México', 'Guadalajara', 'Monterrey']

# Función para generar una fecha y hora aleatorias
def generar_fecha_hora():
    fecha = datetime.datetime(year=2023, month=random.randint(1, 12), day=random.randint(1, 28))
    hora = datetime.time(hour=random.randint(0, 23), minute=random.randint(0, 59), second=random.randint(0, 59))
    return fecha, hora

# Función para generar una duración aleatoria
def generar_duracion():
    return None if random.randint(1, 10) in duracion_nula else random.randint(1, 3600)

# Función para generar un número de teléfono aleatorio
def generar_numero_telefonico(num_digitos):
    return str(random.randint(10**(num_digitos-1), (10**num_digitos)-1))

# Función para generar un campo receptor aleatorio
def generar_receptor(actividad):
    if actividad in receptor_actividad:
        return generar_numero_telefonico(12)
    else:
        return None

# Generar datos aleatorios
#filas = int(input("Ingrese la cantidad de filas que desea generar: "))
filas = 150
datos = []
for i in range(filas):
    fecha, hora = generar_fecha_hora()
    actividad = random.choice(actividades)
    originado = random.choice(origenados)
    receptor = generar_receptor(actividad)
    imei = imei_sal_data if actividad in ['SAL', 'DATA'] else None
    duracion = generar_duracion()
    lat = [str(random.choice(latitud))]
    lon = [str(random.choice(longitud))]
    azim = [str(random.choice(azimuth))]
    calle = random.choice(calles)
    colonia = random.choice(colonias)
    municipio = random.choice(municipios)
    datos.append([fecha, hora, actividad, originado, receptor, imei, duracion, lat, lon, azim, calle, colonia, municipio])

# Guardar datos aleatorios en un archivo CSV
import csv
with open('datos_aleatorios.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Fecha', 'Hora', 'Actividad', 'Originado', 'Receptor', 'IMEI', 'Duracion', 'Latitud', 'Longitud', 'Azimuth', 'Calle', 'Colonia', 'Municipio'])
    writer.writerows(datos)