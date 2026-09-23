def fizzbuzz() -> list[str]:
    """Genera la lista de elementos para los números del 1 al 100 con la regla FizzBuzz."""
    resultado = []
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            resultado.append("FizzBuzz")
        elif i % 3 == 0:
            resultado.append("Fizz")
        elif i % 5 == 0:
            resultado.append("Buzz")
        else:
            resultado.append(str(i))
    return resultado


def expand(cifras: list[int]) -> list[int]:
    """Dado un arreglo con las cifras de un número expansivo, genera el siguiente."""
    if not cifras:
        return []
    
    siguiente = []
    cifra_actual = cifras[0]
    conteo = 0
    
    for cifra in cifras:
        if cifra == cifra_actual:
            conteo += 1
        else:
            siguiente.extend([conteo, cifra_actual])
            cifra_actual = cifra
            conteo = 1
            
    siguiente.extend([conteo, cifra_actual])
    return siguiente


def list2num(cifras: list[int]) -> int:
    """Dado un arreglo con las cifras de un número expansivo, devuelve el número entero."""
    if not cifras:
        return 0
    return int("".join(map(str, cifras)))


if __name__ == "__main__":
    # Imprime el resultado de FizzBuzz por pantalla según la consigna
    for elemento in fizzbuzz():
        print(elemento)