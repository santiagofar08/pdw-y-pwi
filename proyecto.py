from tkinter import Button, Label, Tk, filedialog, ttk, Frame, PhotoImage
import pygame
import mutagen  
import random

pygame.mixer.init(frequency=44100)

# Variables
cancion_actual = ''
direcion = ''
pos = 0
n = 0

# Función para abrir archivo
def abrir_archivo():
    global direcion, pos, n, cancion_actual
    pos = 0
    n = 0
    direcion = filedialog.askopenfilenames(initialdir='/', title='Escoger la cancion(es)',
                                           filetypes=(('mp3 files', '*.mp3*'), ('All files', '*.*')))
    n = len(direcion)
    cancion_actual = direcion[pos]
    nombre_cancion = cancion_actual.split('/')
    nombre_cancion = nombre_cancion[-1]
    nombre['text'] = nombre_cancion

# Función para iniciar la reproducción
def iniciar():
    global cancion_actual
    pygame.mixer.music.load(cancion_actual)
    pygame.mixer.music.play()
    iniciar_reproduccion()

# Función para actualizar la barra de volumen
def iniciar_reproduccion():
    global cancion_actual, direcion, pos, n, actualizar
    time = pygame.mixer.music.get_pos()
    x = int(int(time) * 0.001)  # Posición de la canción en segundos
    tiempo['value'] = x

    # Establecer volumen
    y = float(int(volumen.get()) * 0.1)
    pygame.mixer.music.set_volume(y)
    nivel['text'] = int(y * 100)

    # Cargar tiempo total de la canción
    audio = mutagen.File(cancion_actual)
    log = audio.info.length
    minutos, segundos = divmod(log, 60)
    minutos, segundos = int(minutos), int(segundos)
    tt = minutos * 60 + segundos
    tiempo['maximum'] = tt  # Establecer máximo de la barra de progreso

    texto['text'] = f"{minutos}:{segundos}"

    # Actualizar cada 100ms
    actualizar = ventana.after(100, iniciar_reproduccion)

    if x == tt:  # Si la canción terminó
        ventana.after_cancel(actualizar)
        texto['text'] = "00:00"
        if pos != n-1:
            pos += 1
            ventana.after(100, iniciar_reproduccion)
            pygame.mixer.music.play()
        else:
            pos = 0

# Función para retroceder
def retroceder():
    global pos, n
    if pos > 0:
        pos = pos - 1
    cantidad['text'] = f"{pos}/{n}"

# Función para adelantar
def adelantar():
    global pos, n
    if pos == n - 1:
        pos = 0
    else:
        pos = pos + 1
    cantidad['text'] = f"{pos}/{n}"

# Interfaz gráfica
ventana = Tk()
ventana.title('Reproductor de Musica')
ventana.iconbitmap('icono.ico')
ventana.config(bg='black')
ventana.resizable(0, 0)

# Estilo de la barra de progreso
estilo = ttk.Style()
estilo.theme_use('clam')
estilo.configure("Vertical.TProgressbar", foreground='green2', background='green2', troughcolor='black', bordercolor='black', lightcolor='green2', darkcolor='green2')

# Frame principal
frame1 = Frame(ventana, bg='black', width=600, height=350)
frame1.grid(column=0, row=0, sticky='nsew')
frame2 = Frame(ventana, bg='black', width=600, height=50)
frame2.grid(column=0, row=1, sticky='nsew')

# Barra de volumen
volumen = ttk.Scale(frame2, to=10, from_=0, orient='horizontal', length=90, style='Horizontal.TScale')
volumen.grid(column=7, row=2)

# Barra de tiempo
tiempo = ttk.Progressbar(frame2, orient='horizontal', length=390, mode='determinate', style="Horizontal.TProgressbar")
tiempo.grid(row=0, columnspan=8, padx=5)

# Etiquetas
texto = Label(frame2, bg='black', fg='green2', width=5)
texto.grid(row=0, column=8)

nombre = Label(frame2, bg='black', fg='red', width=55)
nombre.grid(column=0, row=1, columnspan=8, padx=5)

cantidad = Label(frame2, bg='black', fg='green2')
cantidad.grid(column=8, row=1)

# Imágenes de los botones
imagen1 = PhotoImage(file='carpeta.png')
imagen2 = PhotoImage(file='play.png')
imagen3 = PhotoImage(file='anterior.png')
imagen4 = PhotoImage(file='adelante.png')

# Botones
boton1 = Button(frame2, image=imagen1, command=abrir_archivo)
boton1.grid(column=0, row=2, pady=10)
boton2 = Button(frame2, image=imagen2, bg='yellow', command=iniciar)
boton2.grid(column=1, row=2, pady=10)
atras = Button(frame2, image=imagen3, bg='orange', command=retroceder)
atras.grid(column=5, row=2, pady=10)
adelante = Button(frame2, image=imagen4, bg='green', command=adelantar)
adelante.grid(column=6, row=2, pady=10)

# Estilo para la barra de volumen
style = ttk.Style()
style.configure("Horizontal.TScale", bordercolor='green2', troughcolor='black', background='green2', foreground='green2', lightcolor='green2', darkcolor='black')

# Nivel de volumen
nivel = Label(frame2, bg='black', fg='green2', width=3)
nivel.grid(column=8, row=2)

ventana.mainloop()
