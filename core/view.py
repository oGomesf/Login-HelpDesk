import customtkinter as ctk
from tkinter import *

class AppView(ctk.CTk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.Config_janela_inicial()
        self.tela_login()

    def Config_janela_inicial(self):
        ctk.set_appearance_mode("Dark")
        self.title("Sistema de login")
        self.geometry("700x400")
        self.resizable(False, False)

    def toggle_senha_login(self):
        if self.show_pass_login.get() == 1:
            self.user_pass_entry.configure(show="")
        else:
            self.user_pass_entry.configure(show="*")

    def toggle_senha_cad(self):
        if self.show_pass_cad.get() == 1:
            self.user_cad_pass_entry.configure(show="")
            self.confirm_cad_pass_entry.configure(show="")
        else:
            self.user_cad_pass_entry.configure(show="*")
            self.confirm_cad_pass_entry.configure(show="*")

    def tela_login(self):
        if hasattr(self, 'frame_cadastro'):
            self.frame_cadastro.place_forget()

        try:
            self.img = PhotoImage(file="Server-rafiki.png")
            self.label_img = ctk.CTkLabel(self, text=None, image= self.img)
            self.label_img.grid(row=1, column=0, padx=10)
        except:
            print("Imagem não encontrada")

        self.titulo_label = ctk.CTkLabel(self, text="Faça o login ou cadastre-se\npara acessar o Help Desk!", font= ("Century Gothic", 15, "bold"))
        self.titulo_label.grid(row=0, column=0, pady= 10, padx=10)

        self.frame_login = ctk.CTkFrame(self, width=350, height=380)
        self.frame_login.place(x=350, y=10)

        self.label_title = ctk.CTkLabel(self.frame_login, text="Faça seu Login", font= ("Century Gothic", 20, "bold"))
        self.label_title.grid(row=0, column= 0, padx= 10, pady=10)

        self.user_login_entry = ctk.CTkEntry(self.frame_login, width=300, placeholder_text="Digite seu usuário", font=("Century Gothic", 14, "bold"), corner_radius=15)
        self.user_login_entry.grid(row=1, column=0, padx=10, pady=10)
        
        self.user_pass_entry = ctk.CTkEntry(self.frame_login, width=300, placeholder_text="Digite sua senha", font=("Century Gothic", 14, "bold"),
                                             corner_radius=15, show= "*")
        self.user_pass_entry.grid(row=2, column=0, padx=10, pady=10)
        
        self.show_pass_login = ctk.CTkCheckBox(self.frame_login, text="Clique para ver a senha", font=("Century Gothic", 12, "bold"), command=self.toggle_senha_login)
        self.show_pass_login.grid(row=3, column=0, padx=10, pady=10)

        self.btn_login = ctk.CTkButton(self.frame_login, width=200, text="Login", font=("Century Gothic", 14, "bold"),
                                        fg_color="green", corner_radius=10, command=self.controller.Verificar_login)
        self.btn_login.grid(row=4, column=0, padx=10, pady=10)
        
        self.spam = ctk.CTkLabel(self.frame_login, text="Não possui conta?, se cadastre abaixo!", font=("Century Gothic", 12, "bold"))
        self.spam.grid(row=5, column=0, padx=10, pady=10)

        self.btn_cadastro = ctk.CTkButton(self.frame_login, width=200, text="Cadastre-se", font=("Century Gothic", 14, "bold"), fg_color="Dark Blue",
                                          corner_radius=10, command=self.tela_cadastro)
        self.btn_cadastro.grid(row=6, column=0, padx=10, pady=10)          

    def tela_cadastro(self):
        self.frame_login.place_forget()
        self.frame_cadastro = ctk.CTkFrame(self, width=350, height=380)
        self.frame_cadastro.place(x=350, y=10)
        
        self.label_title_cad = ctk.CTkLabel(self.frame_cadastro, text="Faça seu cadastro", font= ("Century Gothic", 20, "bold"))
        self.label_title_cad.grid(row=0, column= 0, padx= 10, pady=5)

        self.user_cad_entry = ctk.CTkEntry(self.frame_cadastro, width=300, placeholder_text="Digite seu usuário", font=("Century Gothic", 14, "bold"), corner_radius=15)
        self.user_cad_entry.grid(row=1, column=0, padx=10, pady=5)

        self.user_cad_email_entry = ctk.CTkEntry(self.frame_cadastro, width=300, placeholder_text="Digite seu e-mail", font=("Century Gothic", 14, "bold"), corner_radius=15)
        self.user_cad_email_entry.grid(row=2, column=0, padx=10, pady=5)
        
        self.user_cad_pass_entry = ctk.CTkEntry(self.frame_cadastro, width=300, placeholder_text="Digite sua senha", font=("Century Gothic", 14, "bold"),
                                             corner_radius=15, show= "*")
        self.user_cad_pass_entry.grid(row=3, column=0, padx=10, pady=5)

        self.confirm_cad_pass_entry = ctk.CTkEntry(self.frame_cadastro, width=300, placeholder_text="Confirme sua senha", font=("Century Gothic", 14, "bold"),
                                             corner_radius=15, show= "*")
        self.confirm_cad_pass_entry.grid(row=4, column=0, padx=10, pady=5)

        self.show_pass_cad = ctk.CTkCheckBox(self.frame_cadastro, text="Clique para ver a senha", font=("Century Gothic", 12, "bold"), command=self.toggle_senha_cad)
        self.show_pass_cad.grid(row=5, column=0, padx=10, pady=5)

        self.btn_cadastrar_user = ctk.CTkButton(self.frame_cadastro, width=200, text="Cadastrar", font=("Century Gothic", 14, "bold"), fg_color="Dark Green",
                                          corner_radius=10, command=self.controller.Cadastrar_usuario)
        self.btn_cadastrar_user.grid(row=6, column=0, padx=10, pady=5)

        self.btn_login_back = ctk.CTkButton(self.frame_cadastro, width=200, text="Voltar ao Login", font=("Century Gothic", 14, "bold"), fg_color="Dark Blue",
                                            corner_radius=10, command=self.tela_login)
        self.btn_login_back.grid(row=7, column=0, padx=10, pady=5)
    
    def Clear_entry_cad(self):
        self.user_cad_entry.delete(0, END)
        self.user_cad_pass_entry.delete(0, END)
        self.user_cad_email_entry.delete(0, END)
        self.confirm_cad_pass_entry.delete(0, END)

    def Clear_entry_login(self):
        self.user_login_entry.delete(0, END)
        self.user_pass_entry.delete(0, END)