import math
num = int(input("Digite um número: "))
raiz = math.sqrt(num)
print("A raiz de {} é igual a {:.2f}".format(num, raiz))
print("A raiz de {} é igual a {}".format(num,math.ceil(raiz)))#arendodar pra cima
print("A raiz de {} é igual a {}".format(num,math.floor(raiz)))#rendodar pra baixo
