
def multiplicacion(multiplicando,multiplicador):
    producto = multiplicando * multiplicador
    return producto

if __name__=="__main__":

multiplicando = float(input("multiplicando:"))
multiplicador = float(input("multiplicador:"))

resultado = multiplicacion(multiplicando, multiplicador)
print(f"{multiplicando}*{multiplicador}={resultado}")