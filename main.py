from tkinter import *
import requests
import json
from PIL import ImageTk, Image
import urllib.request
from io import BytesIO
import random

root = Tk()
root.title('API - Rick and Morty')
root.geometry('800x400')
root.config(bg='blue')
root.config()

etiqueta_01 = Label(root, bg='blue', font='Monospace 16 bold', fg='white')
etiqueta_01.place(x=390,y=40)
etiqueta_02 = Label(root, bg='blue', font='Monospace 16 bold', fg='white')
etiqueta_02.place(x=390,y=110)
etiqueta_03 = Label(root, bg='blue', font='Monospace 16 bold', fg='white')
etiqueta_03.place(x=390,y=180)
etiqueta_04 = Label(root, bg='blue', font='Monospace 16 bold', fg='white')
etiqueta_04.place(x=390,y=250)
 
def buscar():
    num = random.randint(1,150)
    url = 'https://rickandmortyapi.com/api/character/{}'.format(num)
    r = requests.get(url)
    j = r.json()
    i = j['image']
    etiqueta_01['text'] = 'Nombre: '+j['name']
    etiqueta_02['text'] = 'Estado: '+j['status']
    etiqueta_03['text'] = 'Especie: '+j['species']
    if j['type'] == '':
        etiqueta_04['text'] = j['type']
    else:
        etiqueta_04['text'] = 'Tipo: '+j['type']
    respuesta = requests.get(i)
    imagen_01 = Image.open(BytesIO(respuesta.content))
    new_img = imagen_01.resize((300,256))
    render = ImageTk.PhotoImage(new_img)
    img1 = Label(root, image = render)
    img1.image = render
    img1.place(x=50,y=38)

buscar()

boton_01 = Button(root, text='Buscar', height='2', width='40', command = buscar)
boton_01.place(x=50,y=320)

boton_02 = Button(root, text='Salir', height='2', width='40', command = root.quit)
boton_02.place(x=410,y=320)

root.mainloop()