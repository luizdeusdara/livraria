import psycopg2
if __name__ == '__main__':
    # Preencher com os parâmetros de conexão do seu banco de dados:
    conexao = psycopg2.connect(host='silly.db.elephantsql.com', database='fqgifeti', user='fqgifeti', password='EvZ7icmEDAGLTasmifQS5iiI1Lk8WHVy')
    print('Conectado ao banco de dados!!!')
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM autores")
    resultados = cursor.fetchall()
    for resultado in resultados:
        print(resultado)
    cursor.close()
    conexao.close()