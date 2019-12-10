areas_de_conocimiento = (
    'Desarrollo e Ingenieria',
    'Diseño y UX',
    'Marketing Digital',
    'Negocios y Emprendimiento',
    'Producción Audiovisual',
    'Crecimiento Profesional',    
)

rutas_desarrollo = (
    'Fundamentos de Programación',
    'Desarrollo Web Frontend',
    'Desarrollo Web Backend',
    'Bases de Datos',
    'Desarrollo Móvil',
    'Big Data y Data Science',
    'Inteligencia Artificial',
    'Internet of Things',
    'Seguridad Informática',
    'Cloud Technologies',
    'Desarrollo de Videojuegos'
)

rutas_diseno = (
    
)

rutas_marketing = (
    
)

class LearningPath():
    
    def __init__(self, categoria, especialidad, nivel, nombre):
        self.categoria = categoria
        self.especialidad = especialidad
        self.nivel = nivel
        self.nombre = nombre

class ListaRutas():
    
    def __init__():
        self.rutas = []

    def area_de_conocimiento(option):
        if option == 'd':
            rutas[0] = 'Desarrollo e Ingenieria'
            print('Elegiste Desarrollo e Ingenieria')

        elif option == 'di':
            rutas[0] = 'Diseño y UX'
            print('Elegiste Diseño y UX')
            
        elif option == 'm':
            rutas[0] = 'Marketing Digital'
            print('Elegiste Marketing Digital')
            
        elif option == 'n':
            rutas[0] = 'Negocios y Emprendimiento'
            print('Elegiste Negocios y Emprendimiento')
            
        elif option == 'p':
            rutas[0] = 'Producción Audiovisual'
            print('Elegiste Producción Audiovisual')

        elif option == 'c':
            rutas[0] = 'Crecimiento Profesional'
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
        option = str(input('''Elige un área de conocimiento: 
                           
                           [D]esarollo e Ingeniería
                           [Di]seño y UX
                           [M]arketing Digital
                           [N]egocios y Emprendimiento
                           [P]roducción Audiovisual
                           [C]recimiento profesional
                           
                           ''').lower())
        
        ListaRutas.area_de_conocimiento(option)

if __name__ == "__main__":
    run()