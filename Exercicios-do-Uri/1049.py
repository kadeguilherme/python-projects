animal = str(input(""))

tipoanimal = str(input(""))

alimento = str(input(""))

if (animal == "vertebrado"):

    if (tipoanimal == "ave"):

        if( alimento == "carnivoro"):
            print("aguia")

        elif(alimento == "onivo"):
            print("pomba")

    elif(tipoanimal == "mamifero"):

        if(alimento == "onivoro"):
            print("homem")

        elif(alimento == "herbivero"):
            print("vaga")


elif(animal == "invertebrado"):

    if(tipoanimal == "inseto"):

        if(alimento == "hemafogo"):
            print("pulga")

        elif(alimento == "herbivero"):
            print("lagarta")

    elif(tipoanimal =="anelideo"):

        if(alimento == "hematofogo"):
            print("sanguesusga")

        elif(alimento == "onivoro"):
            print("minhoca")