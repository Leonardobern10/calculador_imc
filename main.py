# Calculadora de IMC
from calculo_imc import calculo_imc
from classifica_imc import classifica_imc


def main():
    inicio = input("Bem vindo a calculador de IMC. Deseja realizar o calculo? S/N")
    if inicio.lower() == "s":
        imc = calculo_imc()
        print(f"Seu imc é igual a {imc} kg/mg²")
        classifica_imc(imc)
    elif inicio.lower() == "n":
        print("Fechando...")
    else:
        print("Comando inválido! Pressione 'N' para sair.")
        main()


main()