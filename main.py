from core.controller import AppController
from core.view import AppView

if __name__ == "__main__":
    # 1. Instancia o controller
    controller = AppController()
    
    # 2. Cria o banco/tabela
    controller.Criar_tabela()
    
    # 3. Cria a interface passando o controller
    app_instance = AppView(controller)
    
    # 4. Conecta a interface de volta no controller
    controller.set_view(app_instance)
    
    # 5. Inicia o loop
    app_instance.mainloop()