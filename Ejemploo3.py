
def calcular_area_rectangulo(ancho, largo):

    return ancho * largo

def calcular_area_triangulo(base, altura):

    return 0.5 * base * altura

def main():

    ancho = 4
    largo = 6
    rect_area = calcular_area_rectangulo(ancho, largo)
    print(f"Área del rectángulo de ancho {ancho} y largo {largo} es: {rect_area}")


    base = 5
    altura = 8
    tri_area = calcular_area_triangulo(base, altura)
    print(f"Área del triángulo de base {base} y altura {altura} es: {tri_area}")


if __name__ == "__main__":
    main()

