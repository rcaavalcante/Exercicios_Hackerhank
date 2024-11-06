if __name__ == "__main__":
    import sys

    input = sys.stdin.read
    dados = input().strip().split('\n')

    # Leitura dos dados
    n = int(dados[0])
    english_subscribers = set(map(int, dados[1].split()))

    b = int(dados[2])
    french_subscribers = set(map(int, dados[3].split()))

    # Encontrar a interseção dos conjuntos
    both_subscribed = english_subscribers & french_subscribers

    # Imprimir o número de estudantes que assinaram ambos os jornais
    print(len(both_subscribed))

