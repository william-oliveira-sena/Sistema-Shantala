from turtle import right
import psycopg2 as conector
import tkinter as tk
from tkinter import ttk
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
#função de mensagem na tela, recebe o texto que deve ser apresentado
def msg(alerta):
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
    pyautogui.alert(alerta)

#função para pesquisar dados para os campos select
def pesquisar(comandopesq):
    conectarBanco()
    cursor = conexao.cursor() 
    comando = comandopesq
    cursor.execute(comando)
    registros = cursor.fetchall()
    return registros

#função pesquisar o id com o nome 
def pesquisarid(comandopesq, nome):
    conectarBanco()
    cursor = conexao.cursor()
    cursor.execute(comandopesq, nome)
    registros = cursor.fetchall()
    return registros  
      
#função cadastrar professores
def cadastrarProfessores():
    cadastrarprofessores = tk.Tk()
    cadastrarprofessores.resizable(False, False)
    cadastrarprofessores.title("Sistema Escola Shantala")
    cadastrarprofessores.geometry('600x300')
    tk.Label(cadastrarprofessores, text="Cadastrar Professores: ").grid(row=2, column=0)
    tk.Label(cadastrarprofessores, text="Nome Professor").grid(row=3, column=0)
    nome = tk.Entry(cadastrarprofessores)
    nome.grid(row=3, column=1)

    def cadastrarprofessor():          
        nomeProfessor = nome.get()
        dados = (nomeProfessor,)
        conectarBanco()
        cursor = conexao.cursor() 
        comando = """INSERT INTO "professores" ("nomeprofessor") VALUES (%s)"""
        cursor.execute(comando, dados)
        conexao.commit()
        count = cursor.rowcount

        if count > 0:
            alerta = "Cadastro Realizado com Sucesso!"
            msg(alerta)
            cadastrarprofessores.destroy()

        cursor.close()
        conexao.close()    

    tk.Button(cadastrarprofessores, text='Cadastrar', command=cadastrarprofessor).grid(row=5, column=0, sticky=tk.W, pady=4)
    tk.Button(cadastrarprofessores, text='Sair', command=cadastrarprofessores.destroy).grid(row=5, column=1, sticky=tk.W, pady=4)

    cadastrarprofessores.mainloop()
def editarProfessores():
    print ("editando")

def on_item_selected(event):
    selected_item = treeview.selection()
    if selected_item:
        item = treeview.item(selected_item)
        item_text = item['values']
        print("Selecionado:", item_text)

def professores():
      #tk.Button(editarprofessor, text='Editar', command=editarprofessor.destroy).grid(row=14, column=1, sticky=tk.W, pady=4)
    global treeview

    root=tk.Tk()
    root.title("Pesquisa Professores")

    root.geometry("800x600")

    width = root.winfo_width()
    height = root.winfo_height()

    frame = tk.Frame(root)
    frame.pack(side="right", fill="both", expand=True)

    vsb = tk.Scrollbar(frame, orient="vertical")
    vsb.pack(side='right', fill='y')

    hsb = tk.Scrollbar(frame, orient="horizontal")
    hsb.pack(side='bottom', fill='x')

    # Criação do Treeview
    treeview = ttk.Treeview(frame, columns=("ID Professor", "Nome Professor"), show='headings', yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    # Definir os cabeçalhos das colunas
    treeview.heading("ID Professor", text="ID Professor")
    treeview.heading("Nome Professor", text="Nome Professor")
    
    vsb.config(command=treeview.yview)
    hsb.config(command=treeview.xview)

# Adicionar algumas linhas de dados
    comandopesq= """SELECT * FROM professores"""
    data = pesquisar(comandopesq)

    for item in data:
        treeview.insert("", "end", values=item)
    
    treeview.config(height=15)

#Adicionar um binding para a seleção dos itens
    treeview.bind("<<TreeviewSelect>>", on_item_selected)
# adicionar a função de editar aqui para chamar nova tela e editar

# Exibir o Treeview na janela
    treeview.pack(fill="both", expand=True, padx=10, pady=10)
    
   # tk.Label(editarProfessores, text="Cadastrar Professores: ").grid(row=2, column=0)
    #tk.Label(editarProfessores, text="Nome Professor").grid(row=3, column=0)
   # nome = tk.Entry(editarProfessores)
    #nome.grid(row=3, column=1)
    tk.Button(root, text='Editar', command=editarProfessores).pack(pady=100)
    tk.Button(root, text='Cadastrar', command=cadastrarProfessores).pack(pady=100)

# Executar a interface gráfica
    root.mainloop()

# Função para cadastrar Alunos
def cadastrarAluno():
    cadastrarAluno = tk.Tk()
    cadastrarAluno.resizable(False, False)
    cadastrarAluno.title("Sistema Escola Shantala")
    cadastrarAluno.geometry('600x300')
    tk.Label(cadastrarAluno, text="Cadastrar Alunos: ").grid(row=2, column=0)
    tk.Label(cadastrarAluno, text="Nome Aluno").grid(row=3, column=0)
    tk.Label(cadastrarAluno, text="Endereço").grid(row=4, column=0)
    tk.Label(cadastrarAluno, text="Número").grid(row=5, column=0)
    tk.Label(cadastrarAluno, text="Complemento").grid(row=6, column=0)
    tk.Label(cadastrarAluno, text="Bairro").grid(row=7, column=0)
    tk.Label(cadastrarAluno, text="Telefone").grid(row=8, column=0)
    tk.Label(cadastrarAluno, text="Data Nascimento").grid(row=9, column=0)
    tk.Label(cadastrarAluno, text="CPF").grid(row=10, column=0)
    tk.Label(cadastrarAluno, text="RG").grid(row=11, column=0)
    tk.Label(cadastrarAluno, text="Cadastro Único").grid(row=12, column=0)
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
        dados = (nomeAluno, enderecoAluno, numeroAluno, complementoAluno, bairroAluno, telefoneAluno, dataNascimentoAluno, cpfAluno, rgAluno, cuAluno)
        conectarBanco()
        cursor = conexao.cursor()
        comando = """INSERT INTO "alunos" ("nomealuno", "endereco", "numero", "complemento", "bairro", "telefone", "datanascimento", "cpf", "rg", "cu") 
                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(comando, dados)
        conexao.commit()
        count = cursor.rowcount
        if count > 0:
            alerta = "Cadastro Realizado com Sucesso!"
            msg(alerta)
            cadastrarAluno.destroy()

        cursor.close()
        conexao.close()    

    tk.Button(cadastrarAluno, text='Cadastrar', command=cadastraraluno).grid(row=14, column=0, sticky=tk.W, pady=4)
    tk.Button(cadastrarAluno, text='Sair', command=cadastrarAluno.destroy).grid(row=14, column=1, sticky=tk.W, pady=4)

    cadastrarAluno.mainloop()

# Função para cadastrar Turmas
def cadastrarTurma():
    cadastrarTurmas = tk.Tk()
    cadastrarTurmas.resizable(False, False)
    cadastrarTurmas.title("Sistema Escola Shantala")
    cadastrarTurmas.geometry('600x300')
    tk.Label(cadastrarTurmas, text="Cadastrar Turma: ").grid(row=2, column=0)
    tk.Label(cadastrarTurmas, text="Curso").grid(row=3, column=0)
    tk.Label(cadastrarTurmas, text="Professor").grid(row=4, column=0)
    tk.Label(cadastrarTurmas, text="Frequência").grid(row=5, column=0)
    tk.Label(cadastrarTurmas, text="Data Início").grid(row=6, column=0)
   
    comandopesqcursos = """SELECT nomecurso FROM cursos"""
    cursos = pesquisar(comandopesqcursos)
    comandopesqprof = """SELECT nomeprofessor FROM professores"""
    prof = pesquisar(comandopesqprof)
    comandopesqfreq = """SELECT nomedias FROM frequencia"""
    frequencia = pesquisar(comandopesqfreq)

    ncurso = tk.StringVar()
    escolhacurso = ttk.Combobox(cadastrarTurmas, width=27, textvariable=ncurso)
    escolhacurso['values'] = cursos
    escolhacurso.grid(column=1, row=3)
    escolhacurso.current()

    prof = tuple(p[0].strip("''") for p in prof)
    print(frequencia)
    nprofe = tk.StringVar()
    escolhaprofessor = ttk.Combobox(cadastrarTurmas, width=27, textvariable=nprofe)
    escolhaprofessor['values'] = prof
    escolhaprofessor.grid(column=1, row=4)
    escolhaprofessor.current()

    frequencia = tuple(f[0].strip("''") for f in frequencia)
    nfreq = tk.StringVar()
    escolhafrequencia = ttk.Combobox(cadastrarTurmas, width=27, textvariable=nfreq)
    escolhafrequencia['values'] = frequencia
    escolhafrequencia.grid(column=1, row=5)
    escolhafrequencia.current()

    datainicio = tk.Entry(cadastrarTurmas)
    datainicio.grid(row=6, column=1)

    def cadastrarturma():              
        nomec = escolhacurso.get()
        nomeCurso = (nomec,)
        nomeP = escolhaprofessor.get()
        nomeProf = (nomeP,)
        nomef = escolhafrequencia.get()
        nomefreque = (nomef,)
        inicio = datainicio.get()

        conectarBanco()
        cursor = conexao.cursor()

        # Pesquisando IDs
        comandopesquisaidcursos = """SELECT idcurso FROM cursos WHERE nomecurso LIKE %s"""
        resultcurso = pesquisarid(comandopesquisaidcursos, nomeCurso)
        if len(resultcurso) == 0:
            alertamsg="Curso não encontrado"
            msg(alertamsg)
            return
        idcurso = resultcurso[0]

        comandopesquisaidprof = """SELECT idprofessores FROM professores WHERE nomeprofessor LIKE %s"""
        resultprof = pesquisarid(comandopesquisaidprof, nomeProf)
        if len(resultprof) == 0:
            alertamsg = "Professor não encontrado"
            msg(alertamsg)
            return
        idprof = resultprof[0]

        comandopesquisaidfreq = """SELECT idfrequencia FROM frequencia WHERE nomedias LIKE %s"""
        resultfreq = pesquisarid(comandopesquisaidfreq, nomefreque)
        if len(resultfreq) == 0:
            alertamsg = "Frequência não encontrada"
            msg(alertamsg)
            return
        idfreq = resultfreq[0]

        cursor = conexao.cursor()
        comando = """INSERT INTO "turmas" ("idcurso", "idprofessor", "idfrequencia", "datainicio") VALUES (%s, %s, %s, %s)"""
        dados = (idcurso, idprof, idfreq, inicio)
        cursor.execute(comando, dados)
        conexao.commit()
        count = cursor.rowcount
        if count > 0:
            alerta = "Cadastro Realizado com Sucesso!"
            msg(alerta)
            cadastrarTurmas.destroy()

        cursor.close()
        conexao.close()    

    tk.Button(cadastrarTurmas, text='Cadastrar', command=cadastrarturma).grid(row=10, column=0, sticky=tk.W, pady=4)
    tk.Button(cadastrarTurmas, text='Sair', command=cadastrarTurmas.destroy).grid(row=10, column=1, sticky=tk.W, pady=4)

    cadastrarTurmas.mainloop()

# Função para cadastrar Cursos
def cadstrarCurso():
    cadstrarCurso = tk.Tk()
    cadstrarCurso.resizable(False, False)
    cadstrarCurso.title("Sistema Escola Shantala")
    cadstrarCurso.geometry('600x300')
    tk.Label(cadstrarCurso, text="Cadastrar curso: ").grid(row=2, column=0)
    tk.Label(cadstrarCurso, text="Nome Curso ").grid(row=3, column=0)
    tk.Label(cadstrarCurso, text="Duração").grid(row=4, column=0)

    curso = tk.Entry(cadstrarCurso)
    curso.grid(row=3, column=1)
    duracao = tk.Entry(cadstrarCurso)
    duracao.grid(row=4, column=1)

    def cadastrarcurso():              
        conectarBanco()
        cursor = conexao.cursor()
        comando = """INSERT INTO "cursos" ("nomecurso", "duracao") VALUES (%s, %s)"""
        dados = (curso.get(), duracao.get())
        cursor.execute(comando, dados)
        conexao.commit()
        count = cursor.rowcount
        if count > 0:
            alerta = "Cadastro Realizado com Sucesso!"
            msg(alerta)
            cadstrarCurso.destroy()

        cursor.close()
        conexao.close()    

    tk.Button(cadstrarCurso, text='Cadastrar', command=cadastrarcurso).grid(row=6, column=0, sticky=tk.W, pady=4)
    tk.Button(cadstrarCurso, text='Sair', command=cadstrarCurso.destroy).grid(row=6, column=1, sticky=tk.W, pady=4)

    cadstrarCurso.mainloop()

# Função para cadastrar Aluno em Turma
def cadastrarAlunoTurma():
    cadastrarAlunoTurma = tk.Tk()
    cadastrarAlunoTurma.resizable(False, False)
    cadastrarAlunoTurma.title("Sistema Escola Shantala")
    cadastrarAlunoTurma.geometry('600x300')
    tk.Label(cadastrarAlunoTurma, text="Cadastrar Turma do Aluno: ").grid(row=2, column=0)
    tk.Label(cadastrarAlunoTurma, text="ID Turma ").grid(row=3, column=0)
    tk.Label(cadastrarAlunoTurma, text="Nome Aluno").grid(row=4, column=0)

    idTurma = tk.Entry(cadastrarAlunoTurma)
    idTurma.grid(row=3, column=1)

    comandopesqcursos = """SELECT nomealuno FROM alunos"""
    alunos = pesquisar(comandopesqcursos)

    alunos = tuple(a[0].strip("''") for a in alunos)
    naluno = tk.StringVar()
    escolheAlunoTurma = ttk.Combobox(cadastrarAlunoTurma, width=27, textvariable=naluno)
    escolheAlunoTurma['values'] = alunos
    escolheAlunoTurma.grid(column=1, row=4)
    escolheAlunoTurma.current()

    

    def cadastraralunoturma():              
        conectarBanco()
        cursor = conexao.cursor()
        idturma = idTurma.get()
        nomealuno = escolheAlunoTurma.get()
        nomea = (nomealuno,)
         # Pesquisando IDs
        comandopesquisaidaluno = """SELECT idaluno FROM alunos WHERE nomealuno LIKE %s"""
        resultAluno = pesquisarid(comandopesquisaidaluno, nomea)
        if len(resultAluno) == 0:
            alertamsg="Aluno não encontrado"
            msg(alertamsg)
            return 
        idaluno = resultAluno[0]

        comando = """INSERT INTO "alunoturmas" ("idturma", "idaluno") VALUES (%s, %s)"""
        dados = (idturma, idaluno)
        cursor.execute(comando, dados)
        conexao.commit()
        count = cursor.rowcount
        if count > 0:
            alerta = "Cadastro Realizado com Sucesso!"
            msg(alerta)
            cadastrarAlunoTurma.destroy()

        cursor.close()
        conexao.close()    

    tk.Button(cadastrarAlunoTurma, text='Cadastrar', command=cadastraralunoturma).grid(row=6, column=0, sticky=tk.W, pady=4)
    tk.Button(cadastrarAlunoTurma, text='Sair', command=cadastrarAlunoTurma.destroy).grid(row=6, column=1, sticky=tk.W, pady=4)

    cadastrarAlunoTurma.mainloop()

# Menu Principal
principal = tk.Tk()
principal.resizable(False, False)
principal.title("Sistema Escola Shantala")
principal.geometry('800x600+10+10')
tk.Button(principal, text='Alunos', command=cadastrarAluno).grid(row=1, column=0, sticky=tk.W, pady=4)
tk.Button(principal, text='Cursos', command=cadstrarCurso).grid(row=1, column=1, sticky=tk.W, pady=4)
tk.Button(principal, text='Turmas', command=cadastrarTurma).grid(row=1, column=2, sticky=tk.W, pady=4)
tk.Button(principal, text='Professores', command=professores).grid(row=1, column=3, sticky=tk.W, pady=4)
tk.Button(principal, text='Alunos na turma', command=cadastrarAlunoTurma).grid(row=1, column=4, sticky=tk.W, pady=4)
tk.Button(principal, text='Sair', command=principal.quit).grid(row=1, column=5, sticky=tk.W, pady=4)

principal.mainloop()
