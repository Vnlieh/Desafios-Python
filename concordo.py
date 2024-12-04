def main():
    resposta = input("Você concorda?").lower()
    concordo(resposta)

def concordo(resposta):
    if resposta == "sim" or resposta == "s":
        print("Concordo.")
    elif resposta == "não" or resposta == "nao" or resposta == "n":
        print("Não concordo.")
    else:
        print("Comando não encontrado.")
main()