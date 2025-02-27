Inicio = int(input("Digite o valor inicial:  "))
fim = int(input("Digite o valor final:  "))
soma = 0
for i in range(Inicio,fim+1):
 if i % 2 == 0:
    soma += i
    print(f"soma dos pares {i} é igual a {soma}")