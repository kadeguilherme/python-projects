num = int(input("Digite o numero para começar a tabuada: "))
print("-"*15)

for n in range(0,11,1):
    r = num * n
    print("{} x {:2} = {} ".format(num, n, r))
print("-"*15)