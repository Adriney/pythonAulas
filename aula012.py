nome  = str(input("Qual é o seu nome? "))
if nome == "Alan":
    print("Que nome bonito!")
elif nome == "Pedro" or nome == "Maria" or nome == "Paulo" or nome == "João" :
    print("Seu nome é bem popular no Brasil.")
elif nome in "Ana Cláudia Jéssica Juliana":
    print("Belo nome feminino")
else:
    print("Seu nome é bem normal.")
    print("tenha um bom dia, {}!".format(nome))