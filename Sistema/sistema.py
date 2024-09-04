import psycopg2 as conector
import tkinter as tk

def conectarBanco():   
   global conexao
   conexao = conector.connect(
            host="localhost",
            dbname="shantala",
            user="postgres",
            password="12345",
            port="5432",
            options='-c client_encoding=UTF8'
        )

def cadastrarProfessores():
    
    cadastrarprofessores = tk.Tk()
    cadastrarprofessores.resizable(False, False)
    cadastrarprofessores.title("Sistema Escola Shantala")
    cadastrarprofessores.geometry('600x300')
    tk.Label(cadastrarprofessores,text="Cadastrar Professores: ").grid(row=2, column=0)
    tk.Label(cadastrarprofessores,text="Nome Professor").grid(row=3,column=0)
    nome = tk.Entry(cadastrarprofessores)
    nome.grid(row=3, column=1)

    def cadastrarprofessor():              
        nome_professor = nome.get()  # Pega o valor do campo de entrada
        dados = (nome_professor,)  # Cria uma tupla com o valor
        
        conectarBanco()
        cursor = conexao.cursor() 
        comando = """INSERT INTO "professores" ("nomeprofessor") VALUES (%s)"""
        cursor.execute(comando, dados)
        conexao.commit() 
        cursor.close()
        conexao.close()    

    tk.Button(cadastrarprofessores, text='Cadastrar', command=cadastrarprofessor).grid(row=5,column=0,sticky=tk.W,pady=4)
    tk.Button(cadastrarprofessores, text='Sair', command=cadastrarprofessores.destroy).grid(row=5,column=1,sticky=tk.W,pady=4)

    cadastrarprofessores.mainloop()

principal = tk.Tk()
principal.resizable(False, False)
principal.title("Sistema Escola Shantala")
principal.geometry('600x300')
tk.Button(principal, text='Cadastrar Aluno', command=principal.quit).grid(row=1,column=0,sticky=tk.W,pady=4)
tk.Button(principal, text='Cadastrar Curso', command=principal.quit).grid(row=1,column=1,sticky=tk.W,pady=4)
tk.Button(principal, text='Cadastrar Turma', command=principal.quit).grid(row=1,column=2,sticky=tk.W,pady=4)
tk.Button(principal, text='Cadastrar Professor', command=cadastrarProfessores).grid(row=1,column=3,sticky=tk.W,pady=4)
tk.Button(principal, text='Cadastrar Aluno na turma', command=principal.quit).grid(row=1,column=4,sticky=tk.W,pady=4)
tk.Button(principal, text='Sair', command=principal.quit).grid(row=1,column=5,sticky=tk.W,pady=4)

principal.mainloop()
