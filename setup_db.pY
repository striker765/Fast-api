import sqlite3

def create_db():
    conn = sqlite3.connect('hosts.db')
    cursor = conn.cursor()

    # Criar a tabela hosts
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS hosts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        procedure TEXT
    )
    ''')

    # Adicionar novos registros
    cursor.executemany(
        'INSERT INTO hosts (name, procedure) VALUES (?, ?)',
        [
            ('MCASSAB37', 'Acionamento: Lucas, número 1987234893547.\n'
                           'Procedimento em caso de alerta:\n'
                           'Verificar conexão de rede e contatar o suporte técnico imediatamente.'),
            ('MCASSAB38', 'Acionamento: Lucas, número 1983234893547.\n'
                           'Procedimento em caso de alerta:\n'
                           'Verificar conexão de rede e contatar o suporte técnico imediatamente.'),
            ('MCASSAB31', 'Acionamento: Lucas, número 1981234893547.\n'
                           'Procedimento em caso de alerta:\n'
                           'Verificar conexão de rede e contatar o suporte técnico imediatamente.'),
            ('MCASSAB40', 'Acionamento: Lucas, número 1980234893547.\n'
                           'Procedimento em caso de alerta:\n'
                           'Verificar conexão de rede e contatar o suporte técnico imediatamente.'),
            ('MCASSAB30', 'Acionamento: Lucas, número 1989234893547.\n'
                           'Procedimento em caso de alerta:\n'
                           'Verificar conexão de rede e contatar o suporte técnico imediatamente.'),
            ('Fast api', (
                'Computador Local (Desenvolvimento e Teste)\n'
                '1. Desenvolver e Testar\n\n'
                'Servidor Remoto (Hospedagem da API)\n'
                '2. Transferir Código\n'
                '    - Conecte-se ao servidor remoto via PuTTY.\n'
                '    - Transfira seu código para o servidor usando scp, SFTP, ou outra ferramenta.\n'
                '      Exemplo com scp:\n'
                '        scp -r /caminho/do/seu/projeto usuario@ip_do_servidor:/caminho/no/servidor\n\n'
                '3. Configurar e Executar a API no Servidor\n'
                '    - Atualize o sistema e instale Python e pip no servidor:\n'
                '        sudo apt update\n'
                '        sudo apt install python3 python3-pip\n'
                '    - Instale as dependências necessárias (FastAPI, Uvicorn):\n'
                '        pip3 install fastapi uvicorn\n'
                '    - Navegue para o diretório onde o código foi transferido:\n'
                '        cd /caminho/no/servidor\n'
                '    - Execute a API com uvicorn:\n'
                '        uvicorn api:app --host 0.0.0.0 --port 8000 --reload\n'
                '    - Configure o firewall do servidor para permitir o tráfego na porta 8000:\n'
                '        sudo ufw allow 8000\n\n'
                '4. Acessar e Testar a API com Postman\n'
                '    - Abra o Postman no seu computador local.\n'
                '    - Crie uma nova requisição HTTP com o método desejado (por exemplo, GET).\n'
                '    - Insira a URL da API no formato:\n'
                '        http://<ip_do_servidor>:8000/procedimento/teste%20de%20pix\n'
                '      Substitua <ip_do_servidor> pelo IP do servidor e <nome_host> pelo nome do host que você deseja consultar.\n'
                '    - Envie a requisição e visualize a resposta da API no Postman.'
            ))
        ]
    )

    conn.commit() 
    conn.close()

if __name__ == '__main__':
    create_db()
