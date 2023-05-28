import math

grau = int(input("Digite o grau da equação (1 ou 2): "))

if grau < 1 or grau > 2:
    print("Grau inválido")
else:
    
    if grau == 1:
        print("A equação é do primeiro grau")
        a = float(input("Digite o valor de a: "))

        if a == 0:
            print("Valor de a inválido")
        else:
            b = float(input("Digite o valor de b: "))
            raiz = -b / a
            print(f"Raiz da equação: {raiz:.2f}")

    if grau == 2:
        print("A equação é do segundo grau")
        a = float(input("Digite o valor de a: "))

        if a == 0:
            print("Valor de a inválido")
        else:
            b = float(input("Digite o valor de b: "))
            c = float(input("Digite o valor de c: "))

            delta = b ** 2 - 4 * a * c

            if delta < 0:
                print("A equação não possui raízes reais")
            elif delta == 0:
                raiz = -b / (2 * a)
                print(f"A equação possui uma raiz real: {raiz:.2f}")
            else:
                raiz1 = (-b + math.sqrt(delta)) / (2 * a)
                raiz2 = (-b - math.sqrt(delta)) / (2 * a)
                print(f"A equação possui duas raízes reais: {raiz1:.2f}, {raiz2:.2f}")
