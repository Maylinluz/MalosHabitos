def calcular(a, b, c):
    return a * b + c


def principal(x = 5, y = 3, z = 7):

    resultado = calcular(x, y, z)
    print(f"El resultado de {x} * {y} + {z} es: {resultado}")

if __name__ == "__main__":

principal()
