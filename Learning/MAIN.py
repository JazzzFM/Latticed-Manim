# -*- coding: utf-8 -*-  
import subprocess

def run():
    while True:
        command = str(input('''
██▓    ▄▄▄     ▄▄▄█████▓▄▄▄█████▓ ██▓ ▄████▄  ▓█████ ▓█████▄ 
▓██▒   ▒████▄   ▓  ██▒ ▓▒▓  ██▒ ▓▒▓██▒▒██▀ ▀█  ▓█   ▀ ▒██▀ ██▌
▒██░   ▒██  ▀█▄ ▒ ▓██░ ▒░▒ ▓██░ ▒░▒██▒▒▓█    ▄ ▒███   ░██   █▌
▒██░   ░██▄▄▄▄██░ ▓██▓ ░ ░ ▓██▓ ░ ░██░▒▓▓▄ ▄██▒▒▓█  ▄ ░▓█▄   ▌
░██████▒▓█   ▓██▒ ▒██▒ ░   ▒██▒ ░ ░██░▒ ▓███▀ ░░▒████▒░▒████▓ 
░ ▒░▓  ░▒▒   ▓▒█░ ▒ ░░     ▒ ░░   ░▓  ░ ░▒ ▒  ░░░ ▒░ ░ ▒▒▓  ▒ 
░ ░ ▒  ░ ▒   ▒▒ ░   ░        ░     ▒ ░  ░  ▒    ░ ░  ░ ░ ▒  ▒ 
   ░ ░    ░   ▒    ░        ░       ▒ ░░           ░    ░ ░  ░ 
    ░  ░     ░  ░                  ░  ░ ░         ░  ░   ░    
    ░                ░      

Herramienta para hacer visualizaciones y animaciones con retículas en 2D, 3D y 4D. 
                             CIC - IPN - ESFM
                                                    - Made with manim, python and LaTex.

¿Cuál es la dimensión del Espacio donde vas a trabajar?
[D] Dimensión Dos |R^2
[T] Dimensión Tres |R^3
[C] Dimensión Cuatro |R^4
[s] salir
            '''))
        if command == 'D':
            print('¿Cuál es la dimensión de la retícula?')
            break
        elif command == 'T':
            print('¿Cuál es la dimensión de la retícula?')
            break
        else:
            break

if __name__ == '__main__':
    run()

