#Lista que contiene el mapa (prueba)
mapa=[
[2,2,2,2,2],
[2,4,4,4,2],
[2,4,4,4,2],
[2,4,4,0,2],
[2,2,2,2,2]]

#Metodo para imprimir el mapa
def mapaimpreso():
    impresiondemapa=""
    for columnas in mapa:
        for filas in columnas:
            impresiondemapa=impresiondemapa+" "+str(filas)
        print(impresiondemapa)
        impresiondemapa=""
    
mapaimpreso()

#Identificacion del personaje (prueba)
monoX=3
monoY=3

while True:
    movimiento=str(input("¿Hacia donde te quieres mover? a- izquierda d- derecha w- arriba s- abajo   "))
    
#Movimiento hacia la derecha    
    if movimiento == "d":
        
        if mapa[monoX][monoY+1]==2:
            print("No vas a poder atravesar un muro... Aún ;)")  

        elif mapa[monoX][monoY]==6 and mapa[monoX][monoY+1]==1 and mapa[monoX][monoY+2]==4:
            mapa[monoX][monoY]=3
            mapa[monoX][monoY+2]=1
            monoY=monoY+1
            mapa[monoX][monoY]=0
            mapaimpreso()      


        elif mapa[monoX][monoY]==6 and mapa[monoX][monoY+1]==1 and mapa[monoX][monoY+2]==3:
            mapa[monoX][monoY]=3
            mapa[monoX][monoY+2]=5
            monoY=monoY+1
            mapa[monoX][monoY]=0
            mapaimpreso()      

        elif mapa[monoX][monoY]==6 and mapa[monoX][monoY+1]==3:
            mapa[monoX][monoY]=3
            monoY=monoY+1
            mapa[monoX][monoY]=6
            mapaimpreso()
        
        elif mapa[monoX][monoY]==6 and mapa[monoX][monoY+1]==5 and mapa[monoX][monoY+2]==3:
            mapa[monoX][monoY]=3
            mapa[monoX][monoY+2]=5
            monoY=monoY+1
            mapa[monoX][monoY]=6
            mapaimpreso()
        
        elif mapa[monoX][monoY]==6 and mapa[monoX][monoY+1]==4:
            mapa[monoX][monoY]=3
            monoY=monoY+1
            mapa[monoX][monoY]=0
            mapaimpreso()
       
        elif mapa[monoX][monoY+1]==4:
            mapa[monoX][monoY]=4
            monoY=monoY+1
            mapa[monoX][monoY]=0
            mapaimpreso()   

        elif mapa[monoX][monoY+1]==3:
            mapa[monoX][monoY]=4
            monoY=monoY+1
            mapa[monoX][monoY]=6
            mapaimpreso()

        elif mapa[monoX][monoY+1]==1 and mapa[monoX][monoY+2]==4:
            mapa[monoX][monoY]=4
            mapa[monoX][monoY+2]=1
            monoY=monoY+1
            mapa[monoX][monoY]=0
            mapaimpreso()

        elif mapa[monoX][monoY+1]==1 and mapa[monoX][monoY+2]==2:
            print ("No puedes atravesar el muro por ti mismo, ¿Qué te hace pensar que con una caja lo haras?")

        elif mapa[monoX][monoY+1]==1 and mapa[monoX][monoY+2]==3:
            mapa[monoX][monoY]=4
            mapa[monoX][monoY+2]=5
            monoY=monoY+1
            mapa[monoX][monoY]=0
            mapaimpreso()
        
        elif mapa[monoX][monoY+1]==1 and mapa[monoX][monoY+2]==1:
            print("Con que trabajos mueves una jajaja")

        elif mapa[monoX][monoY+1]==5 and mapa[monoX][monoY+2]==3:
            mapa[monoX][monoY]=4
            mapa[monoX][monoY+2]=5
            monoY=monoY+1
            mapa[monoX][monoY]=6
            mapaimpreso()

        elif mapa[monoX][monoY+1]==5 and mapa[monoX][monoY+2]==4:
            mapa[monoX][monoY]=3
            mapa[monoX][monoY+2]=1
            monoY=monoY+1
            mapa[monoX][monoY]=6
            mapaimpreso()

        elif mapa[monoX][monoY+1]==5 and mapa[monoX][monoY+2]==2:
            print("No puedes atravesar los muros... aún ;)")

#Movimiento hacia la izquierda    
    elif movimiento == "a":
        
        if mapa[monoX][monoY-1]==2:
            print("No vas a poder atravesar un muro... Aún ;)")  

        elif mapa[monoX][monoY]==6 and mapa[monoX][monoY-1]==1 and mapa[monoX][monoY-2]==4:
            mapa[monoX][monoY]=3
            mapa[monoX][monoY-2]=1
            monoY=monoY-1
            mapa[monoX][monoY]=0
            mapaimpreso()      


        elif mapa[monoX][monoY]==6 and mapa[monoX][monoY-1]==1 and mapa[monoX][monoY-2]==3:
            mapa[monoX][monoY]=3
            mapa[monoX][monoY-2]=5
            monoY=monoY-1
            mapa[monoX][monoY]=0
            mapaimpreso()      

        elif mapa[monoX][monoY]==6 and mapa[monoX][monoY-1]==3:
            mapa[monoX][monoY]=3
            monoY=monoY-1
            mapa[monoX][monoY]=6
            mapaimpreso()
        
        elif mapa[monoX][monoY]==6 and mapa[monoX][monoY-1]==5 and mapa[monoX][monoY-2]==3:
            mapa[monoX][monoY]=3
            mapa[monoX][monoY-2]=5
            monoY=monoY-1
            mapa[monoX][monoY]=6
            mapaimpreso()
        
        elif mapa[monoX][monoY]==6 and mapa[monoX][monoY-1]==4:
            mapa[monoX][monoY]=3
            monoY=monoY-1
            mapa[monoX][monoY]=0
            mapaimpreso()
       
        elif mapa[monoX][monoY-1]==4:
            mapa[monoX][monoY]=4
            monoY=monoY-1
            mapa[monoX][monoY]=0
            mapaimpreso()   

        elif mapa[monoX][monoY-1]==3:
            mapa[monoX][monoY]=4
            monoY=monoY-1
            mapa[monoX][monoY]=6
            mapaimpreso()

        elif mapa[monoX][monoY-1]==1 and mapa[monoX][monoY-2]==4:
            mapa[monoX][monoY]=4
            mapa[monoX][monoY-2]=1
            monoY=monoY-1
            mapa[monoX][monoY]=0
            mapaimpreso()

        elif mapa[monoX][monoY-1]==1 and mapa[monoX][monoY-2]==2:
            print ("No puedes atravesar el muro por ti mismo, ¿Qué te hace pensar que con una caja lo haras?")

        elif mapa[monoX][monoY-1]==1 and mapa[monoX][monoY-2]==3:
            mapa[monoX][monoY]=4
            mapa[monoX][monoY-2]=5
            monoY=monoY-1
            mapa[monoX][monoY]=0
            mapaimpreso()
        
        elif mapa[monoX][monoY-1]==1 and mapa[monoX][monoY-2]==1:
            print("Con que trabajos mueves una jajaja")

        elif mapa[monoX][monoY-1]==5 and mapa[monoX][monoY-2]==3:
            mapa[monoX][monoY]=4
            mapa[monoX][monoY-2]=5
            monoY=monoY-1
            mapa[monoX][monoY]=6
            mapaimpreso()

        elif mapa[monoX][monoY-1]==5 and mapa[monoX][monoY-2]==4:
            mapa[monoX][monoY]=3
            mapa[monoX][monoY-2]=1
            monoY=monoY-1
            mapa[monoX][monoY]=6
            mapaimpreso()

        elif mapa[monoX][monoY-1]==5 and mapa[monoX][monoY-2]==2:
            print("No puedes atravesar los muros... aún ;)")

#Movimiento hacia la arriba    
    elif movimiento == "w":
        
        if mapa[monoX-1][monoY]==2:
            print("No vas a poder atravesar un muro... Aún ;)")  

        elif mapa[monoX][monoY]==6 and mapa[monoX-1][monoY]==1 and mapa[monoX-2][monoY]==4:
            mapa[monoX][monoY]=3
            mapa[monoX-2][monoY]=1
            monoX=monoX-1
            mapa[monoX][monoY]=0
            mapaimpreso()      


        elif mapa[monoX][monoY]==6 and mapa[monoX-1][monoY]==1 and mapa[monoX-2][monoY]==3:
            mapa[monoX][monoY]=3
            mapa[monoX-2][monoY]=5
            monoX=monoX-1
            mapa[monoX][monoY]=0
            mapaimpreso()      

        elif mapa[monoX][monoY]==6 and mapa[monoX-1][monoY]==3:
            mapa[monoX][monoY]=3
            monoX=monoX-1
            mapa[monoX][monoY]=6
            mapaimpreso()
        
        elif mapa[monoX][monoY]==6 and mapa[monoX-1][monoY]==5 and mapa[monoX-2][monoY]==3:
            mapa[monoX][monoY]=3
            mapa[monoX-2][monoY]=5
            monoX=monoX-1
            mapa[monoX][monoY]=6
            mapaimpreso()
        
        elif mapa[monoX][monoY]==6 and mapa[monoX-1][monoY]==4:
            mapa[monoX][monoY]=3
            monoX=monoX-1
            mapa[monoX][monoY]=0
            mapaimpreso()
       
        elif mapa[monoX-1][monoY]==4:
            mapa[monoX][monoY]=4
            monoX=monoX-1
            mapa[monoX][monoY]=0
            mapaimpreso()   

        elif mapa[monoX-1][monoY]==3:
            mapa[monoX][monoY]=4
            monoX=monoX-1
            mapa[monoX][monoY]=6
            mapaimpreso()

        elif mapa[monoX-1][monoY]==1 and mapa[monoX-2][monoY]==4:
            mapa[monoX][monoY]=4
            mapa[monoX-2][monoY]=1
            monoX=monoX-1
            mapa[monoX][monoY]=0
            mapaimpreso()

        elif mapa[monoX-1][monoY]==1 and mapa[monoX-2][monoY]==2:
            print ("No puedes atravesar el muro por ti mismo, ¿Qué te hace pensar que con una caja lo haras?")

        elif mapa[monoX-1][monoY]==1 and mapa[monoX-2][monoY]==3:
            mapa[monoX][monoY]=4
            mapa[monoX-2][monoY]=5
            monoX=monoX-1
            mapa[monoX][monoY]=0
            mapaimpreso()
        
        elif mapa[monoX-1][monoY]==1 and mapa[monoX-2][monoY]==1:
            print("Con que trabajos mueves una jajaja")

        elif mapa[monoX-1][monoY]==5 and mapa[monoX-2][monoY]==3:
            mapa[monoX][monoY]=4
            mapa[monoX-2][monoY]=5
            monoX=monoX-1
            mapa[monoX][monoY]=6
            mapaimpreso()

        elif mapa[monoX-1][monoY]==5 and mapa[monoX-2][monoY]==4:
            mapa[monoX][monoY]=3
            mapa[monoX-2][monoY]=1
            monoX=monoX-1
            mapa[monoX][monoY]=6
            mapaimpreso()

        elif mapa[monoX-1][monoY]==5 and mapa[monoX-2][monoY]==2:
            print("No puedes atravesar los muros... aún ;)")

#Movimiento hacia la abajo    
    elif movimiento == "s":
        
        if mapa[monoX+1][monoY]==2:
            print("No vas a poder atravesar un muro... Aún ;)")  

        elif mapa[monoX][monoY]==6 and mapa[monoX+1][monoY]==1 and mapa[monoX+2][monoY]==4:
            mapa[monoX][monoY]=3
            mapa[monoX+2][monoY]=1
            monoX=monoX+1
            mapa[monoX][monoY]=0
            mapaimpreso()      


        elif mapa[monoX][monoY]==6 and mapa[monoX+1][monoY]==1 and mapa[monoX+2][monoY]==3:
            mapa[monoX][monoY]=3
            mapa[monoX+2][monoY]=5
            monoX=monoX+1
            mapa[monoX][monoY]=0
            mapaimpreso()      

        elif mapa[monoX][monoY]==6 and mapa[monoX+1][monoY]==3:
            mapa[monoX][monoY]=3
            monoX=monoX+1
            mapa[monoX][monoY]=6
            mapaimpreso()
        
        elif mapa[monoX][monoY]==6 and mapa[monoX+1][monoY]==5 and mapa[monoX+2][monoY]==3:
            mapa[monoX][monoY]=3
            mapa[monoX+2][monoY]=5
            monoX=monoX+1
            mapa[monoX][monoY]=6
            mapaimpreso()
        
        elif mapa[monoX][monoY]==6 and mapa[monoX+1][monoY]==4:
            mapa[monoX][monoY]=3
            monoX=monoX+1
            mapa[monoX][monoY]=0
            mapaimpreso()
       
        elif mapa[monoX+1][monoY]==4:
            mapa[monoX][monoY]=4
            monoX=monoX+1
            mapa[monoX][monoY]=0
            mapaimpreso()   

        elif mapa[monoX+1][monoY]==3:
            mapa[monoX][monoY]=4
            monoX=monoX+1
            mapa[monoX][monoY]=6
            mapaimpreso()

        elif mapa[monoX+1][monoY]==1 and mapa[monoX+2][monoY]==4:
            mapa[monoX][monoY]=4
            mapa[monoX+2][monoY]=1
            monoX=monoX+1
            mapa[monoX][monoY]=0
            mapaimpreso()

        elif mapa[monoX+1][monoY]==1 and mapa[monoX+2][monoY]==2:
            print ("No puedes atravesar el muro por ti mismo, ¿Qué te hace pensar que con una caja lo haras?")

        elif mapa[monoX+1][monoY]==1 and mapa[monoX+2][monoY]==3:
            mapa[monoX][monoY]=4
            mapa[monoX+2][monoY]=5
            monoX=monoX+1
            mapa[monoX][monoY]=0
            mapaimpreso()
        
        elif mapa[monoX+1][monoY]==1 and mapa[monoX+2][monoY]==1:
            print("Con que trabajos mueves una jajaja")

        elif mapa[monoX+1][monoY]==5 and mapa[monoX+2][monoY]==3:
            mapa[monoX][monoY]=4
            mapa[monoX+2][monoY]=5
            monoX=monoX+1
            mapa[monoX][monoY]=6
            mapaimpreso()

        elif mapa[monoX+1][monoY]==5 and mapa[monoX+2][monoY]==4:
            mapa[monoX][monoY]=3
            mapa[monoX+2][monoY]=1
            monoX=monoX+1
            mapa[monoX][monoY]=6
            mapaimpreso()

        elif mapa[monoX+1][monoY]==5 and mapa[monoX+2][monoY]==2:
            print("No puedes atravesar los muros... aún ;)")

    else:
        print ("Oprimiste la tecla equivocada")
