import sqlite3
from tkinter import messagebox
from core.model import BackEnd

class AppController(BackEnd):
    def __init__(self):
        self.view = None 

    def set_view(self, view_instance):
        self.view = view_instance

    def Cadastrar_usuario(self):
        self.user_cadastro = self.view.user_cad_entry.get()
        self.email_cadastro = self.view.user_cad_email_entry.get()
        self.pass_cadastro = self.view.user_cad_pass_entry.get()
        self.confirm_pass_cadastro = self.view.confirm_cad_pass_entry.get()

        if self.user_cadastro == "" or self.email_cadastro == "" or self.pass_cadastro == "" or self.confirm_pass_cadastro == "":
            messagebox.showerror(title="Sistema de Login", message="Por favor, preencha todos os campos!")
            return
        
        if self.pass_cadastro != self.confirm_pass_cadastro:
            messagebox.showerror(title="Sistema de Login", message="As senhas não coincidem!")
            return

        self.ConectarDB()
        try:
            self.cursor.execute("""
                INSERT INTO Usuarios (Username, Email, Senha, Confirma_senha)
                VALUES (?,?,?,?)""", (self.user_cadastro, self.email_cadastro, self.pass_cadastro, self.confirm_pass_cadastro))
            self.conn.commit()
            messagebox.showinfo(title="Sistema de login", message="Dados cadastrados com sucesso")
            self.view.Clear_entry_cad()
            self.view.tela_login()
            
        except sqlite3.IntegrityError as u:
            erro_msg = str(u)
            if "Usuarios.Username" in erro_msg:
                messagebox.showerror(title="Usuário inválido", message="O usuário já foi cadastrado!")
            elif "Usuarios.Email" in erro_msg:
                messagebox.showerror(title="Email inválido", message="Email já cadastrado!")
            elif "CHECK constraint failed" in erro_msg:
                messagebox.showerror(title="Email inválido", message="O e-mail deve ser no formato: exemplo@email.com")
        finally:
            self.DesconectDB()

    def Verificar_login(self):
        self.user_login = self.view.user_login_entry.get()
        self.user_pass = self.view.user_pass_entry.get()
        self.ConectarDB()
        try:
            self.cursor.execute("""SELECT * FROM Usuarios WHERE Username = ? AND Senha = ?""", 
                                (self.user_login, self.user_pass))
            self.verifica_dados = self.cursor.fetchone()
            if self.verifica_dados:
                messagebox.showinfo(title="Sistema de login", message="Logado com sucesso!")
                self.view.Clear_entry_login()
            else:
                messagebox.showerror(title="Sistema de login", message="Login ou senha inválidos")
        except Exception as e:
            messagebox.showerror(title="Erro de Sistema", message=f"Erro ao consultar banco: {e}")
        finally:
            self.DesconectDB()