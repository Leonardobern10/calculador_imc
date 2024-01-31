def classifica_imc(valor_imc):
    if valor_imc < 18.5:
        print("CLASSIFICAÇÃO DO IMC: Magreza")
    elif valor_imc >= 18.5 or valor_imc < 24.9:
        print("CLASSIFICAÇÃO DO IMC: Normal")
    elif valor_imc >= 25 or valor_imc < 29.9:
        print("CLASSIFICAÇÃO DO IMC: Sobrepeso")
    elif valor_imc >= 29.9 or valor_imc < 34.9:
        print("CLASSIFICAÇÃO DO IMC: Obesidade grau I")
    elif valor_imc >= 34.9 or valor_imc < 39.9:
        print("CLASSIFICAÇÃO DO IMC: Obesidade grau II")
    else:
        print("CLASSIFICAÇÃO DO IMC: Obesidade grau III")