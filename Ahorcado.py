import random

def CrearMatriz():
    """ Función para crear la matriz visual """

    col=50
    fil=30
    matrix=[["█"]*col for i in range(fil)] # ▓ ▀ █
    fi=29
    for f in range(28):  # TALLO
        matrix[fi].insert(45," ")
        fi-=1
    co=23
    for f in range(23):  # RAMA
        matrix[1][co]="▀"
        co+=1

    matrix[2][23]=" "   #TALLO corto

    return matrix

def imprimirHombre(error):
    """ Función para armar el hombre según los errores del jugador """

    if error == 1:     # Imprime cabeza
        matriz[3][21],matriz[3][22],matriz[3][23],matriz[3][24],matriz[3][25]="▀"," "," "," ","▀"
        matriz[4][19],matriz[4][20],matriz[4][21],matriz[4][22],matriz[4][23],matriz[4][24],matriz[4][25],matriz[4][26],matriz[4][27]="▀"," "," "," "," "," "," "," ","▀"
        matriz[5][19],matriz[5][20],matriz[5][21],matriz[5][22],matriz[5][23],matriz[5][24],matriz[5][25],matriz[5][26],matriz[5][27]=" "," ","O"," "," "," ","O"," "," "
        matriz[6][19],matriz[6][20],matriz[6][21],matriz[6][22],matriz[6][23],matriz[6][24],matriz[6][25],matriz[6][26],matriz[6][27]="▄"," "," "," ","┴"," "," "," ","▄"
        matriz[7][20],matriz[7][21],matriz[7][22],matriz[7][23],matriz[7][24],matriz[7][25],matriz[7][26]="▄"," ","-","-","-"," ","▄"
        matriz[8][21],matriz[8][22],matriz[8][23],matriz[8][24],matriz[8][25]="▄"," "," "," ","▄"

    elif error == 2:    # Imprime cuerpo
        a=16
        r=0
        for i in range(4):
            for j in range(15-r):
                matriz[9+i][j+a]=" "
            a+=1
            r+=2

        for i in range(2):
            for j in range(9):
                matriz[i+13][j+19]=" "

    elif error == 3:    # Imprime brazo derecho
        for i in range(7):
            for j in range(2):
                matriz[i+9][j+14]=" "

    elif error == 4:    # Imprime brazo izquierdo
        for i in range(7):
            for j in range(2):
                matriz[i+9][j+31]=" "

    elif error == 5:    # Imprime pierna derecha
        for i in range(8):
            for j in range(3):
                matriz[i+15][j+19]=" "

        for i in range(4):
            for j in range(1):
                matriz[i+15][j+22]=" "

        for i in range(1):
            for j in range(4):
                matriz[i+22][j+15]=" "

        matriz[21][18]="▀"


    elif error == 6:    # Imprime pierna izquierda
        for i in range(8):
            for j in range(3):
                matriz[i+15][j+25]=" "

        for i in range(4):
            for j in range(1):
                matriz[i+15][j+24]=" "

        for i in range(1):
            for j in range(4):
                matriz[i+22][j+28]=" "

        matriz[21][28]="▀"

    elif error == 7:        # MUERTE!!
        matriz[5][21],matriz[5][25]="X","X",
        
    return matriz


def limpiarPalabra(cad):
    """Funcion para limpiar las tildes de las palabras del registro"""
    contilde="áéíóúÁÉÍÓÚ"
    sintilde="aeiouAEIOU"
    nueva=""
    for caracter in cad:
        if caracter in contilde:
            posicion= contilde.index(caracter)
            nueva=nueva+ sintilde[posicion]
        else:
            nueva=nueva +caracter
    return nueva

def imprimirListaRecursiva (lista,inicio=0):
    """Funcion para imprimir las listas de forma recurciva"""
    if inicio<len(lista):
        print(lista[inicio],end=" ")
        imprimirListaRecursiva(lista,inicio+1)

def verificarLetra(Usadas):
    """Funcion para verificar las letras que ingresa el usuario"""
    while True:
        try:
            l=input("adivine una letra: ")
            while l in Usadas:
                print("Esa letra ya la usaste, intenta con otra")
                l=input("adivine una letra: ")
            assert l.isalpha(), "Solo se permiten letras"
            assert 2>len(l), "Ingrese una sola letra"
            assert l.islower(), "Solo se permiten letras en minusculas"
            break    
        except AssertionError as mensaje:
            print()
            print(mensaje)
            print()
    return l
 
def verificarPalabra():
    """Funcion para verificar las palabras que ingresa el usuario """
    while True:
        try:
            pal=input("Ingrese la palabra a buscar: ")
            
            assert len(pal)>1, "Ingrese una palabra"
            assert pal.isalpha(),"Solo se permiten palabras"
            assert pal.islower(),"El bloq de mayúsculas esta activado "
            break
        except AssertionError as mensaje:
            print()
            print(mensaje)
            print()
    return pal        

def opcionNivel():
    """ Funcion para elegir el nivel del juego"""
    while True:
        try:
            print("1 = Fácil - 2 = Intermedio - 3 = Dificil")
            num=int(input("Elija un nivel de juego: "))

            assert 0< num< 4
            break
        except ValueError:
            print()
            print("Solo se permiten numeros")
            print()
        except AssertionError:
            print()
            print("elija un número entre 1 y 3")
            print()
    return num 

def jugarDeVuelta():
    """ Funcion para preguntar si desea siguir jugando"""
    while True:
        try:
            num=int(input("Desea seguir jugando? (1=Si / 2 = No): "))
            
            assert 0< num< 3
            break
        except ValueError:
            print()
            print("Solo se permiten numeros")
        except AssertionError:
            print()
            print("elija un número entre 1 y 2")
    return num 

def jugarAhorcado(dic,nom):#1
    """Funcion para jugar al ahorcado """
    
    try:
        
        entrada=open("Palabras.txt","rt",encoding="UTF8")
        respuesta=1

        while respuesta != 2:
            
            alazar= random.randint(1,80380)
            contador=0
            entrada.seek(0)
            linea=entrada.readline()
            
            while linea:
                linea=linea.replace("\n","")           
                if contador==alazar:
                    palabra=linea
                    palabra=palabra.rstrip(" ")
                    break
                    
                contador=contador+1
                linea=entrada.readline()
                                
            letrasUsadas=""
            palabraBuscada=[]
            palabraEscondida=["_"]
            errores=0                 
                       

            nivel=opcionNivel()
                
            if nivel==1: # Nivel facil
                
                palabraSinTilde=limpiarPalabra(palabra)
                for i in range (len(palabraSinTilde)):
                    palabraBuscada.append(palabraSinTilde[i])
                
                palabraEscondida=palabraEscondida*len(palabraSinTilde)
                print()
                while True:
                                        
                    imprimirHombre(errores)
                    f=25
                    c=50
                    for i in range(f): # Imprime matriz
                        for j in range(c):
                            print(matriz[i][j],end="")
                        print()
                     
                    #print(palabraSinTilde) # ver con que palabra se esta jugando
                    usadas=" ".join(letrasUsadas)
                    
                    print()
                    imprimirListaRecursiva(palabraEscondida)#imprimimos la lista de forma recursiva
                    print(f"Letras usadas:{usadas:>10}",end=" ") 
                    
                    print()
                    letra=verificarLetra(letrasUsadas)
                    
                    if letra in palabraSinTilde:
                        letrasUsadas=letrasUsadas+ letra
                        
                        for i in range(len(palabraSinTilde)):
                            if palabraSinTilde[i]==letra:
                                palabraEscondida[i]=letra
                                
                    else:
                        letrasUsadas=letrasUsadas+letra
                        errores=errores+1
                        print()
                        print("Letra incorrecta")
                        print()                        
                    
                    if palabraBuscada==palabraEscondida:
                        dic[nom][0]=dic[nom][0]+1
                        print()
                        print("Ganaste!!! la palabra es:", palabraSinTilde)
                        print()
                        break            

            elif nivel==2: # Nivel intermedio
                
                palabraSinTilde=limpiarPalabra(palabra)
                for i in range (len(palabraSinTilde)):
                    palabraBuscada.append(palabraSinTilde[i])
                
                palabraEscondida=palabraEscondida*len(palabraSinTilde)
                print()
                
                while errores!=7:
                                        
                    imprimirHombre(errores)
                    f=25
                    c=50
                    for i in range(f): # Imprime matriz
                        for j in range(c):
                            print(matriz[i][j],end="")
                        print()
                   
                    #print(palabraSinTilde) # ver con que palabra se esta jugando
                    usadas=" ".join(letrasUsadas)
                    
                    print()
                    imprimirListaRecursiva(palabraEscondida)#imprimimos la lista de forma recursiva
                    print(f"Letras usadas:{usadas:>10}",end=" ") 
                    
                    print()
                    letra=verificarLetra(letrasUsadas)
                    
                    if letra in palabraSinTilde:
                        letrasUsadas=letrasUsadas+ letra
                        
                        for i in range(len(palabraSinTilde)):
                            if palabraSinTilde[i]==letra:
                                palabraEscondida[i]=letra
                                
                    else:
                        letrasUsadas=letrasUsadas+letra
                        errores=errores+1
                        print()
                        print("Letra incorrecta")
                        print()
                        
                        if errores==7:
                            
                            mensaje=f"Perdiste, la palabra era {palabraSinTilde} cometiste los {errores} errores"
                            print(mensaje)
                            break

                    if palabraBuscada==palabraEscondida:
                        dic[nom][1]=dic[nom][1]+1
                        print()
                        print("Ganaste!!! la palabra es:", palabraSinTilde)
                        print()
                        break
            
            elif nivel==3: # Nivel Dificil
                
                for i in range (len(palabra)):
                    palabraBuscada.append(palabra[i])
                
                palabraEscondida=palabraEscondida*len(palabra)
                print()
                while errores!=7:
                                        
                    imprimirHombre(errores)
                    f=25
                    c=50
                    for i in range(f): # Imprime matriz
                        for j in range(c):
                            print(matriz[i][j],end="")
                        print()
                    
                    #print(palabra) # ver con que palabra se esta jugando
                    usadas=" ".join(letrasUsadas)
                    
                    print()
                    imprimirListaRecursiva(palabraEscondida)#imprimimos la lista de forma recursiva
                    print(f"Letras usadas:{usadas:>10}",end=" ") 
                    
                    print()
                    letra=verificarLetra(letrasUsadas)
                    
                    if letra in palabra:
                        letrasUsadas=letrasUsadas+ letra
                        
                        for i in range(len(palabra)):
                            if palabra[i]==letra:
                                palabraEscondida[i]=letra
                                
                    else:
                        letrasUsadas=letrasUsadas+letra
                        errores=errores+1
                        print()
                        print("Letra incorrecta")
                        print()
                        
                        if errores==7:
                            
                            mensaje=f"Perdiste, la palabra era {palabra} cometiste los {errores} errores"
                            print(mensaje)
                            break
                        
                    if palabraBuscada==palabraEscondida:
                        dic[nom][2]=dic[nom][2]+1
                        print()
                        print("Ganaste!!! la palabra es:", palabra)
                        print()
                        break          
            respuesta=jugarDeVuelta()     
     
    except FileNotFoundError as mensaje:
        print("No se puede abrir el archivo:",mensaje)
    except OSError as mensaje:
        print ("No se puede leer el archivo:",mensaje)
        
    finally:
        try:
            entrada.close()
        except NameError:
            pass
    
    return dic 

def crearArchivo():#2
    """Funcio para crear un archivo con las palabras del registro """
    try:
        entrada= open("Palabras.txt","rt",encoding="UTF8")
        salida=open("PalabrasUsadasAhorcado.txt","wt")
        linea=entrada.readline()
        
        while linea:
            salida.write(linea)
            linea=entrada.readline()           
 
    except FileNotFoundError as mensaje:
        print("No se puede abrir el archivo:",mensaje)
    except OSError as mensaje:
        print ("No se puede leer el archivo:",mensaje)
    
    else:
        print("El archivo se creo correctamente")
    
    finally:
        try:
            entrada.close()
            salida.close()
            print("Cerrado los archivos")
        except NameError:
            pass
      
def buscarPalabra():#4
    """Funcion para buscar palabras en el registro """
    try:
        entrada= open("Palabras.txt","rt",encoding="UTF8")     
        linea=entrada.readline()
        
        palabra=verificarPalabra()
        bandera=True
        while linea:
            linea=linea.replace("\n","")
            
            palabraRegistro=linea
            palabraRegistro=palabraRegistro.rstrip(" ")
            
            if palabraRegistro==palabra:
                print()
                print(f"la palabra {palabra}, se encuentra en el registro")
                bandera=False
                break
            
            linea=entrada.readline()           
        if bandera:
            print()
            print(f"la palabra {palabra}, NO se encuentra en el registro")
            print()
            
    except FileNotFoundError as mensaje:
        print("No se puede abrir el archivo:",mensaje)
    except OSError as mensaje:
        print ("No se puede leer el archivo:",mensaje)
    
    else:
        print("Volviendo al menú")
    
    finally:
        try:
            entrada.close()
        except NameError:
            pass

def opcionUsuario():
    """ Funcion para preguntar si tiene un usuario creado"""
    while True:
        try:
            num=int(input("Tiene un alias creado?(1=Si / 2 = No): "))
            
            
            assert 0< num< 3
            break
        except ValueError:
            print()
            print("Solo se permiten numeros")
        except AssertionError:
            print()
            print("elija un número: 1 o 2")
    return num 

def verificarUsuario(dic):
    
    """Funcion para verificar si el usuario ya esta creado """
    while True:
        
        try:
            
            pal=input("Ingrese un alias: ")
            
            assert pal not in dic, "ese alias ya esta utilizado, ingrese otro"
            assert len(pal)>1, "Ingrese un alias mas largo"
            assert pal.isalpha(),"Solo se permiten palabras"
            assert pal.islower(),"El alias en minusculas"
            break
        except AssertionError as mensaje:
            print()
            print(mensaje)
            print()
    return pal

def buscarUsuario(dic):
    """Funcion para verificar si el usuario ya esta creado """
    while True: 
        try:
            pal=input("Ingrese su alias: ")
            
            assert pal in dic, "El alias no esta en el registro"
            assert len(pal)>1, "Ingrese un alias mas largo"
            assert pal.isalpha(),"Solo se permiten palabras"
            assert pal.islower(),"El alias en minusculas"
            break
        except AssertionError as mensaje:
            print()
            print(mensaje)
            print()
            
            if pal not in dic :
                try:
                    x = int(input("1. para crear nuevo usuario \n 2. Para utilizar uno existente: \n  "))
                    assert 0< x < 3
                    if x == 1:
                        pal= verificarUsuario(dic)
                        dic[pal]=[0,0,0]
                        break
                except ValueError:
                    print()
                    print("Solo se permiten numeros")
                except AssertionError:
                    print()
                    print("elija un número entre 1 y 2")

                
    return pal    

#-----------------programa principal---------------

print("Bienvenidos al ahorcado elija un opcion")        
jugar="Jugar ahorcado"
verPalabras="Crear archivo con palabras utilizadas"
reglas="Ver las reglas del Ahorcado"
buscar="Buscar una palabra"
historial="Ver el historial de cada jugardor"
salir="Salir del Juego"
HistorialJugadores={}

opcion=10
while True:
    try:
        while opcion!=6:
            
            print()
            print("1" f"{jugar:->70}")
            print("2" f"{verPalabras:->70}")
            print("3" f"{reglas:->70}")
            print("4"f"{buscar:->70}")
            print("5"f"{historial:->70}")
            print("6"f"{salir:->70}")
            print()
            opcion=int(input("elija una opcion: "))
            print()
            
            if opcion==1:
                
                matriz=CrearMatriz()
                usuario=opcionUsuario()
                
                if usuario==1:
                    usuarioViejo=buscarUsuario(HistorialJugadores)
                    jugarAhorcado(HistorialJugadores, usuarioViejo)
                
                elif usuario==2:
                    usuarioNuevo=verificarUsuario(HistorialJugadores)
                    HistorialJugadores[usuarioNuevo]=[0,0,0]
                    jugarAhorcado(HistorialJugadores, usuarioNuevo)      
                  
            elif opcion == 2:
                crearArchivo()
            elif opcion== 3:
                print()
                print("Bienvenidos al ahorcado del grupo 8, el objetivo del juego es aprender nuevas palabras,\n" 
                "estas fueron extraídas de la RAE, tenés 80 mil para aprender.\n"
                "Él juego tiene 3 nieveles:\n"
                "\n"
                "Fácil:\n"
                "Los intentos son ilimitados\n"
                "\n"
                "Intermedio:\n"
                "Tenés 7 intentos y las tildes de las palabras son borradas para que no se tome el error\n"
                "\n"
                "Difícil:\n"
                "Tenés 7 intentos y si se ingresa una letra sin tilde se toma un error\n")
                print()
            elif opcion==4:
                buscarPalabra()
            elif opcion==5:
                for usuario in HistorialJugadores:
                    print (usuario , "gano > "+"En facil: "+str(HistorialJugadores[usuario][0])+ " En intermedio: "+ str(HistorialJugadores[usuario][1])+" En dificil: "+str(HistorialJugadores[usuario][2]))
            print()
            
            assert 0< opcion < 7          
        break
    except ValueError:
        print()
        print("Solo se permiten números")
            
    except AssertionError:
        print("elija un número entre 1 y 6")
            
print()
print("Gracias por jugar!!!!")            
      