def ler_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Ei! Digite um numero válido (ex: 1, 2 ...)")


numero = ler_inteiro("Digite o numero para ver a tabuada: ")


print(f"\nTabuada do {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
