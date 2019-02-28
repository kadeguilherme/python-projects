nome = input ("Digite seu nome completo : ").strip()

print("\nAnalisando seu nome...\n")

maior = nome.upper()
print("Seu nome maiúscula é : {}".format(maior))

menor = nome.lower()
print("Seu nome minúsculo é : {}".format(menor))

espacos = nome.count(" ")
total = len(nome)
print("Seu nome tem ao todo {} letras".format(total - espacos))

fistname = nome.split(" ")
tam = len(fistname[0])

print("Seu primeiro nome é {} e ele tem {} letras".format(fistname[0],tam))