if __name__ == "__main__":
    x = int(1)
    y = int(1)
    z = int(1)
    n = int(2)

    resultado = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
    resultado = list(resultado)

    print(resultado)