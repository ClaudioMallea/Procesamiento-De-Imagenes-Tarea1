import numpy as np
import skimage
import os
from skimage import data
from skimage import io
import matplotlib.pylab as plt
from skimage import color
import Python.pai.basic  as pai
from skimage.filters import threshold_adaptive
from Stack import Stack



#Funcion que entrega una lista de los 8-conexos siguientes de un vertices dado:
def conexos8_siguientes(x,y, punto_i, punto_j):
    lista=[]
    if(x+1==punto_i and y==punto_j):
        lista.append([punto_i-1,punto_j+1])
        lista.append([punto_i,punto_j+1])
        lista.append([punto_i+1,punto_j+1])
        lista.append([punto_i+1,punto_j])
        lista.append([punto_i+1,punto_j-1])
        lista.append([punto_i,punto_j-1])
        lista.append([punto_i-1,punto_j-1])
    elif(x+1==punto_i and y-1==punto_j):
        lista.append([punto_i,punto_j+1])
        lista.append([punto_i+1,punto_j+1])
        lista.append([punto_i+1,punto_j])
        lista.append([punto_i+1,punto_j-1])
        lista.append([punto_i,punto_j-1])
        lista.append([punto_i-1,punto_j-1])
        lista.append([punto_i-1,punto_j])
    elif(x==punto_i and y-1==punto_j):
        lista.append([punto_i+1,punto_j+1])
        lista.append([punto_i+1,punto_j])
        lista.append([punto_i+1,punto_j-1])
        lista.append([punto_i,punto_j-1])
        lista.append([punto_i-1,punto_j-1])
        lista.append([punto_i-1,punto_j])
        lista.append([punto_i-1,punto_j+1])
    elif(x-1==punto_i and y-1==punto_j):
        lista.append([punto_i+1,punto_j])
        lista.append([punto_i+1,punto_j-1])
        lista.append([punto_i,punto_j-1])
        lista.append([punto_i-1,punto_j-1])
        lista.append([punto_i-1,punto_j])
        lista.append([punto_i-1,punto_j+1])
        lista.append([punto_i,punto_j+1])
    elif (x-1 == punto_i and y == punto_j):
        lista.append([punto_i+1,punto_j-1])
        lista.append([punto_i,punto_j-1])
        lista.append([punto_i-1,punto_j-1])
        lista.append([punto_i-1,punto_j])
        lista.append([punto_i-1,punto_j+1])
        lista.append([punto_i,punto_j+1])
        lista.append([punto_i+1,punto_j+1] )
    elif (x-1 == punto_i and y+1 == punto_j):
        lista.append( [punto_i,punto_j-1])
        lista.append([punto_i-1,punto_j-1])
        lista.append([punto_i-1,punto_j])
        lista.append([punto_i-1,punto_j+1])
        lista.append([punto_i,punto_j+1])
        lista.append([punto_i+1,punto_j+1])
        lista.append([punto_i+1,punto_j])
    elif (x == punto_i and y+1 == punto_j):
        lista.append([punto_i-1,punto_j-1])
        lista.append([punto_i-1,punto_j])
        lista.append([punto_i-1,punto_j+1])
        lista.append([punto_i,punto_j+1])
        lista.append([punto_i+1,punto_j+1])
        lista.append([punto_i+1,punto_j])
        lista.append([punto_i+1,punto_j-1])
    elif (x+1 == punto_i and y+1 == punto_j):
        lista.append([punto_i-1,punto_j])
        lista.append([punto_i-1,punto_j+1])
        lista.append([punto_i,punto_j+1])
        lista.append([punto_i+1,punto_j+1])
        lista.append([punto_i+1,punto_j])
        lista.append([punto_i+1,punto_j-1])
        lista.append([punto_i,punto_j-1])
    return lista





#Funcion que desde un punto en un Arreglo retorna una lista con los puntos en los que es 4 conexo (s
#si es que esos puntos no estan en la orilla:

def lpointsc(n,Arreglo,j):

    lista=[]
    for x in range(len(Arreglo)):
        for y in range(len(Arreglo[0])):
            if(Arreglo[x][y]==j):
                lista.append((x,y))


    return lista


def lboundaryc(Imagen):
    lista_B=[]

    encontrado=False

    for x in range(len(Imagen)):
        for y in range(len(Imagen[0])):
            if (Imagen[x][y] != 1):
                encontrado=True
                q = (x,y-1)
                p = (x,y)
                q_previos=[]
                q_previos.append(q)
                salvado=p
                lista_B.append(p)
                p=0

                while(p!=(x,y)):

                    Conexos_de_p=conexos8_siguientes(q[0],q[1],salvado[0],salvado[1])

                    for z in Conexos_de_p:

                        q_previos.append(z)
                        if(Imagen[z[0]][z[1]]!=1 ):


                            p=(z[0],z[1])
                            lista_B.append(p)

                            q=q_previos[len(q_previos)-2]
                            salvado=p


                            break




            if(encontrado):

                break
        if(encontrado):

            break


    return lista_B




def ComponenteConexoN(n,Imagen):
    NuevaImagen = np.ones((len(Imagen), len(Imagen[0])))
    for x in range(len(Imagen)):
        for y in range(len(Imagen[0])):
            if(Imagen[x][y]==n):
                NuevaImagen[x][y]=0
    return NuevaImagen

def BoundingBox(Puntos): #toma los puntos de algun componente, o borde de este
    punto_min_columna= 100000
    punto_min_fila=10000
    punto_max_columna=0
    punto_max_fila=0
    for punto in Puntos:
        if (punto[1]<punto_min_columna):
            punto_min_columna=punto[1]
        if (punto[0]<punto_min_fila):
            punto_min_fila=punto[0]
        if  punto[1]>punto_max_columna:
            punto_max_columna=punto[1]
        if  punto[0]>punto_max_fila:
            punto_max_fila=punto[0]
    x=punto_min_fila-1
    y=punto_min_columna-1
    w=punto_max_columna-punto_min_columna
    h=punto_max_fila-punto_min_fila
    boundingbox=[x,y,w,h]
    return boundingbox


def conexo4(x,y,Imagen):
    lista=[]
    if((Imagen[x-1][y+1]==False) ):
        lista.append((x-1, y+1))
    if ((Imagen[x][y + 1] == False)):
        lista.append((x, y + 1))
    if((Imagen[x+1][y+1]==False)  ):
        lista.append((x+1, y+1))
    if((Imagen[x+1][y]==False) ) :
        lista.append((x+1,y))
    if((Imagen[x+1][y-1]==False) ):
        lista.append((x+1, y-1))
    if((Imagen[x][y-1]==False) ):
        lista.append((x, y-1))
    if((Imagen[x-1][y-1]==False) ):
        lista.append((x-1, y-1))

    if((Imagen[x-1][y]==False) ):
        lista.append((x-1, y))

    return lista

def conexo_4(x,y):
    lista=[]
    lista.append((x, y + 1))
    lista.append((x + 1, y))
    lista.append((x, y - 1))
    lista.append((x - 1, y))
    return lista



def dfs(x,y,Arreglo,Imagen,n):

    pila=Stack()
    pila.push([x,y])
    while(not pila.isEmpty()):
        v=pila.pop()



        if(Imagen[v[0]][v[1]]!=True):

            if (Arreglo[v[0]][v[1]] == 1): #primera vez que se visita este punto

                Arreglo[v[0]][v[1]] = n

                for (x,y) in conexo4(v[0],v[1],Imagen) :


                    pila.push([x,y])
    return Arreglo




"""for i in range(0, len(binary_adaptive)):
    for j in range(0, len(binary_adaptive[0])):
        print(binary_adaptive[i][j])"""

#def imagenAcomponente(imagen):


if __name__ == '__main__':

    ##Imagen normal a imagen binarizada
    filename = 'D:\Procesamiento de imagenes\Rut_1.jpg'
    image = io.imread(filename)

    red = image[:, :, 0]
    green = image[:, :, 1]
    blue = image[:, :, 2]
    image = 0.299 * red + 0.587 * green + 0.114 * blue


            #Metodo Otsu
    otsu_th = pai.getOtsu(image)
    bin_image = pai.threshold(image, otsu_th)



            #Metodo Adaptativo
    block_size = 35
    binary_adaptive = threshold_adaptive(image, block_size, offset=10)

    """        #Mostrar comparacion
    #xs[0].imshow(image, cmap="gray", vmin=0, vmax=255)
    #xs[0].set_title("Imagen gris")
    #xs[1].imshow(bin_image*255, cmap="gray", vmin=0, vmax=255)
    #xs[1].set_title("Método Otsu")
    #xs[2].imshow(binary_adaptive*255, cmap="gray", vmin=0, vmax=255)
    #xs[2].set_title("Método Adaptativo")


    #xs[0].axis("off")
    #xs[1].axis("off")
    #xs[2].axis("off")"""




    ArregloComponentes = np.ones((len(binary_adaptive),len(binary_adaptive[0])))



    n=2


    for x in range(len(binary_adaptive)):
        for y in range(len(binary_adaptive[0])):
            if(binary_adaptive[x][y]==False and ArregloComponentes[x][y]==1):
                dfs(x, y, ArregloComponentes, binary_adaptive, n)
                n=n+1
                #imgplot = plt.imshow(ArregloComponentes*255)
                #plt.show()


    id=n-2
#PARA EL INFORME
    for i in range(2,12):
        Imagen10=ComponenteConexoN(i, ArregloComponentes)

        hola = np.ones((51, 220))
        for punto in lboundaryc(Imagen10):
            hola[punto[0]][punto[1]] = 0
        imgplot = plt.imshow(hola * 255)
        plt.show()

    print(BoundingBox(lboundaryc(Imagen10)))