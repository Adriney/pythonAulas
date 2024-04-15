#tipos de fatiamento

#frase
#[C][u][r][s][o][][e][m][][V][i][d][e][o][][P][y][t][h][o][n]
# 0  1  2  3  4  5 6  7  8 9 10 11 12 13 14 15 16 17 18 19 20
#
#frase[9]    =   v (corespode a letra no espaço numerado)
#frase[9:14] = Video (corresponde do espaço 9, abaixo do 14)
#frase[9:21:2] = Vdopto (vai pular as casas de 2 em 2)
#frase[:5]  = Curso (do inicio ate abaixo de 5)
#frase[15:] = Python (da casa 15 até o final)
#frase[9::3] = VePh (mostra a casa 9 e vai pulando de 3 em 3 até o final.
#
# ANALISE DE FRASE
#  len(frase)  = 21 caracteres(Analisa a frase e diz quantos caracteres possui)
# frase.cont("o") = 3 (diz quantas vezes tem a letra)
# frase.cont('o',0,13) = 1 (diz quantas vezes tem a letra, lembrando que o ultimo caractere é ignorado)
# frase.find('deo') = 11 = (diz em que momento começou a frase)
# frase.find('Android') = -1 (-1 significa que a palavra não foi encontrada(lembrando que começa em 0))
# 'Curso'in frase = True  (pede se existe a palavra dentro da frase)
#
#TRANSFORMAÇÃO
#  frase.replace('Python','Android') = vai substituir  a palavra Python por Android
# frase.upper() = deixa a frase toda em maiúsculas(exceto o que já esta em maiúscula)
# frase.lower() = deixa a frase toda em minúsculas(exceto o que já esta em minúscula)
# frase.capitalize() =  deixa a frase toda em minúscula, e a primeira letra em maiúscula
#frase.title() =  deixa todas as palavras com a primeira letra em maiúscula
#frase.strip() = remove espaços inuteis antes e/ou depois da  frase
#frase.rstrip() = remove  espaço(os últimos espaços da frase) lado direito da frase
#frase.lstrip() = remove espaço(os primeiros espaços da frase) lado esquerdo da frase
#
#DIVISÃO
# frase.split() =  é um método em Python que divide uma string em uma lista de substrings com base em um delimitador especificado.
#JUNÇÃO
# '-'.join(frase) = junta as palavras e divide por um traço