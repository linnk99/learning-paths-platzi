class LearningPath():
    
    def __init__(self, categoria, especialidad, nivel):
        self.categoria = categoria
        self.especialidad = especialidad
        self.nivel = nivel

class ListaRutas():
    
    def __init__():
        self.rutas = []
    

def command(option):
    if option == 'd':
        
        print('Elegiste Desarrollo e Ingenieria')

    elif option == 'di':
        
        print('Elegiste Diseño y UX')
        
    elif option == 'm':
        
        print('Elegiste Marketing Digital')
        
    elif option == 'n':
        
        print('Elegiste Negocios y Emprendimiento')
        
    elif option == 'p':
        
        print('Elegiste Producción Audiovisual')

    elif option == 'c':
        
        print('Elegiste Crecimiento Profesional')
        
    else:
        print('Opción no válida, intenta de nuevo por favor.')
        

def run():
    print('''                    
     _                           _               _____      _   _         
    | |                         (_)             |  __ \    | | | |        
    | |     ___  __ _ _ __ _ __  _ _ __   __ _  | |__) |_ _| |_| |__  ___ 
    | |    / _ \/ _` | '__| '_ \| | '_ \ / _` | |  ___/ _` | __| '_ \/ __|
    | |___|  __/ (_| | |  | | | | | | | | (_| | | |  | (_| | |_| | | \__ \.
    |______\___|\__,_|_|  |_| |_|_|_| |_|\__, | |_|   \__,_|\__|_| |_|___/
                                        __/ |                           
                                        |___/                                                                                                                                                   
            ''')    
    
    while True:
        option = str(input('''Elige una opción: 
                           
                           [D]esarollo e Ingeniería
                           [Di]seño y UX
                           [M]arketing Digital
                           [N]egocios y Emprendimiento
                           [P]roducción Audiovisual
                           [C]recimiento profesional
                           
                           ''').lower())
        
        command(option)

if __name__ == "__main__":
    run()