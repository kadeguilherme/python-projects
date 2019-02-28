#split criar uma lista separada por espaços
linha = input().split(" ")
linha2 = input().split(" ")
#tranforma a str da lista em int e float
codigo = int(linha[0])
codigo2 = int(linha2[0])
nume = int(linha[1])
nume2 = int(linha2[1])
valor = float(linha[2])
valor2 = float(linha2[2])

res = (nume * valor) + (nume2 * valor2)
print("VALOR A PAGAR: R$ {:.2f}".format(res))