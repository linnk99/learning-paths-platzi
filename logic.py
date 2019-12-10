

def command(option):
    

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
                           [M]arketing
                           [N]egocios y Emprendimiento
                           [P]roducción Audiovisual
                           [C]recimiento profesional
                           
                           ''').lower())
        
        command(option)

if __name__ == "__main__":
    run()