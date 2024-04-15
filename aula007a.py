nome = input('Qual é seu nome?')
print('Prazer em te conhecer {}!'.format(nome))
print('Prazer em te conhecer {:20}!'.format(nome)) # com espaço de 20 caracteres
print('Prazer em te conhecer {:>20}!'.format(nome))# > alinhado a direita
print('Prazer em te conhecer {:<20}!'.format(nome)) # < alinhado a esqueda
print('Prazer em te conhecer {:=^20}!'.format(nome))# ^ fica centralizado
print('Prazer em te conhecer {:*^20}!'.format(nome))