import requests, json
import os

def mostrar_opcoes():
    print("1. Listar")
    print("2. Sair")

tabelas = ["TipoItem", "Item", "Local", "TipoEntidade", "Entidade", "Inimigo", "Personagem", "Quest", "NPC", "Jogo"]
def mostrar_tabelas():
    for i in range(len(tabelas)):
        print(str(i)+". "+tabelas[i])

def listar_tabela(tabela):
    res = requests.get("http://localhost:4999/listar/"+tabelas[tabela])
    res_json = json.dumps(res.json()["lista"], indent=4, ensure_ascii=False)
    limpar_terminal()
    print(res_json)

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

done = False
while not done:
    mostrar_opcoes()
    entrada = int(input("Selecione uma das opções: "))
    if entrada == 1:
        limpar_terminal()
        mostrar_tabelas()
        tabela = int(input("Selecione uma das tabelas para listar: "))
        if tabela < 0 or tabela > len(tabelas)-1:
            print("Número inválido!")
        else:
            limpar_terminal()
            print("Carregando...")
            listar_tabela(tabela)
    elif entrada == 2:
        limpar_terminal()
        exit()
    else:
        print("Opção inválida!")
