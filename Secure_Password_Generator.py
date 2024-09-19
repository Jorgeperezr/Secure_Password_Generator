import string
import random

# Historial de contraseñas generadas
historial_contraseñas = []
pin = None

# Función para establecer el PIN
def establecer_pin():
    global pin
    while True:
        pin_1 = input("Se requiere establecer un PIN de 4 a 6 dígitos para gestionar las contraseñas: ")
        pin_2 = input("Confirme su PIN: ")
        
        if pin_1 == pin_2 and pin_1.isdigit() and 4 <= len(pin_1) <= 6:
            pin = pin_1
            print("PIN establecido correctamente.")
            break
        else:
            print("Error. Los PIN no coinciden o no cumplen con los requisitos (4 a 6 dígitos).")

# Función para verificar el PIN
def verificar_pin():
    for _ in range(3):  # Tres intentos para ingresar el PIN correcto
        intento = input("Ingrese su PIN para ver las contraseñas: ")
        if intento == pin:
            return True
        else:
            print("PIN incorrecto.")
    return False

# Función para mostrar el historial de contraseñas
def mostrar_historial():
    if verificar_pin():
        if historial_contraseñas:
            print("\nHistorial de contraseñas generadas:")
            for i, contraseña in enumerate(historial_contraseñas, 1):
                print(f"{i}. {contraseña}")
        else:
            print("\nNo hay contraseñas generadas aún.")
    else:
        print("Ha superado el número máximo de intentos. Acceso denegado.")

# Función para generar contraseñas seguras
def generar_contraseña(longitud, incluir_letras=True, incluir_digitos=True, incluir_especiales=True, incluir_mayusculas=True, incluir_minusculas=True):
    caracteres = ""

    if incluir_letras:
        if incluir_mayusculas:
            caracteres += string.ascii_uppercase
        if incluir_minusculas:
            caracteres += string.ascii_lowercase
    if incluir_digitos:
        caracteres += string.digits
    if incluir_especiales:
        caracteres += string.punctuation

    if not caracteres:
        raise ValueError("Debe seleccionar al menos un tipo de caracter.")

    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

# Función para verificar la fortaleza de la contraseña
def verificar_fortaleza(contraseña):
    longitud = len(contraseña)
    tiene_mayusculas = any(c.isupper() for c in contraseña)
    tiene_minusculas = any(c.islower() for c in contraseña)
    tiene_digitos = any(c.isdigit() for c in contraseña)
    tiene_especiales = any(c in string.punctuation for c in contraseña)

    if longitud >= 12 and tiene_mayusculas and tiene_minusculas and tiene_digitos and tiene_especiales:
        return "Fuerte"
    elif longitud >= 8 and (tiene_mayusculas or tiene_minusculas) and tiene_digitos:
        return "Media"
    else:
        return "Débil"

def obtener_preferencias_contraseña():
    while True:
        try:
            incluir_letras = input("¿Desea incluir letras en su contraseña? (s/n): ").lower() == 's'
            incluir_digitos = input("¿Desea incluir dígitos en su contraseña? (s/n): ").lower() == 's'
            incluir_especiales = input("¿Desea incluir caracteres especiales en su contraseña? (s/n): ").lower() == 's'
            incluir_mayusculas = input("¿Incluir mayúsculas? (s/n): ").lower() == 's'
            incluir_minusculas = input("¿Incluir minúsculas? (s/n): ").lower() == 's'
            return incluir_letras, incluir_digitos, incluir_especiales, incluir_mayusculas, incluir_minusculas
        except ValueError:
            print("Error. Ingrese 's' para sí o 'n' para no.")

def obtener_longitud_contraseña():
    while True:
        try:
            longitud = int(input("Ingrese la longitud deseada para su contraseña: "))
            if longitud < 5:
                print("Error. La contraseña debe tener al menos 5 caracteres.")
            else:
                return longitud
        except ValueError:
            print("Error. Ingrese un número válido.")

def main():
    establecer_pin()  # Establecer el PIN al inicio del programa

    while True:
        print("\n--- Generador de Contraseñas ---")
        print("1. Generar nueva contraseña")
        print("2. Ver historial de contraseñas")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            longitud_contraseña = obtener_longitud_contraseña()
            incluir_letras, incluir_digitos, incluir_especiales, incluir_mayusculas, incluir_minusculas = obtener_preferencias_contraseña()

            try:
                contraseña_generada = generar_contraseña(
                    longitud_contraseña,
                    incluir_letras,
                    incluir_digitos,
                    incluir_especiales,
                    incluir_mayusculas,
                    incluir_minusculas
                )
                fortaleza = verificar_fortaleza(contraseña_generada)
                print(f"\nContraseña generada: {contraseña_generada} (Fortaleza: {fortaleza})")
                historial_contraseñas.append(contraseña_generada)
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "2":
            mostrar_historial()

        elif opcion == "3":
            print("¡Gracias por usar el generador de contraseñas!")
            break

        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()
