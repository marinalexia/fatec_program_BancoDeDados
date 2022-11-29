#2 Escreva um programa para armazenar uma agenda de telefones em um dicionário. 
#Cada pessoa pode ter um ou mais telefones e a chave do dicionário é o nome da 
#pessoa. Seu programa deve ter as seguintes funções:

agenda = {
    "Carol Marques": {
        "Telefone 1": "1234-5689", 
        "Telefone 2": "3456-7344"
        }, 
    "Mauricio Teles": {
        "Telefone 1": "6789-0456",
        "Telefone 2": "4567-8342"
        }
    }

telefone1 = str
telefone2 = str

def incluirNovoNome():
#essa função acrescenta um novo nome na agenda, com um ou 
#mais telefones. Ela deve receber como argumentos o nome e os telefones
    nome = str(input("Digite um Nome: "))
    telefone1 = str(input("Digite o primeiro telefone: "))
    agenda[nome] = {"Telefone 1": telefone1} #adiciona o primeiro telefone como um item dentro do dicionario nome
    print(agenda)
    resposta = str(input("Deseja adicionar mais um telefone? "))
    if resposta == "Sim" and "sim":
        telefone2 = str(input("Digite o segundo telefone: "))
        agenda[nome].update({"Telefone 2": telefone2}) #adiciona mais um item ao nome
        print(nome)
    else:
        print("Contato adicionado.")
    print(agenda)
    return agenda


def incluirTelefone():
#essa função acrescenta um telefone em um nome existente na agenda. Caso o nome não 
# exista na agenda, voc deve perguntar se a pessoa deseja ê̂ deve perguntar se a pessoa deseja inclui-lo. 
# Caso a resposta seja afirmativa, use a função anterior para incluir o novo nome.
    print(agenda)
    pesquisaNome = str(input("Digite o nome do contato que vocÊ gostaria de adicionar o telefone: "))  
    if agenda.get(pesquisaNome):
        telefone2 = str(input("O contato já existe. Digite o telefone a ser adicionado: "))
        agenda[pesquisaNome].update({"Telefone 2": telefone2})
            #adicionar telefone
    else:
        respostaTelefone = str(input("O contato ainda não existe em sua agenda. Gostaria de incluir? "))
        if respostaTelefone == "Sim":
            incluirNovoNome()   
        else:
            print("ação concluída.") 
    print(agenda)
    return agenda

def excluirTelefone():
#essa função exclui um telefone de uma pessoa que já está na 
#agenda. Se a pessoa tiver apenas um telefone, ela deve ser excluída da agenda.
    contatoExcluido = str(input("Qual contato você gostaria de excluir o número? "))
    if agenda.get(contatoExcluido):
        if len(agenda[contatoExcluido]) > 1:
            agenda[contatoExcluido].pop("Telefone 2")
            print("Telefone 2 exclúido do contato.")
        else:
            agenda.pop(contatoExcluido)
            print("O contato só possui um telefone e foi exclúido da agenda")
    else:
        print("O contato não existe na agenda")
    print(agenda)
    return agenda


def excluirNome():
# excluirNome – essa função exclui uma pessoa da agenda.
    excluirPessoa = str(input("Qual contato você deseja deletar da agenda? "))
    if agenda.get(excluirPessoa):
        agenda.pop(excluirPessoa)
        print(agenda)
    else:
        print("O contato não existe.")
    return agenda

def consultarTelefone():
    # consultarTelefone – essa função retorna os telefones de uma pessoa na 
    numeroConsulta = str(input("Qual contato você deseja consultar? "))
    if agenda.get(numeroConsulta):
        print(agenda.get(numeroConsulta))
    else:
        print("O contato não existe")
    return agenda


incluirNovoNome()
incluirTelefone()
excluirTelefone()
excluirNome()
consultarTelefone()
print(agenda)
