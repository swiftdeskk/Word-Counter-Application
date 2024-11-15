import re
import os

os.system('cls & title "Word Counter Application | discord.gg/moonlygg"')

# Función para limpiar la consola
def limpiar_consola():
    """Limpia la consola en función del sistema operativo."""
    os.system("cls" if os.name == "nt" else "clear")

# Función para contar las palabras
def contar_palabras(texto):
    """Cuenta las palabras en un texto."""
    palabras = texto.split()
    return len(palabras)

# Función para contar los caracteres
def contar_caracteres(texto):
    """Cuenta los caracteres en un texto (sin contar espacios adicionales)."""
    return len(texto.replace(" ", ""))

# Función para contar las frases
def contar_frases(texto):
    """Cuenta las frases en un texto (considerando que cada frase termina en punto, signo de interrogación o exclamación)."""
    frases = re.split(r'[.!?]', texto)
    return len([frase for frase in frases if frase.strip()])

# Función para guardar las estadísticas en un archivo
def guardar_estadisticas(texto, num_palabras, num_caracteres, num_frases):
    """Guarda las estadísticas en un archivo dentro de la carpeta 'output'."""
    # Asegurarse de que la carpeta 'output' exista
    if not os.path.exists('output'):
        os.makedirs('output')

    # Crear el nombre del archivo con base en la fecha y hora para evitar sobrescribir
    nombre_archivo = 'output/estadisticas.txt'

    with open(nombre_archivo, 'a') as archivo:
        archivo.write("Texto Analizado:\n")
        archivo.write(f"{texto}\n\n")
        archivo.write("Estadísticas:\n")
        archivo.write(f"Palabras: {num_palabras}\n")
        archivo.write(f"Caracteres: {num_caracteres}\n")
        archivo.write(f"Frases: {num_frases}\n")
        archivo.write("="*40 + "\n")

# Función para mostrar las estadísticas
def mostrar_estadisticas(texto):
    """Muestra las estadísticas del texto ingresado y guarda la información."""
    num_palabras = contar_palabras(texto)
    num_caracteres = contar_caracteres(texto)
    num_frases = contar_frases(texto)
    
    print("\nEstadísticas del texto:")
    print(f"Palabras: {num_palabras}")
    print(f"Caracteres: {num_caracteres}")
    print(f"Frases: {num_frases}")
    
    # Guardar las estadísticas en el archivo
    guardar_estadisticas(texto, num_palabras, num_caracteres, num_frases)

# Función para la interfaz de usuario
def interfaz_usuario():
    """Interfaz de usuario para ingresar el texto y mostrar las estadísticas."""
    print("Bienvenido a la Aplicación de Contador de Palabras! \n")
    texto = input("Por favor, ingresa el texto que deseas analizar:\n")
    
    mostrar_estadisticas(texto)

    # Regresar al menú principal después de mostrar resultados
    input("\nPresiona Enter para regresar al menú principal...")
    limpiar_consola()  # Limpiar la consola antes de regresar al menú principal

# Función principal que ejecuta el programa
def main():
    """Función principal que ejecuta el programa."""
    while True:
        try:
            limpiar_consola()  # Limpiar la consola al inicio del programa
            interfaz_usuario()
        except KeyboardInterrupt:
            print("\nPrograma detenido. ¡Adiós!")
            break

if __name__ == "__main__":
    main()