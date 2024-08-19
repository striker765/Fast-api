import sqlite3
from colorama import Fore, Style, init

# Inicializa a biblioteca colorama
init(autoreset=True)

def obter_procedimento_do_host(db, nome_do_host):
    cursor = db.cursor()
    cursor.execute('SELECT procedure FROM hosts WHERE name = ?', (nome_do_host,))
    resultado = cursor.fetchone()
    
    if resultado:
        return resultado[0]
    else:
        return 'Host não encontrado.'

def main():
    try:
        db = sqlite3.connect('hosts.db')
        
        while True:
            entrada_usuario = input(Fore.GREEN + "Digite uma opção ou nome de um Host (ou 'exit' para sair): " + Style.RESET_ALL).strip()
            if entrada_usuario.lower() == 'exit':
                break
            
            procedimento = obter_procedimento_do_host(db, entrada_usuario)
            print(Fore.CYAN + f'Procedimento para {entrada_usuario}:\n{Style.RESET_ALL}{procedimento}')
    
    except sqlite3.Error as e:
        print(Fore.RED + f"Erro ao acessar o banco de dados: {e}" + Style.RESET_ALL)
    
    finally:
        if db:
            db.close()

if __name__ == '__main__':
    main()
