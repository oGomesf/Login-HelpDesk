🛠️ Sistema de Chamados com Autenticação
Um sistema desktop moderno para gerenciamento de chamados (CRUD), com controle de acesso, desenvolvido em Python e CustomTkinter.

📖 Sobre o Projeto
Este sistema combina uma interface moderna e responsiva para o gerenciamento de tickets de suporte com uma camada de segurança inicial. O projeto utiliza o CustomTkinter para garantir uma estética atual (com suporte nativo a temas Dark e Light) e o SQLite3 para persistência de dados local de forma leve e eficiente.

✨ Funcionalidades
🔐 Sistema de Autenticação (Finalizado)
[x] Login de Usuários: Validação de credenciais no banco de dados.

[x] Cadastro de Usuários: Registro de novos operadores do sistema.

[x] Segurança: Persistência de dados de usuários via SQLite.

🎫 Gestão de Chamados (Em progresso)
[ ] Criação (Create): Abertura de novos chamados com título, descrição e prioridade.

[ ] Visualização (Read): Listagem e consulta de chamados existentes.

[ ] Edição (Update): Atualização de status e informações dos tickets.

[ ] Exclusão (Delete): Remoção de chamados do banco de dados.

🚀 Tecnologias Utilizadas
Linguagem: Python

GUI: CustomTkinter & Tkinter

Banco de Dados: SQLite3

🔧 Como Executar
Pré-requisitos
Python 3.8 ou superior.

Instalação
Bash
# Instale a biblioteca de interface moderna
pip install customtkinter
Execução
Bash
# Execute o arquivo de entrada (app.py)
python main.py
📁 Estrutura do Projeto (FINAL - estado atual, em progresso. irei organizar melhor conforme for integrando os sistemas)
Plaintext
├── database/
│   └── sistema.db        # Armazena tabelas de usuários e chamados
├── src/
│   ├── auth.py           # Lógica de login e cadastro
│   ├── crud.py           # Funções de manipulação dos chamados
│   └── interface.py      # Telas desenvolvidas em CustomTkinter
└── main.py               # Ponto de entrada da aplicação
🚧 Próximos Passos
[ ] Implementar níveis de permissão (Usuário vs. Administrador).

[ ] Adicionar funcionalidade de "esqueci minha senha".

[ ] Melhorar a visualização dos chamados com filtros de busca.

✨ Desenvolvimento por [Alexandre Gomes]
