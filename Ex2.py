print("Lista de números inteiros")

def lista1(num1, num2, num3, num4, num5):
    if num1 < num2 < num3 < num4 < num5:
        return "Esta é uma lista de ordem crescente!!!"
    else:
        return "A lista que você escreveu não está em ordem crescente!!!"

num1 = int(input("Agora você usúario indicará uma lista de 5 números para vermos se ela é crescente ou não, comece com o primeiro: "))
num2 = int(input("Agora digite o segundo número: "))
num3 = int(input("Terceiro: "))
num4 = int(input("Quarto: "))
num5 = int(input("E por fim indique o quinto número: "))

resultado = lista1(num1, num2, num3, num4, num5)

print(resultado)


