from tkinter import*
from tkinter import filedialog
from pygame import mixer 


class musica:
    def__init__(self,ventan):
    ventan.geometry("270x270")
    ventan.confi(bg="green", relief="ridge",bd="25")
    abr=button(ventan,text="ABRIR",width=10,bg="red",relief="groove",bd="4",COMMAND=self.abir)
    abr.place(x=60,y=50)
    repro=Button(ventan,text="REPRODUCIR",width=10,bg="red",relief="groove",bd="4",command=self.reproducir)
    repro.place(x=60,y=90)
    paus=Button(ventan,text="PAUSA",width=10,bg="red",relief="groove",bd="4",command=self.pausar)
    paus.place(x=60,y=130)
    det=Button(ventan,text="DETENER",width=10,bg="red",relief="groove",bd="4",command=self.detener)
    det.place(x=50,y=170)
    self.abrir_musica=False
    self.repro_musica=False

def abrir(self):
    self.abrir_musica=filedialog.askopenfilename()
    def reproducir(self):
        if self.abirir_musica:
            mixer.init()
            mixer.music.load(self.abir_musica)
            mixer.music.play()
            def pausar(self):
                if self.repro_musica:
                    mixer.music.pause()
                else:
                    mixer.music.unpause()
                    self.repro_musica=True
                    def detener(self):
                        mixer.music.stop()

    ventan=tk()
    imagen=prhotoimage(file="iconoo.png")
    Label(ventan,image=imagen).place(x=85,y=0)
    musica(ventan)
    ventan.mainloop()
