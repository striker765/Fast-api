from fastapi import FastAPI, HTTPException
import sqlite3

app = FastAPI()

def obter_procedimento_do_host(nome_do_host: str):
    db = sqlite3.connect('hosts.db')
    cursor = db.cursor()
    cursor.execute('SELECT procedure FROM hosts WHERE name = ?', (nome_do_host,))
    resultado = cursor.fetchone()
    db.close()
    
    if resultado:
        return resultado[0]
    else:
        raise HTTPException(status_code=404, detail="Host não encontrado.")

@app.get("/procedimento/{nome_host}")
def read_procedimento(nome_host: str):
    return {"procedimento": obter_procedimento_do_host(nome_host)}
