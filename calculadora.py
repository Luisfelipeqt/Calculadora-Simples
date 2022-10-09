def soma(a = 0, b = 0):
     return print(f"A soma de A + B é: {a + b}")

def subtracao(a = 0, b = 0):
     return print(f"A Subtração de A - B é: {a - b}")

def multiplicacao(a = 0, b = 0):
    return print(f"A multiplicação de A x B é: {a * b}")

def divisao(a, b):
    if (b == 0):
        print(f"Não pode dividir por zero!")
    else:
        print(f"O resultado da divisão é: { a / b}")
    


print("Calculadora simples!")

n1 = float(input("Insira o seu primeiro número: "))
n2 = float(input("Insire o seu segundo número: "))

soma(n1, n2)
subtracao(n1, n2)
multiplicacao(n1, n2)
divisao(n1, n2)
