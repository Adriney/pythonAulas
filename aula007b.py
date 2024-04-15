n1 = int(input('Digite um valor:'))
n2 = int(input('Outro valor:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {},\n o produto é {},\n e a divisão é {:.3f}'.format(s,m,d), end=' >*> ')
#{:.3f} depois do pnto 3 casas decimais
# \n serve para quebrar a linha
# , end='' é usado para manter a resposta somente em uma linha
print('Divisão inteira {} e potência {}'.format(di, e))
