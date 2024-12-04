def calcular(numero1, operador, numero2):
    if operador == "+":
        return numero1 + numero2
    elif operador == "-":
        return numero1 - numero2
    elif operador == "*":
        return numero1 * numero2
    elif operador == "/":
        return numero1 / numero2
    else:
        return "Erro:Número invalido."
    
def interpretador():
    try:
        entrada = input("Digite uma expressão aritmética(número; operador; numero):")
        partes = entrada.split()

        if len(partes)!=3:
            print("Erro: Formato inválido")
            return
        
        operando1 = float(partes[0])
        operador = partes[1]
        operando2 = float(partes[2])

        resultado = calcular(operando1, operador, operando2)
        print("resultado:", resultado)

    except ValueError:
        print("Erro: Certifique-se de que os números estão corretos.")
    except Exception as e:
        print("Erro inesperado:",e)

interpretador()
        

