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

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Chamados(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                descricao TEXT,
                status TEXT DEFAULT 'Aberto',
                data_abertura DATETIME DEFAULT CURRENT_TIMESTAMP
            );
        """)

        self.conn.commit()
        print("Tabela criada com sucesso!")
        self.DesconectDB()

        # --- MÉTODOS DO CRUD DE CHAMADOS ---

    def salvar_chamado_db(self, titulo, descricao):
        """Insere um novo chamado no banco"""
        self.ConectarDB()
        try:
            self.cursor.execute("""
                INSERT INTO Chamados (titulo, descricao)
                VALUES (?, ?)""", (titulo, descricao))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Erro ao salvar: {e}")
            return False
        finally:
            self.DesconectDB()

    def buscar_chamados_db(self):
        """Retorna todos os chamados para listar na Treeview"""
        self.ConectarDB()
        self.cursor.execute("SELECT id, titulo, status, data_abertura FROM Chamados ORDER BY id DESC")
        dados = self.cursor.fetchall()
        self.DesconectDB()
        return dados

    def deletar_chamado_db(self, id_chamado):
        """Remove um chamado pelo ID"""
        self.ConectarDB()
        try:
            self.cursor.execute("DELETE FROM Chamados WHERE id = ?", (id_chamado,))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Erro ao deletar: {e}")
            return False
        finally:
            self.DesconectDB()

    def atualizar_chamado_db(self, id_chamado, novo_status):
        """Atualiza o status de um chamado (ex: de Aberto para Concluído)"""
        self.ConectarDB()
        try:
            self.cursor.execute("UPDATE Chamados SET status = ? WHERE id = ?", (novo_status, id_chamado))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Erro ao atualizar: {e}")
            return False
        finally:
            self.DesconectDB()