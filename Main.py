# -*- coding: utf-8 -*-  

import subprocess
import shlex, subprocess

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

####################################################################################################################################################
# This is already! :D

        if command == 'D':
            dim1 = int(input('¿Cuál es la dimensión de la retícula?: '))
            
            if dim1 == 1 :
                command_line = 'python3.7 -m manim Laticed.py SpanLattice1D -pl'
                args = shlex.split(command_line)
                subprocess.call(args)

            if dim1 == 2 :
                
                do1 = str(input('''
                    ¿Qué deseas hacer? 
                    [a] Animar la retícula por el conjunto generador.
                    [b] Dibujar la retícula directamente. 
                    [c] Diujar la reítcula y su Dominio Fundamental.
                    [d] Reducir la retícula por algoritmo de Gauss.
                    '''))
                if do1 == 'a':
                    command_line = 'python3.7 -m manim Laticed.py SpanLattice2D -pl'
                    args = shlex.split(command_line)
                    subprocess.call(args)
                
                if do1 == 'b':
                    command_line = 'python3.7 -m manim Laticed.py  DrawLattice2D -pl'
                    args = shlex.split(command_line)
                    subprocess.call(args)
                
                if do1 == 'c':
                    command_line = 'python3.7 -m manim Laticed.py  DrawDomFundLattice2D -pl'
                    args = shlex.split(command_line)
                    subprocess.call(args)
                  
                if do1 == 'd':
                    command_line = 'python3.7 -m manim Laticed.py  GaussLatticeReduction -pl'
                    args = shlex.split(command_line)
                    subprocess.call(args)        
                else:
                    print("¡Selecione una opción!")

            if dim1 >= 3:
                print('¡La dimensión de la retícula no debe ser mayor a la del espacio!')

########################################################################################################################
        
        if command == 'T':
            dim2 = int(input('¿Cuál es la dimensión de la retícula?: '))

            if dim2 == 1 :
                command_line = 'python3.7 -m manim Laticed.py DrawLattice1Din3D -pl'
                args = shlex.split(command_line)
                subprocess.call(args)

            if dim2 == 2 :

                do2 = str(input('''
                    ¿Qué deseas hacer? 
                    [a] Dibujar la retícula directamente. 
                    [b] Diujar la reítcula y su Dominio Fundamental.
                    '''))
                if do2 == 'a':
                    command_line = 'python3.7 -m manim Laticed.py DrawLattice2Din3D -pl'
                    args = shlex.split(command_line)
                    subprocess.call(args)

                if do2 == 'b':
                    command_line = 'python3.7 -m manim Laticed.py DrawLatticeDomFund2Din3D -pl'
                    args = shlex.split(command_line)
                    subprocess.call(args)

                else:
                    break

            if dim2 == 3:
                do3 = str(input('''
                    ¿Qué deseas hacer? 
                    [a] Dibujar la retícula directamente. 
                    [b] Diujar la reítcula y su Dominio Fundamental.
                    [c] Reducir la retícula por algoritmo LLL.
                    '''))
                # This is already! :D
                if do3 == 'a':
                    command_line = 'python3.7 -m manim Laticed.py DrawLattice3D -pl'
                    args = shlex.split(command_line)
                    subprocess.call(args)

                if do3 == 'b':
                    command_line = 'python3.7 -m manim Laticed.py DrawDomFund3D -pl'
                    args = shlex.split(command_line)
                    subprocess.call(args)

                if do3 == 'c':
                    command_line = 'python3.7 -m manim Laticed.py LLLReduceLattice -pl'
                    args = shlex.split(command_line)
                    subprocess.call(args)

                else: 
                    break

            if dim2 >= 4:
                print('¡La dimensión de la retícula no debe ser mayor a la del espacio!')

#############################################################################################################################################

        if command == 'C':
            print("Se va a dibujar la represenación de una retícula de cuatro dimensiones.")
            command_line = 'python3.7 -m manim Laticed.py DrawLattice4D -pl'                 
            args = shlex.split(command_line)
            subprocess.call(args)



#############################################################################################################################################        
        if command == 's':
            break

        else:
            print("¡Seleccione una de las opciones!")

if __name__ == '__main__':
    run()

