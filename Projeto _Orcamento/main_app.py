from tkinter import *
from tkinter import Tk, ttk
from PIL import Image, ImageTk


co0 = "black"
co1 = "white"             
co2 = "gray"             
co3 = "blue"             
co4= "red"
co5 = "orange"
co6 = "green"
co7 = "yellow"
co8 = "purple"
co9 = "pink"
co10 = "cyan"
co11 = "magenta"
co12 = "brown"
co13 = "gold"

janela = Tk()
janela.title("")
janela.geometry('800x600')
janela.configure(background=co1)
janela.resizable(width=False, height=False)

style = ttk.Style(janela)
style.theme_use('clam')

frameCima = Frame(janela, width=800, height=150, background=co0, relief= "flat")
frameCima.grid(row=0, column=0)

frameMeio = Frame(janela, width=800, height=250, background=co2, relief= "flat")
frameMeio.grid(row=1, column=0)

frameBaixo = Frame(janela, width=800, height=200, background=co1, relief= "flat")
frameBaixo.grid(row=2, column=0)

app = Label(frameCima, text="Orçamento",compound=LEFT, padx=10, relief=FLAT, anchor=NW, font=('Verdana 40'), bg=co1, fg=co4  )


janela.mainloop()
