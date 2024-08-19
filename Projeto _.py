import sqlite3
import os
from colorama import Fore, Style, init

# Inicializa a biblioteca colorama
init(autoreset=True)

def limpar_tela():

    sistema = os.name
    if sistema == 'nt':
        os.system('cls')
    else:
        os.system('clear')




def deletar_host(db, nome_do_host):
    cursor = db.cursor()
    cursor.execute("DELETE FROM tabela_hosts WHERE nome_host = ?", (nome_do_host,))
    db.commit()
    print(Fore.GREEN + f'Host "{nome_do_host}" deletado com sucesso!' + Style.RESET_ALL)



def obter_procedimento_do_host(db, nome_do_host):
    cursor = db.cursor()
    cursor.execute('SELECT procedure FROM hosts WHERE name = ?', (nome_do_host,))
    resultado = cursor.fetchone()
    if resultado:
        return resultado[0]
    else:
        return 'Host não encontrado.'

def adicionar_host(db, nome_do_host, procedimento):
    cursor = db.cursor()
    cursor.execute('INSERT INTO hosts (name, procedure) VALUES (?, ?)', (nome_do_host, procedimento))
    db.commit()
    print(Fore.GREEN + 'Host adicionado com sucesso!' + Style.RESET_ALL)

def alterar_host(db, nome_do_host, novo_procedimento):
    cursor = db.cursor()
    cursor.execute('UPDATE hosts SET procedure = ? WHERE name = ?', (novo_procedimento, nome_do_host))
    if cursor.rowcount > 0:
        db.commit()
        print(Fore.GREEN + 'Host alterado com sucesso!' + Style.RESET_ALL)

    else:
        print(Fore.RED + 'Host não encontrado para alteração.' + Style.RESET_ALL)


def main():
    try:
        db = sqlite3.connect('hosts.db')
        
        while True:
            print(Fore.YELLOW + "Menu de opções:" + Style.RESET_ALL)
            print(Fore.GREEN +"1. Adicionar Host|")

            print(Fore.GREEN +"2. Alterar Host  ")

            print(Fore.GREEN +"3. Buscar Host   ")

            print(Fore.GREEN +"4. Deletar Host  ")

            print(Fore.GREEN +"5. Limpar Tela   ")

            print(Fore.GREEN +"6. Sair          ")


            
            opcao = input(Fore.GREEN + "Digite a opção desejada: " + Style.RESET_ALL).strip()
            limpar_tela()
            
            if opcao == '1':
                nome_do_host = input(Fore.YELLOW + "Digite o nome do novo Host: " + Style.RESET_ALL).strip()
                procedimento = input(Fore.YELLOW + "Digite o procedimento do Host: " + Style.RESET_ALL).strip()
                adicionar_host(db, nome_do_host, procedimento)
                
            elif opcao == '2':
                nome_do_host = input(Fore.YELLOW + "Digite o nome do Host que deseja alterar: " + Style.RESET_ALL).strip()
                novo_procedimento = input(Fore.YELLOW + "Digite o novo procedimento para o Host: " + Style.RESET_ALL).strip()
                alterar_host(db, nome_do_host, novo_procedimento)
                
            elif opcao == '3':
                nome_do_host = input(Fore.YELLOW + "Digite o nome do Host para buscar: " + Style.RESET_ALL).strip()
                procedimento = obter_procedimento_do_host(db, nome_do_host)
                print(Fore.CYAN + f'Procedimento para {nome_do_host}:\n{Style.RESET_ALL}{procedimento}')

            elif opcao == '4':
                nome_do_host = input(Fore.GREEN + "Digite o nome do Host que deseja deletar: " + Style.RESET_ALL).strip()
                deletar_host(db, nome_do_host)

            elif opcao == '5':
                limpar_tela()

                
            elif opcao == '6':
                break
            
            else:
                print(Fore.RED + "Opção inválida. Tente novamente." + Style.RESET_ALL)
    
    except sqlite3.Error as e:
        print(Fore.RED + f"Erro ao acessar o banco de dados: {e}" + Style.RESET_ALL)
    
    finally:
        if db:
            db.close()

if __name__ == '__main__':
    main()


# http://localhost:8000/procedimento/tst

# uvicorn api:app --host 0.0.0.0 --port 8000 --reload