from typing import List

import pysine
import os.path
from os import path
from tkinter import *
import configparser

# Principal
vibes = Tk()
vibes.title("-- Vibes -- v2.2 --")
vibes.iconbitmap(default="vibesico.ico")
vibes.geometry("1100x500+0+0")
vibes.wm_resizable(width=False, height=False)

# Interface - Imagens e Labels
interfaceImg = PhotoImage(file="interfacelogo.png")
fundoInterface = PhotoImage(file="interface.png")

labelFundo = Label(vibes, image=fundoInterface)
labelLogo = Label(vibes, image=interfaceImg, background='white')
labelLogo.place(x=49, y=53)
labelFundo.place(x=0, y=0)

# Arquivo de configuracao
config = configparser.ConfigParser()
config.read('config.ini')
def criar_config():
    if path.exists('config.ini'):
        print('Ok')
    else:
        config.add_section('Frequencias')
        config.set('Frequencias', 'freq', '555, 700, 1000')
        config.set('Frequencias', 'duracao', '1')
        with open('config.ini', 'w') as configfile:
            config.write(configfile)


freq = config.get(section='Frequencias',option='freq')
freqsplit = freq.split(',')
duracao = config.getint('Frequencias', 'duracao')

# Funções
def clique_esquerdo_mouse(arg):
    global flag, x1, y1
    flag = not flag

    if flag:
        x1 = arg.x
        y1 = arg.y

    else:
        print(f'width={arg.x - x1}, height={arg.y - y1}, x={x1}, y={y1}')


def frequencia_botao4():
    global entryfreq
    frequencia4 = entryfreq.get()
    pysine.sine(int(frequencia4), duracao)


def som_frequencia(botao):
    global frequencia
    if botao == 1:
        pysine.sine(int(freqsplit[0]), 1)

    elif botao == 2:
        pysine.sine(int(freqsplit[1]), 1)

    elif botao == 3:
        pysine.sine(int(freqsplit[2]), 1)

    elif botao == 4:
        frequencia_botao4()


# Variáveis
flag = x1 = y1 = x = 0

# Criação dos botões
bt1 = Button(vibes, text='Opção 1\nFrequência ' + str(freqsplit[0]) + 'hz', font="Arial 14", command=lambda: som_frequencia(1))
bt2 = Button(vibes, text='Opção 2\nFrequência' + str(freqsplit[1]) + 'hz', font="Arial 14", command=lambda: som_frequencia(2))
bt3 = Button(vibes, text='Opção 3\nFrequência' + str(freqsplit[2]) + 'hz', font="Arial 14", command=lambda: som_frequencia(3))
bt4 = Button(vibes, text="OK", font="Arial 14", command=lambda: frequencia_botao4())

bt1.place(width=279, height=51, x=79, y=217)
bt2.place(width=279, height=51, x=79, y=287)
bt3.place(width=279, height=51, x=79, y=355)
bt4.place(width=72, height=51, x=285, y=430)


# Entry
def limitarEntry(*args):
    value = limite.get()
    if len(value) > 5: limite.set(value[:5])


limite = StringVar()
limite.trace('w', limitarEntry)

entryfreq = Entry(vibes, font="Arial 16", justify=CENTER, textvariable=limite)
entryfreq.place(width=206, height=51, x=79, y=431)

# Eventos
vibes.bind("<Button-1>", clique_esquerdo_mouse)
vibes.mainloop()
