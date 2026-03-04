from core.controller import AppController
from core.view import AppView

if __name__ == "__main__":
    #-- Instancia o controller --
    controller = AppController()
    
    #--Cria o banco/tabela --
    controller.Criar_tabela()
    
    #-- Cria a interface passando o controller -- 
    app_instance = AppView(controller)
    
    #-- Conecta a interface de volta no controller --
    controller.set_view(app_instance)
    
    #-- Inicia o app --
    app_instance.mainloop()