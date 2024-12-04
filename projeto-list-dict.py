# Lista de filmes com dicionários
filmes = [
    {"nome": "O Senhor dos Anéis", "ano": 2001, "diretor": "Peter Jackson", "nota": 9.0},
    {"nome": "Matrix", "ano": 1999, "diretor": "Lana Wachowski e Lilly Wachowski", "nota": 8.7},
    {"nome": "Avatar", "ano": 2009, "diretor": "James Cameron", "nota": 8.2},
    {"nome": "Star Wars: Uma Nova Esperança", "ano": 1977, "diretor": "George Lucas", "nota": 8.6},
    {"nome": "Vingadores: Ultimato", "ano": 2019, "diretor": "Anthony e Joe Russo", "nota": 8.4},
    {"nome": "Interstellar", "ano": 2014, "diretor": "Christopher Nolan", "nota": 8.6},
    {"nome": "Inception", "ano": 2010, "diretor": "Christopher Nolan", "nota": 8.8},
    {"nome": "O Rei Leão", "ano": 1994, "diretor": "Roger Allers e Rob Minkoff", "nota": 8.5},
    {"nome": "Forrest Gump", "ano": 1994, "diretor": "Robert Zemeckis", "nota": 8.8},
    {"nome": "Clube da Luta", "ano": 1999, "diretor": "David Fincher", "nota": 8.8},
]

# Função para buscar informações de um filme
def buscar_filme(nome, filmes):
    for filme in filmes:
        if filme["nome"].lower() == nome.lower():
            return filme
    return None

# Função principal
def main():
    while True:
        nome_filme = input("Digite o nome do filme: ")
        filme_encontrado = buscar_filme(nome_filme, filmes)
    
        if filme_encontrado:
            print(f"\nInformações do filme:")
            print(f"Nome: {filme_encontrado['nome']}")
            print(f"Ano: {filme_encontrado['ano']}")
            print(f"Diretor: {filme_encontrado['diretor']}")
            print(f"Nota: {filme_encontrado['nota']}")
        else:
            print("Filme não encontrado.")

        continuar = input("Deseja pesquisar outro filme?(Sim/Não)").lower()
        if continuar =="não" or continuar =="nao":
            print("Encerrando o programa...")
            break
        
        else:
            continue



main()