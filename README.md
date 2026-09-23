# Trabajo Práctico: Testing Unitario con Pytest (QA)

Este repositorio contiene la resolución de las consignas prácticas asignadas para el módulo de **QA Automation**, centradas en el desarrollo e implementación de **pruebas unitarias** utilizando el framework `pytest` en Python.

---

## Consignas del Trabajo

### 1. FizzBuzz
Generar e imprimir los números del 1 al 100 aplicando las siguientes reglas:
* Si el número es divisible por **3**, la salida es `"Fizz"`.
* Si el número es divisible por **5**, la salida es `"Buzz"`.
* Si el número es divisible por **3 y por 5**, la salida es `"FizzBuzz"`.
* En cualquier otro caso, se devuelve el número como una cadena de texto.

### 2. Números Expansivos (Look-and-Say)
Dada una secuencia de números expansivos donde el primer término es `1`:
* **Sustitución:** Cada grupo de $n$ cifras consecutivas iguales en un número expansivo se reemplaza por el número $n$ seguido de la cifra repetida (por ejemplo, `3333` $\rightarrow$ `43`).
* **Secuencia de ejemplo:**
  * `1` $\rightarrow$ *"un uno"*: `11`
  * `11` $\rightarrow$ *"dos unos"*: `21`
  * `21` $\rightarrow$ *"un dos, un uno"*: `1211`
  * `1211` $\rightarrow$ *"un uno, un dos, dos unos"*: `111221`

Se desarrollaron dos funciones principales:
1. `expand(cifras)`: Recibe una lista con las cifras de un número expansivo y genera la lista correspondiente al siguiente término de la secuencia.
2. `list2num(cifras)`: Recibe la lista con las cifras de un número expansivo y la convierte en un entero único.

---

## Estructura del Proyecto

```text
qa-tp-unit-tests/
├── src/
│   └── ejercicios.py         # Lógica de FizzBuzz y Números Expansivos
├── tests/
│   └── test_ejercicios.py    # Suite de pruebas unitarias con pytest
├── README.md                 # Documentación técnica del proyecto
└── requirements.txt          # Dependencias del proyecto