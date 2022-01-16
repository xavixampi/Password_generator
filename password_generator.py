#Importamos las librerias necesarias
import random
from tkinter import *

#Creamos una variable con los caracteres que queremos que se puedan utilzar para crear la contraseña
chars='abcdefghijklmñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ123456789!@#$%&*'

#Crear la ventana y personalizarla
root=Tk()
root.geometry('800x400')
root.configure(bg='cyan2')
root.resizable(0,0)

#Funcion para generar un numero y que posteriormente se muestre en la ventana. Será el comando del botón b1
def Number():
    #El programa intentara convertir el valor de e1 en un numero entero
    try:
        x=int(e1.get())
        #Si el valor de e1 es mayor a 0 el porgrama creara una contraseña aleatoria
        if x>0:
            for i in range(1):
                password=''
            for j in range(0,x):
                password_characters=random.choice(chars)
                password+=password_characters
        #Mostraremos en pantalla la contraseña generada
        l2=Entry(root,text=password,bg='seagreen2',fg='black',justify='center')
        l2.insert(0,password)  
        l2.configure(state='readonly')
        l2.place(x=0,y=300,height=15,width=800)
        l2.configure(font=("Arial", 10, 'bold'))

        #Nos saldra un aviso que dirá que podemos copiar la contraseña
        answer.config(text='The password has been created\nCtrl+C to copy')

    #Si el numero no se ha podido convertir en entero nos saldrá un aviso
    except ValueError:
        answer.config(text='Error\nIntroduce solo numeros enteros',bg='red4',fg='gold')


#Creamos una etiqueta para mostrar el título del pantalla
ltitle=Label(root,text='PASSWORD GENERATOR',bg='cyan2',fg='magenta4')
ltitle.place(x=200,y=20,width=400,height=100)
ltitle.configure(font=("Arial", 16, 'bold',"italic"))

#Creamos una etiqueta y una entrada de texto para introducir el numero de caracteres que queremos
l1=Label(root,text='Number of characters:')
l1.place(x=150+37.5,y=100,height=50,width=200)

e1=Entry(root)
e1.place(x=350+37.5,y=100,height=50,width=200)

#Creamos un boton para enviar la informacion introducida en e1. El comando es la función Number, creada anteriormente
b1=Button(root,text='Send',command=Number)
b1.place(x=589,y=100,height=50,width=50)

#Etiqueta de texto para decir que se está generando la contraseña
answer=Label(root,text='...Loading password...',bg='cyan2',fg='black')
answer.place(x=287.5,y=175,width=225,height=100)
answer.configure(font=("Arial", 10, 'bold'))



root.mainloop()


