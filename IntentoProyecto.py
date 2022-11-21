from tkinter import Tk, Button, Entry, Label, PhotoImage, Frame
from PIL import Image
import requests
import time

class Aplicacion(Frame):
    def __init__(self, master, *args):
        super().__init__(master, *args)
        self.click = True

        self.master.columnconfigure(0, weight = 1)
        self.master.columnconfigure(1, weight = 1)
        self.master.rowconfigure(1, weight = 1)
        self.master.columnconfigure(2, weight = 1)
        self.master.rowconfigure(2, weight = 1)

        self.frame = Frame(self.master, bg = "white", highlightbackground = "gray10", highlightthickness = 2)
        self.frame.grid(columnspan = 3, row = 0, sticky = "nsew", padx = 5, pady= 5)

        self.frame2 = Frame(self.master, bg = "pale green", highlightbackground = "LightBlue4", highlightthickness = 2)
        self.frame2.grid(column = 0, row = 1, sticky = "nsew", padx = 5, pady= 5)
        self.frame3 = Frame(self.master, bg = "light sky blue", highlightbackground = "LightBlue4", highlightthickness = 2)
        self.frame3.grid(column = 1, row = 1, sticky = "nsew", padx = 5, pady= 5)
        self.frame4 = Frame(self.master, bg = "dark orange", highlightbackground = "LightBlue4", highlightthickness = 2)
        self.frame4.grid(column = 2, row = 1, sticky = "nsew", padx = 5, pady= 5)

        self.frame5 = Frame(self.master, bg = "SeaGreen2", highlightbackground = "LightBlue4", highlightthickness = 2)
        self.frame5.grid(column = 0, row = 2, sticky = "nsew", padx = 5, pady= 5)
        self.frame6 = Frame(self.master, bg = "light sea green", highlightbackground = "LightBlue4", highlightthickness = 2)
        self.frame6.grid(column = 1, row = 2, sticky = "nsew", padx = 5, pady= 5)
        self.frame7 = Frame(self.master, bg = "medium aquamarine", highlightbackground = "LightBlue4", highlightthickness = 2)
        self.frame7.grid(column = 2, row = 2, sticky = "nsew", padx = 5, pady= 5)

        self.widgets()

    def animacion(self):
        self.frame.config(highlightbackground = "dark slate blue")
        self.frame2.config(highlightbackground = "black")
        self.frame3.config(highlightbackground = "black")
        self.frame4.config(highlightbackground = "black")
        self.frame5.config(highlightbackground = "black")
        self.frame6.config(highlightbackground = "black")
        self.frame7.config(highlightbackground = "black")
        self.obtener_tiempo()
        gif = Image.open("buscar.gif")
        frames = gif.n_frames
        if (self.click == True) :
            for i in range (1, frames):
                self.inicio = PhotoImage(file= "buscar.gif", format= "gif -index %i" %(i))
                self.boton_inicio["image"] = self.inicio
                time.sleep(0.04)
                self.master.update()
                self.click = False
                if (i + 1 == frames):
                    self.click = True
                
    def obtener_tiempo(self):
        ciudad = self.ingresa_ciudad.get()
        #key = "a83012c82494fd9b985c63b560cb55fc"
        #API = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}"
        #Coordenadas = "http://api.openweathermap.org/geo/1.0/direct?q={city name}&appid={API key}"
        coordenadas = "http://api.openweathermap.org/geo/1.0/direct?q="+ ciudad + "&appid=a83012c82494fd9b985c63b560cb55fc"
        try:
            resultadosCoordenadas = requests.get(coordenadas)
            json_datoscoordenadas = resultadosCoordenadas.json()
            lat = str(json_datoscoordenadas["lat"])
            lon = str(json_datoscoordenadas["lon"])
            nombreCiudad = str(json_datoscoordenadas["country"])
        except:
            lat = "-"
            lon = "-"
            nombreCiudad = "-"
        print(lat)
        print(lon)
        print(nombreCiudad)
        api = "api.openweathermap.org/data/2.5/weather?q={"+ ciudad +"}&appid={a83012c82494fd9b985c63b560cb55fc}"
        try: 
            resultados = requests.get(api)
            json_datosclima = resultados.json()
            self.temperatura["text"] = str(int(json_datosclima["main"]["temp"] - 273.15)) + "°C"
            self.temperatura_minima["text"] = str(int(json_datosclima["main"]["temp_min"] - 273.15)) + "°C"
            self.temperatura_maxima["text"] = str(int(json_datosclima["main"]["temp_max"] - 273.15)) + "°C"
            self.presion["text"] = str(json_datosclima["main"]["pressure"]) + "hPa"
            self.humedad["text"] = str(json_datosclima["main"]["humidity"]) + "%"
            self.viento["text"] = str(int(json_datosclima["wind"]["speed"]) * 18/5) + "km/h"
            self.localidad["text"] = json_datosclima["name"] + "-" + json_datosclima["sys"]["country"]
            print(json_datosclima)
        except:
            self.aviso["text"] = "Error"
            self.temperatura["text"] = "-"
            self.temperatura_minima["text"]  = "-"
            self.temperatura_maxima["text"] = "-"
            self.presion["text"]  = "-"
            self.humedad["text"] = "-"
            self.viento["text"] = "-"
            self.master.update()
            time.sleep(1)
            self.aviso["text"] = ""
            self.localidad["text"] = ""

    def widgets(self):
        self.inicio = PhotoImage(file = "buscar.gif")
        self.imagen_temperatura = PhotoImage(file = "temperatura.png")
        self.imagen_temperatura_minima = PhotoImage(file = "temperatura_minima.png")
        self.imagen_temperatura_maxima = PhotoImage(file = "temperatura_maxima.png")
        self.imagen_humedad = PhotoImage(file = "humedad.png")
        self.imagen_viento = PhotoImage(file = "viento.png")
        self.imagen_presion = PhotoImage(file = "presion.png")
        
        self.boton_inicio = Button(self.frame, image = self.inicio, bg = "red", highlightthickness = 0, activebackground = "gray2", bd = 0, command = self.animacion)
        self.boton_inicio.grid(column = 0, row = 0, padx = 2, pady = 2)
        self.ingresa_ciudad = Entry(self.frame, font = ("Trebuchet MS", 12), highlightbackground = "gray30", highlightcolor = "black", highlightthickness = 2)
        self.ingresa_ciudad.grid(column = 1, row = 0)
        Label(self.frame, text = "Buscar...", fg = "gray55", bg = "white", font = ("Trebuchet MS", 10)).grid(column = 2, row = 0, padx = 5)
        
        self.aviso = Label(self.frame, fg = "red2", bg = "white", font = ("Comic Sans MS", 12))
        self.aviso.grid(column = 3, row = 0, padx = 5)
        self.localidad = Label(self.frame, fg = "blue", bg = "white", font = ("Tahoma", 12))
        self.localidad.grid(column = 4, row = 0, padx = 5)

        Label(self.frame2, text = "Temperatura", bg = "pale green", font = ("Arial Black", 12)).pack(expand = True)
        Label(self.frame4, text = "Temperatura \n Máxima", bg = "dark orange", font = ("Arial Black", 12)).pack(expand = True)
        Label(self.frame3, text = "Temperatura \n Mínima", bg = "light sky blue", font = ("Arial Black", 12)).pack(expand = True)
        Label(self.frame6, text = "Húmedad", bg = "light sea green", font = ("Arial Black", 12)).pack(expand = True)
        Label(self.frame5, text = "Viento", bg = "SeaGreen2", font = ("Arial Black", 12)).pack(expand =True)
        Label(self.frame7, text = "Presión", bg = "medium aquamarine", font = ("Arial Black", 12)).pack(expand = True)

        Label(self.frame2, image = self.imagen_temperatura, bg = "pale green").pack(expand = True, side = "left")
        Label(self.frame3, image = self.imagen_temperatura_minima, bg = "light sky blue").pack(expand = True, side = "left")
        Label(self.frame4, image = self.imagen_temperatura_maxima, bg = "dark orange").pack(expand = True, side = "left")
        Label(self.frame5, image = self.imagen_viento, bg = "SeaGreen2").pack(expand = True, side = "left")
        Label(self.frame6, image = self.imagen_humedad, bg = "light sea green").pack(expand = True, side = "left")
        Label(self.frame7, image = self.imagen_presion, bg = "medium aquamarine").pack(expand = True, side = "left")

        self.temperatura = Label(self.frame2, bg = "pale green", font = ("Impact", 20))
        self.temperatura.pack(expand = True, side = "right")
        self.temperatura_maxima = Label(self.frame4, bg = "dark orange", font = ("Impact", 20))
        self.temperatura_maxima.pack(expand = True, side = "right")
        self.temperatura_minima = Label(self.frame3, bg = "light sky blue", font = ("Impact", 20))
        self.temperatura_minima.pack(expand = True, side = "right")
        self.humedad = Label(self.frame6, bg = "light sea green", font = ("Impact", 20))
        self.humedad.pack(expand = True, side = "right")
        self.viento = Label(self.frame5, bg = "SeaGreen2", font = ("Impact", 20))
        self.viento.pack(expand = True, side = "right")
        self.presion = Label(self.frame7, bg = "medium aquamarine", font = ("Impact", 20))
        self.presion.pack(expand = True, side = "right")

if (__name__ == "__main__"):
    ventana_Aplicacion = Tk()
    ventana_Aplicacion.title("")
    ventana_Aplicacion.config(bg = "white")
    ventana_Aplicacion.minsize(height = 300, width = 500)
    ventana_Aplicacion.call("wm", "iconphoto", ventana_Aplicacion._w, PhotoImage(file = "temperatura.png"))
    ventana_Aplicacion.geometry("500x300+180+80")
    app = Aplicacion(ventana_Aplicacion)
    app.mainloop()