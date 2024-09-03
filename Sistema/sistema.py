import psycopg2 as conector
import tkinter 

conexao = conector.connect(
        host="localhost",
        dbname="Shantala",
        user="postgres",
        password="12345",
        port="5432",
        options='-c client_encoding=UTF8'
    )
cursor = conexao.cursor()

comando = '''INSERT INTO professores (idprofessor,nomeprofessor) VALUES ('1','Julio Henrique Sosa');''' 
cursor.execute(comando)

conexao.commit()

cursor.close()
conexao.close()