# Livro: Introdução à programação com Python - Algoritmo e lógica de programação para iniciantes
# Exercício 4.4 (Condicionais)

salario = float(input("Qual o seu salário? "))
aumento = 0
salario_final = 0

if salario > 1250:
    aumento = 0.10
elif salario <= 1250:
    aumento = 0.15

salario_final = salario + (salario * aumento)

print(f"Salário Final: R$ {salario_final:6.2f}")
