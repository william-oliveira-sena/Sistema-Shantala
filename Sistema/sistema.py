from turtle import right
import psycopg2 as conector
import tkinter as tk
import pyautogui


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
        
        nomeProfessor = nome.get()
        dados = (nomeProfessor ,)
        conectarBanco()
        
        cursor = conexao.cursor() 
        comando = """INSERT INTO "professores" ("nomeprofessor") VALUES (%s)"""
             
        cursor.execute(comando, dados)
        conexao.commit() 
        count = cursor.rowcount

        if count > 0:
        
            screenWidth, screenHeight = pyautogui.size()
            currentMouseX, currentMouseY = pyautogui.position()
            pyautogui.moveTo(100, 150)
            pyautogui.click()
            pyautogui.click(100, 200)
            pyautogui.move(0, 10)
            pyautogui.doubleClick()
            pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)
            pyautogui.write('Cadastro Realizado com sucesso!', interval=0.25)
            pyautogui.press('esc')
            pyautogui.keyDown('shift')
            pyautogui.press(['left', 'left', 'left', 'left'])
            pyautogui.keyUp('shift')
            pyautogui.hotkey('ctrl', 'c')
            pyautogui.alert('Cadastro Realizado com sucesso!') 

        cursor.close()
        conexao.close()    

             

    tk.Button(cadastrarprofessores, text='Cadatrar',command=cadastrarprofessor).grid(row=5,column=0,sticky=tk.W,pady=4)
    tk.Button(cadastrarprofessores, text='Sair',command=cadastrarprofessores.destroy).grid(row=5,column=1,sticky=tk.W,pady=4)

    cadastrarprofessores.mainloop()

    #alunos

def cadastrarAluno():
    
    cadastrarAluno = tk.Tk()
    cadastrarAluno.resizable(False, False)
    cadastrarAluno.title("Sistema Escola Shantala")
    cadastrarAluno.geometry('600x300')
    tk.Label(cadastrarAluno,text="Cadastrar Alunos: ").grid(row=2, column=0)
    tk.Label(cadastrarAluno,text="Nome Aluno").grid(row=3,column=0)
    tk.Label(cadastrarAluno,text="Endereço").grid(row=4,column=0)
    tk.Label(cadastrarAluno,text="Número").grid(row=5,column=0)
    tk.Label(cadastrarAluno,text="Complemento").grid(row=6,column=0)
    tk.Label(cadastrarAluno,text="Bairro").grid(row=7,column=0)
    tk.Label(cadastrarAluno,text="telefone").grid(row=8,column=0)
    tk.Label(cadastrarAluno,text="Data Nascimento").grid(row=9,column=0)
    tk.Label(cadastrarAluno,text="CPF").grid(row=10,column=0)
    tk.Label(cadastrarAluno,text="RG").grid(row=11,column=0)
    tk.Label(cadastrarAluno,text="Cadastro Unico").grid(row=12,column=0)
    nome = tk.Entry(cadastrarAluno)
    nome.grid(row=3, column=1)
    endereco = tk.Entry(cadastrarAluno)
    endereco.grid(row=4, column=1)
    numero = tk.Entry(cadastrarAluno)
    numero.grid(row=5, column=1)
    complemento = tk.Entry(cadastrarAluno)
    complemento.grid(row=6, column=1)
    bairro = tk.Entry(cadastrarAluno)
    bairro.grid(row=7, column=1)
    telefone = tk.Entry(cadastrarAluno)
    telefone.grid(row=8, column=1)
    dataNascimento = tk.Entry(cadastrarAluno)
    dataNascimento.grid(row=9, column=1)
    cpf = tk.Entry(cadastrarAluno)
    cpf.grid(row=10, column=1)
    rg = tk.Entry(cadastrarAluno)
    rg.grid(row=11, column=1)
    cu = tk.Entry(cadastrarAluno)
    cu.grid(row=12, column=1)
    
   
    

    def cadastraraluno():              
        nomeAluno = nome.get()
        enderecoAluno = endereco.get()
        numeroAluno = numero.get()
        complementoAluno = complemento.get()
        bairroAluno = bairro.get()
        telefoneAluno = telefone.get()
        dataNascimentoAluno = dataNascimento.get()
        cpfAluno = cpf.get()
        rgAluno = rg.get()
        cuAluno = cu.get()
        dados = (nomeAluno,enderecoAluno,numeroAluno,complementoAluno,bairroAluno,telefoneAluno,dataNascimentoAluno,cpfAluno,rgAluno,cuAluno, )
        conectarBanco()
        
        cursor = conexao.cursor() 
        comando = """INSERT INTO "alunos" ("nomealuno","endereco","numero","complemento","bairro","telefone","datanascimento","cpf","rg","cu") VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
             
        cursor.execute(comando, dados)
        conexao.commit() 
        count = cursor.rowcount
       

        cursor.close()
        conexao.close()    

             

    tk.Button(cadastrarAluno, text='Cadatrar',command=cadastraraluno).grid(row=14,column=0,sticky=tk.W,pady=4)
    tk.Button(cadastrarAluno, text='Sair',command=cadastrarAluno.destroy).grid(row=14,column=1,sticky=tk.W,pady=4)

    cadastrarAluno.mainloop()




principal = tk.Tk()
principal.resizable(False, False)
principal.title("Sistema Escola Shantala")
principal.geometry('600x300')
tk.Button(principal, text='Cadastrar Aluno',command=cadastrarAluno).grid(row=1,column=0,sticky=tk.W,pady=4)
tk.Button(principal, text='Cadastrar Curso',command=principal.quit).grid(row=1,column=1,sticky=tk.W,pady=4)
tk.Button(principal, text='Cadastrar Turma',command=principal.quit).grid(row=1,column=2,sticky=tk.W,pady=4)
tk.Button(principal, text='Cadastrar Professor',command=cadastrarProfessores).grid(row=1,column=3,sticky=tk.W,pady=4)
tk.Button(principal, text='Cadastrar Aluno na turma',command=principal.quit).grid(row=1,column=4,sticky=tk.W,pady=4)
tk.Button(principal, text='Sair',command=principal.quit).grid(row=1,column=5,sticky=tk.W,pady=4)

principal.mainloop()