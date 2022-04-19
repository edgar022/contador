


#ventana
from pdb import Restart
import tkinter #agregsmos la libreria
ventana=tkinter.Tk()#agregamos la ventana
ventana.title("contador")#titulo de la ventanita
ventana.geometry("400x400")#tamano de pixeles

def changeColor(valor):
    if int(valor) < 0:
        num.config(fg="red")
    elif int(valor) ==0:
        num.config(fg="black")
    elif int(valor) >0:
        num.config(fg="blue")







#funciones de suma resta y reiniciar
def suma():
    valor=int(num["text"])
    num["text"]=f"{valor +1}"
    changeColor(valor)
def resta():
    valor=int(num["text"])
    num["text"]=f"{valor -1}"
    changeColor(valor)
def reiniciar():
    valor=int(num["text"])
    num["text"]=f"{valor *0}"
    changeColor(valor)


#contador
eumar=tkinter.Button(ventana, text="sumar",bg="green", width=11, height=2, command=suma) #crear botoon y su ancho y largo
eumar.place(x=20,y=50) #en que espacio quiero q aparezca el boton de la ventana
rsuma=tkinter.Button(ventana, text="restar",bg="red", width=11, height=2,command=resta)
rsuma.place(x=157, y=50)
ssuma=tkinter.Button(ventana, text="reiniciar",bg="gray", width=11, height=2,command=reiniciar)
ssuma.place(x=300, y=50)
cont=tkinter.Label(ventana, text="contador",foreground="blue", font="cambria 40")
cont.place(x=100, y= 290)
num=tkinter.Label(ventana, text="0", font="cambria 50")
num.place(x=190, y=175)



ventana.mainloop()#cerramos ventana
