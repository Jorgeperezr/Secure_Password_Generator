import random
import string

def generar_contraseña(longitud, incluir_letras=True, incluir_digitos=True, incluir_especiales=True, incluir_mayusculas=True, incluir_minusculas=True):
    # La función "generar_contraseña" permite al usuario personalizar la contraseña:
    # longitud (int): Establecer longitud deseada de la contraseña.
    # incluir_letras (bool): Seleccionar si se incluye letras en la contraseña.
    # incluir_digitos (bool): Seleccionar si se incluye dígitos en la contraseña.
    # incluir_especiales (bool): Indica si se incluye caracteres especiales en la contraseña.
    # incluir_mayusculas (bool): Indica si se incluyen letras mayúsculas en la contraseña.
    # incluir_minusculas (bool): Indica si se incluyen letras minúsculas en la contraseña.

    caracteres = ""

    # Construir el conjunto de caracteres según las preferencias del usuario
    if incluir_letras:
        if incluir_mayusculas:
            caracteres += string.ascii_uppercase
        if incluir_minusculas:
            caracteres += string.ascii_lowercase
    if incluir_digitos:
        caracteres += string.digits
    if incluir_especiales:
        caracteres += string.punctuation

    # Verificar que al menos un tipo de caracter esté incluido
    if not caracteres:
        raise ValueError("Debe seleccionar al menos un tipo de caracter.")

    # Generar la contraseña aleatoria
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

def obtener_preferencias_contraseña():
    """
    Obtiene las preferencias del usuario para generar la contraseña.

    Returns: una tupla de booleanos indicando si incluir letras, dígitos, caracteres especiales, mayúsculas y minúsculas.
    """
    try:
        # Solicitar al usuario que elija las preferencias para la generacion de su contraseña
        incluir_letras = input("¿Desea incluir letras en su contraseña? (s/n): ").lower() == 's'
        incluir_digitos = input("¿Desea incluir dígitos en su contraseña? (s/n): ").lower() == 's'
        incluir_especiales = input("¿Desea incluir caracteres especiales en su contraseña? (s/n): ").lower() == 's'
        incluir_mayusculas = input("¿Incluir mayúsculas? (s/n): ").lower() == 's'
        incluir_minusculas = input("¿Incluir minúsculas? (s/n): ").lower() == 's'

        return incluir_letras, incluir_digitos, incluir_especiales, incluir_mayusculas, incluir_minusculas
    except ValueError:
        print("Error. Ingrese 's' para sí o 'n' para no.")

def obtener_longitud_contraseña():
    """
    Obtiene la longitud deseada para la contraseña del usuario.

    Returns: la longitud deseada para la contraseña (int).
    """
    while True:
        try:
            # Solicitar al usuario que ingrese la longitud deseada para la contraseña
            longitud = int(input("Ingrese la longitud deseada para su contraseña: "))

            # Validar si la longitud es positiva y mayor o igual a 5
            if longitud <= 0:
                print("Error. Se debe escoger un número positivo.")
            elif longitud < 5:
                print("Error. Para que la contraseña sea segura debe tener al menos 5 caracteres.")
            else:
                return longitud
        except ValueError:
            print("Error. Ingrese un número válido.")

def main():
    # Bucle while para establecer la longitud de la contraseña
    while True:
        longitud_contraseña = obtener_longitud_contraseña()

        # Obtener las preferencias del usuario para la contraseña
        incluir_letras, incluir_digitos, incluir_especiales, incluir_mayusculas, incluir_minusculas = obtener_preferencias_contraseña()

        try:
            # Generar la contraseña
            contraseña_generada = generar_contraseña(
                longitud_contraseña,
                incluir_letras,
                incluir_digitos,
                incluir_especiales,
                incluir_mayusculas,
                incluir_minusculas
            )

            # Mostrar la contraseña generada
            print(f"La contraseña generada es: {contraseña_generada}")
            break
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
