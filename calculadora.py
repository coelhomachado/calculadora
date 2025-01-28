def calculadora(num1, num2, opcao_calculo):
  if opcao_calculo == "1":
    return num1 + num2
  elif opcao_calculo == "2":
    return num1 - num2
  elif opcao_calculo == "3":
    return num1 * num2
  elif opcao_calculo == "4":
    return num1 / num2
  else:
    return 0

print("Hello")
print("Este é o algorítimo de uma calculadora")
num1 = int(input("Digite o primeiro número do cálculo:"))
num2 = int(input("Digite o segundo número do cálculo:"))
print("Essas são as opções de operações:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
opcao_calculo = input("Digite a opção desejada:")
print(calculadora(num1, num2, opcao_calculo))