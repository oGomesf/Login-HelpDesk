import customtkinter as ctk
from tkinter import PhotoImage


class app(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.Config_janela_inicial()
        self.tela_login()

    # -- CONFIGURAÇAO JANELA PRINCIPAL -- 
    def Config_janela_inicial(self):
        ctk.set_appearance_mode("Dark")
        self.title("Sitema de login")
        self.geometry("700x400")
        self.resizable(False, False)

    # -- COSTUMIZAÇÃO TELA LOGIN --
    def tela_login(self):
        self.img = PhotoImage(file="Server-rafiki.png")
        self.label_img = ctk.CTkLabel(self, text=None, image= self.img)
        self.label_img.grid(row=1, column=0, padx=10)

        self.title = ctk.CTkLabel(self, text="Faça o login ou cadastre-se\npara acessar o Help Desk!",font= ("Century Gothic", 15, "bold"))
        self.title.grid(row=0, column=0, pady= 10, padx=10)

    #-- Formulário login -- 
        self.frame_login = ctk.CTkFrame(self, width=350, height=380)
        self.frame_login.place(x=350, y=10)

    # -- Widgets Formulario login -- 
        self.label_title = ctk.CTkLabel(self.frame_login, text="Faça seu Login",font= ("Century Gothic", 20, "bold"))
        self.label_title.grid(row=0, column= 0, padx= 10, pady=10)

        self.user_login_entry = ctk.CTkEntry(self.frame_login,width=300, placeholder_text="Digite seu usuário", font=("Century Gothic", 14, "bold"), corner_radius=15)
        self.user_login_entry.grid(row=1, column=0, padx=10, pady=10)
        
        self.user_pass_entry = ctk.CTkEntry(self.frame_login,width=300, placeholder_text="Digite sua senha", font=("Century Gothic", 14, "bold"), corner_radius=15)
        self.user_pass_entry.grid(row=2, column=0, padx=10, pady=10)
        
        self.show_pass = ctk.CTkCheckBox(self.frame_login,text="Clique para ver a senha", font=("Century Gothic", 12, "bold"))
        self.show_pass.grid(row=3, column=0, padx=10, pady=10)

        self.btn_login = ctk.CTkButton(self.frame_login, width=200, text="Login",font=("Century Gothic", 14, "bold"), fg_color="green",corner_radius=10)
        self.btn_login.grid(row=4, column=0, padx=10, pady=10)
        
        self.spam = ctk.CTkLabel(self.frame_login, text="Não possue conta?, se cadastre abaixo!",font=("Century Gothic", 12, "bold"))
        self.spam.grid(row=5, column=0, padx=10, pady=10)

        self.btn_cadastro = ctk.CTkButton(self.frame_login, width=200, text="Cadastre-se",font=("Century Gothic", 14, "bold"), fg_color="Dark Blue",corner_radius=10)
        self.btn_cadastro.grid(row=6, column=0, padx=10, pady=10)          

if __name__ == "__main__":
    app = app()
    app.mainloop()