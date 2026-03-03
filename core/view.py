import customtkinter as ctk
from tkinter import *
from tkinter import ttk

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

    def tela_dashboard(self):
        # 1. Limpeza TOTAL para evitar erro de conflito "grid/pack"
        for widget in self.winfo_children():
            widget.grid_forget()
            widget.pack_forget()
            widget.place_forget()

        # 2. Configurações da Janela
        self.geometry("1000x600")
        self.title("Sistema Help Desk - Dashboard")

        # 3. Sidebar (Barra Lateral)
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.pack(side="left", fill="y")

        self.logo_label = ctk.CTkLabel(self.sidebar, text="HELP DESK", font=("Century Gothic", 22, "bold"))
        self.logo_label.pack(pady=30, padx=20)

        # Botão para abrir o formulário de novo chamado
        self.btn_novo_chamado = ctk.CTkButton(self.sidebar, text="Novo Chamado", 
                                               command=self.abrir_formulario_chamado,
                                               fg_color="green", hover_color="#006400")
        self.btn_novo_chamado.pack(pady=10, padx=20)

        # Botão de Sair (volta para o login)
        self.btn_sair = ctk.CTkButton(self.sidebar, text="Sair / Logout", fg_color="#910000", 
                                       command=self.tela_login)
        self.btn_sair.pack(side="bottom", pady=20, padx=20)

        # 4. Painel Principal (Lado Direito)
        self.main_frame = ctk.CTkFrame(self, corner_radius=10)
        self.main_frame.pack(side="right", fill="both", expand=True, padx=20, pady=20)

        self.dash_title = ctk.CTkLabel(self.main_frame, text="Gerenciamento de Chamados", font=("Century Gothic", 24, "bold"))
        self.dash_title.pack(pady=(20, 10))

        # 5. Estilização da Treeview (Tabela)
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview", 
                        background="#2b2b2b", 
                        foreground="white", 
                        rowheight=25, 
                        fieldbackground="#2b2b2b", 
                        borderwidth=0)
        style.configure("Treeview.Heading", background="#333333", foreground="white", relief="flat")
        style.map("Treeview", background=[('selected', '#1f538d')])

        # Container para a tabela
        self.tree_frame = Frame(self.main_frame, bg="#2b2b2b")
        self.tree_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Criação da Tabela
        self.tree = ttk.Treeview(self.tree_frame, columns=("ID", "Título", "Status", "Data"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Título", text="Título")
        self.tree.heading("Status", text="Status")
        self.tree.heading("Data", text="Data de Abertura")
        
        self.tree.column("ID", width=50, anchor="center")
        self.tree.column("Título", width=350)
        self.tree.column("Status", width=120, anchor="center")
        self.tree.column("Data", width=150, anchor="center")
        
        self.tree.pack(fill="both", expand=True)

        # 6. Botões de Ação (CRUD) abaixo da tabela
        self.action_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.action_frame.pack(fill="x", padx=20, pady=20)

        self.btn_refresh = ctk.CTkButton(self.action_frame, text="Atualizar Lista", 
                                          command=self.controller.carregar_tabela_chamados)
        self.btn_refresh.pack(side="left", padx=5)

        self.btn_delete = ctk.CTkButton(self.action_frame, text="Excluir Selecionado", 
                                         fg_color="#910000", hover_color="#6b0000",
                                         command=self.controller.excluir_chamado_logica)
        self.btn_delete.pack(side="right", padx=5)

        # 7. Carregar dados iniciais
        self.controller.carregar_tabela_chamados()

    def abrir_formulario_chamado(self):
        """Cria uma janela pop-up (Toplevel) para cadastrar novo chamado"""
        self.janela_pop = ctk.CTkToplevel(self)
        self.janela_pop.title("Novo Chamado")
        self.janela_pop.geometry("400x400")
        self.janela_pop.attributes("-topmost", True) # Mantém a janela na frente

        ctk.CTkLabel(self.janela_pop, text="Abrir Novo Chamado", font=("Arial", 18, "bold")).pack(pady=20)

        entry_titulo = ctk.CTkEntry(self.janela_pop, placeholder_text="Título do Problema", width=300)
        entry_titulo.pack(pady=10)

        entry_desc = ctk.CTkTextbox(self.janela_pop, width=300, height=150)
        entry_desc.pack(pady=10)
        entry_desc.insert("0.0", "Descrição do problema...")

        btn_salvar = ctk.CTkButton(self.janela_pop, text="Salvar Chamado", 
                                   command=lambda: self.controller.novo_chamado_logica(
                                       entry_titulo.get(), 
                                       entry_desc.get("0.0", "end-1c"), 
                                       self.janela_pop
                                   ))
        btn_salvar.pack(pady=20)
        
        
