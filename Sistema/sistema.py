import psycopg2 as conector
import tkinter as tk

conexao = conector.connect(
        host="localhost",
        dbname="shantala",
        user="postgres",
        password="12345",
        port="5432",
        options='-c client_encoding=UTF8'
    )
cursor = conexao.cursor()

principal = tk.Tk()
principal.resizable(False, False)
principal.title("Sistema Escola Shantala")
principal.geometry('600x300')
tk.Button(principal, text='Cadastrar Aluno',command=principal.quit).grid(row=1,column=0,sticky=tk.W,pady=4)
tk.Button(principal, text='Cadastrar Curso',command=principal.quit).grid(row=1,column=1,sticky=tk.W,pady=4)
tk.Button(principal, text='Cadastrar Turma',command=principal.quit).grid(row=1,column=2,sticky=tk.W,pady=4)
tk.Button(principal, text='Cadastrar Professor',command=principal.quit).grid(row=1,column=3,sticky=tk.W,pady=4)
tk.Button(principal, text='Cadastrar Aluno na turma',command=principal.quit).grid(row=1,column=4,sticky=tk.W,pady=4)
tk.Label(principal,text="Cadastrar: ").grid(row=2, column=0)
tk.Label(principal,text="Nome:").grid(row=3,column=0)
nome = tk.Entry(principal)
nome.grid(row=3, column=0)
tk.Button(principal, text='Sair',command=principal.quit).grid(row=5,column=1,sticky=tk.W,pady=4)
principal.mainloop()

comando = '''INSERT INTO professores (nomeprofessor) VALUES ('Gloria Duarte Almeida ');''' 
cursor.execute(comando)

conexao.commit()

cursor.close()
conexao.close()