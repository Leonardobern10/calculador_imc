def calculo_imc():
    altura = float(input("Informe sua altura: "))
    peso = float(input("Informe seu peso: "))
    imc = peso / altura ** 2
    return imc