# -*- coding: UTF-8 -*-
def listar(nomes):
    print 'Listando nomes: '
    for nome in nomes:
        print nome

def alterar(nomes):
    print 'Qual nome vc gostaria de alterar?'
    novo_nome = raw_input()

    if(novo_nome in nomes):
        posicao = nomes.index(novo_nome)
        print 'Digite novo nome:'
        nome_novo = raw_input()
        nomes[posicao] = nome_novo

def procurar_regex(nomes):
    print('Digite a expressão regular')
    regex = raw_input()
    nomes_concatenados = ' '.join(nomes)
    resultados = re.findall(regex, nomes_concatenados)
    print(resultados)

def procurar(nomes):
    print 'Digite nome a procurar:'
    nome_a_procurar = raw_input()
    if (nomes_a_procurar in nomes):
        print ('Nome %s está na lista' % (nome_a_procurar))
    else:
        print ('Nome %s Não está na lista' % (nome_a_procurar))


def remover(nomes):
    print 'Qual nome você gostaria de remover?'
    nome = raw_input()
    nomes.remove(nome)

def cadastrar(nomes):
        print 'Digite seu nome: '
        nome = raw_input()
        nomes.append(nome)

def menu():
    nomes = []
    escolha = ''
    while (escolha != '0'):
        print 'Digite 1 para Cadastrar , 2 para listar e 0 para finalizar'
        escolha = raw_input()
        if (escolha == '1'):
            cadastrar(nomes)
        if (escolha == '2'):
            listar(nomes)
        if (escolha == '3'):
            remover(nomes)
        if (escolha == '4'):
            alterar(nomes)
        if (escolha == '5'):
            procurar(nomes)
menu()
