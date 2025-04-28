Feature: Busqueda en mercado libre
    Scenario: Buscar 1 articulo en mercado libre
        Given el usuario se encuenta en la pagina principal de mercado libre
        When el usuario escribe articulo a buscar
        Then aparece el articulo buscado