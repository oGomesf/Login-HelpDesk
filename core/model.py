import sqlite3

class BackEnd():
    def ConectarDB(self):
        self.conn = sqlite3.connect("sistema-cadastro.db")
        self.cursor = self.conn.cursor()
        print("Banco de Dados Conectado")

    def DesconectDB(self):
        self.conn.close()
        print("Banco de Dados Desconectado")

    def Criar_tabela(self):
        self.ConectarDB()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Usuarios(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Username TEXT UNIQUE NOT NULL,
                Email TEXT UNIQUE NOT NULL CHECK (
                        Email LIKE '%@%.com' AND
                        Email NOT LIKE '@%.com' AND
                        Email NOT LIKE '%@.com'
                     ),
                Senha TEXT NOT NULL,
                Confirma_senha TEXT NOT NULL
            );
        """)
        self.conn.commit()
        print("Tabela criada com sucesso!")
        self.DesconectDB()