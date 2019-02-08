#strip tira os espaços antes e depois
nome = input("Digite seu nome: ").strip()

print("Analisando seu nome...")

#nome.upper() transforma tudo em maiúsculas
nomemaiuscula = nome.upper()
print("Seu nome em maiúscilas é {}".format(nomemaiuscula))

#nome.lower() transforma tudo em minúsclos
nomeminusculo = nome.lower()
print("Seu nome minúsculo é {}".format(nomeminusculo))

#nome.count (" ") conta o número de espaços
espc = nome.count(" ")
#o len() conta o tamanho da string
tamnome = len(nome) - espc
print("Seu nome tem ao todo {} letras".format(tamnome))

#nome.split(" ") separa a string por espaços
sepanome = nome.split(" ")
#sepanome[0] pega da lista na posição 0 e começar a contar.
continicio = len(sepanome[0])
print("Seu primeiro nome é {} e ele tem {} letras".format(sepanome[0],continicio))

