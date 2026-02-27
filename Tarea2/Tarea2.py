def convertir_a_binario(n):
    if n <= 1:
        return str(n)
    return convertir_a_binario(n // 2) + str(n % 2)
def contar_digitos(n):
    n = abs(n)
    if n < 10:
        return 1
    return 1 + contar_digitos(n // 10)
def raiz_cuadrada_entera(n):
    def calcular_raiz_cuadrada(n, estimacion):
        if estimacion * estimacion > n:
            return estimacion - 1
        return calcular_raiz_cuadrada(n, estimacion + 1)
    if n < 0: return "No definida para negativos"
    return calcular_raiz_cuadrada(n, 0)
def convertir_a_decimal(romano):
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    romano = romano.upper()
    if len(romano) == 0:
        return 0
    if len(romano) == 1:
        return valores[romano]
    if valores[romano[0]] < valores[romano[1]]:
        return valores[romano[1]] - valores[romano[0]] + convertir_a_decimal(romano[2:])
    else:
        return valores[romano[0]] + convertir_a_decimal(romano[1:])
def suma_numeros_enteros(n):
    if n <= 0:
        return 0
    return n + suma_numeros_enteros(n - 1)
def menu():
    while True:
        print("\n--- MENÚ INTERACTIVO RECURSIVO ---")
        print("1. Convertir a Binario")
        print("2. Contar Dígitos")
        print("3. Raíz Cuadrada Entera")
        print("4. Convertir Romano a Decimal")
        print("5. Suma de Números Enteros")
        print("6. Salir")
        opcion = input("Selecciona una opción (1-6): ")
        if opcion == '1':
            num = int(input("Ingresa un número entero: "))
            print(f"Resultado Binario: {convertir_a_binario(num)}")
        elif opcion == '2':
            num = int(input("Ingresa un número: "))
            print(f"Cantidad de dígitos: {contar_digitos(num)}")
        elif opcion == '3':
            num = int(input("Ingresa un número: "))
            print(f"Raíz cuadrada entera: {raiz_cuadrada_entera(num)}")
        elif opcion == '4':
            rom = input("Ingresa número romano (ej. XIV): ")
            print(f"Valor decimal: {convertir_a_decimal(rom)}")
        elif opcion == '5':
            num = int(input("Sumar hasta el número: "))
            print(f"La suma total es: {suma_numeros_enteros(num)}")
        elif opcion == '6':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")
if __name__ == "__main__":
    menu()