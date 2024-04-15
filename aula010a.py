ano = int(input("qual o ano do seu veículo: "))
tempo = 2024 - ano
print("Seu veículo possui {} anos de uso".format(tempo))
if tempo <=3:
    print("É considerado um carro novo")
else:
    print("É considerado um carro velho")
print("--FIM--")