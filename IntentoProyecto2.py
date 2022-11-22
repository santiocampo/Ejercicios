from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import uuid as codigos
import json

global listaDatos, posicionActual

#Configuración interfaz:
#Ventana Principal
interfaz = Tk()
interfaz.title("Pizzeria Pizzato")
interfaz.geometry("1200x720")
imagenFondoInterfaz = ImageTk.PhotoImage(Image.open("fondo.jpg"))
fondoInterfaz = Label(interfaz, image = imagenFondoInterfaz).place(x = 0, y = 0)

#Ingreso Información

marcoInformacion = LabelFrame(interfaz, text = "Información cliente", bg = "PaleTurquoise4", font = ("ArialBlack", 14))
marcoInformacion.grid(row = 0, column = 0, rowspan = 7, columnspan = 5)

barraIngresoID = Label(marcoInformacion,            anchor = "w",           width = 24,
                       height = 1,                  relief = "ridge",       text = "ID",
                       font = ("ArialBlack", 14)   ).grid(row = 1, column = 0)

barraIngresoNombre = Label(marcoInformacion,            anchor = "w",           width = 24,
                           height = 1,                  relief = "ridge",       text = "Nombre",
                           font = ("ArialBlack", 14)   ).grid(row = 2, column = 0)

barraIngresoApellidos = Label(marcoInformacion,            anchor = "w",           width = 24,
                              height = 1,                  relief = "ridge",       text = "Apellidos",
                              font = ("ArialBlack", 14)   ).grid(row = 3, column = 0)

barraIngresoTelefono = Label(marcoInformacion,            anchor = "w",           width = 24,
                             height = 1,                  relief = "ridge",       text = "Teléfono",
                             font = ("ArialBlack", 14)   ).grid(row = 4, column = 0)

barraIngresoTamaño = Label(marcoInformacion,            anchor = "w",           width = 24,
                           height = 1,                  relief = "ridge",       text = "Tamaño",
                           font = ("ArialBlack", 14)   ).grid(row = 5, column = 0)

barraIngresoIngredientes = Label(marcoInformacion,            anchor = "w",           width = 24,
                                 height = 1,                  relief = "ridge",       text = "Ingredientes",
                                 font = ("ArialBlack", 14)   ).grid(row = 6, column = 0)

crearID = StringVar()
crearID.set(codigos.uuid4())

entradaID = Label(marcoInformacion,       anchor = "w",     height = 1,                  
                  relief = "ridge",       textvariable = crearID,      font = ("ArialBlack", 14))
entradaID.grid(row = 1, column = 1)

entradaNombre = Entry(interfaz, width = 30, borderwidth = 2, fg = "black", font = ("ArialBlack", 14))
entradaNombre.grid(row = 2, column = 2, columnspan = 2)

entradaApellidos = Entry(interfaz, width = 30, borderwidth = 2, fg = "black", font = ("ArialBlack", 14))
entradaApellidos.grid(row = 3, column = 2, columnspan= 2)

entradaTelefono = Entry(interfaz, width = 30, borderwidth = 2, fg = "black", font = ("ArialBlack", 14))
entradaTelefono.grid(row = 4, column = 2, columnspan = 2)

entradaTamaño = Entry(interfaz, width = 30, borderwidth = 2, fg = "black", font = ("ArialBlack", 14))
entradaTamaño.grid(row = 5, column = 2, columnspan = 2)

entradaIngredientes = Entry(interfaz, width = 30, borderwidth = 2, fg = "black", font = ("ArialBlack", 14))
entradaIngredientes.grid(row = 6, column = 2, columnspan = 2)

#Listado Datos

datos = ttk.Treeview(interfaz, columns = (1,2,3,4,5,6), show = "headings", height = "16")
datos.grid(row = 11, column = 0, rowspan = 16, columnspan = 6)

datos.heading(1, text = "ID", anchor = "center")
datos.heading(2, text = "Nombre", anchor = "center")
datos.heading(3, text = "Apellidos", anchor = "center")
datos.heading(4, text = "Teléfono", anchor = "center")
datos.heading(5, text = "Tamaño", anchor = "center")
datos.heading(6, text = "Ingredientes", anchor = "center")

datos.column("#1", anchor = "w", width = 270, stretch = True)
datos.column("#2", anchor = "w", width = 185, stretch = False)
datos.column("#3", anchor = "w", width = 185, stretch = False)
datos.column("#4", anchor = "w", width = 185, stretch = False)
datos.column("#5", anchor = "w", width = 185, stretch = False)
datos.column("#6", anchor = "w", width = 190, stretch = False)

#Ingreso de datos
#Cargar información

def cargarArchivoJson ():
    global listaDatos
    with open("listadoClientes.json", "r") as file_handler:
        listaDatos = json.load(file_handler)
    file_handler.close
    print("El archivo se ha leído y cerrado")

def actualizarArchivoJson():
    global listaDatos
    with open("listaClientes.json", "w") as file_handler:
        json.dump(listaDatos, file_handler, indent = 6)
    file_handler.close 
    print("El archivo se ha actualizado y cerrado")

def eliminarDatosLista():
    for dato in datos.get_children():
        datos.delete(dato)

def cargarDatosJson():
    global listaDatos
    eliminarDatosLista()
    indexFila = 1
    for key in listaDatos:
        id = key["id"]
        Nombre = key["Nombre"]
        Apellidos = key["Apellidos"]
        Telefono = key["Teléfono"]
        Tamaño = key["Tamaño"]
        Ingredientes = key["Ingredientes"]
        datos.insert('', index = "end", iid = indexFila, text = '', values = (id, Nombre, Apellidos, Telefono, Tamaño, Ingredientes))
        indexFila = indexFila + 1

def limpiarCliente():
    entradaNombre.delete(0, END)
    entradaApellidos.delete(0, END)
    entradaTelefono.delete(0, END)
    entradaTamaño.delete(0, END)
    entradaIngredientes.delete(0, END)
    entradaID.configure(text = "")
    entradaNombre.focus_set()
    crearID.set(codigos.uuid4())
    cambiarColorCeldas("#FFFFFF")

def filaListaDatos(id):
    global listaDatos
    fila = 0
    valido = False
    for cliente in listaDatos:
        if cliente["ID"] == id:
            valido = True
            break
        fila = fila +1
    
    if (valido == True):
        return (fila)
    return (-1)

def cambiarColorCeldas(color_nuevo):
    entradaNombre.config(bg = color_nuevo)
    entradaApellidos.config(bg = color_nuevo)
    entradaTelefono.config(bg = color_nuevo)
    entradaTamaño.config(bg = color_nuevo)
    entradaIngredientes.config(bg = color_nuevo)

def cambiarEstadoActivo(estado):
    if estado == "Edit":
        botonActualizar["state"] = "normal"
        botonEliminar["state"] = "normal"
        botonAñadir ["state"] = "disabled"
    elif estado == "Cancel":
        botonActualizar["state"] = "disabled"
        botonEliminar["state"] = "disabled"
        botonAñadir ["state"] = "disabled"
    else:
        botonActualizar["state"] = "disabled"
        botonEliminar["state"] = "disabled"
        botonAñadir ["state"] = "normal"

def cargarDatosFila(_tuple):
    if len(_tuple == 0):
        return;
    
    crearID.set(_tuple[0]);
    entradaNombre.delete(0,END)
    entradaNombre.insert(0,_tuple[1])
    entradaApellidos.delete(0,END)
    entradaApellidos.insert(0,_tuple[2])
    entradaTelefono.delete(0,END)
    entradaTelefono.insert(0,_tuple[3])
    entradaTamaño.delete(0,END)
    entradaTamaño.insert(0,_tuple[4])
    entradaIngredientes.delete(0,END)
    entradaIngredientes.insert(0,_tuple[5])

def Cancelar():
    limpiarCliente()
    cambiarEstadoActivo("New")

def imprimirEntradasCliente():
    global listaDatos
    for entrada in listaDatos:
        print(entrada)
    
    entradaNombre.focus_set()

def agregarCliente():
    id = crearID.get()
    Nombre = entradaNombre.get()
    Apellidos = entradaApellidos.get()
    Telefono = entradaTelefono.get()
    Tamaño = entradaTamaño.get()
    Ingredientes = entradaIngredientes.get()

    if len(Nombre == 0):
        cambiarColorCeldas("#FFB2AE")
        return
    seleccionOperacion("Agregar", id, Nombre, Apellidos, Telefono, Tamaño, Ingredientes)


def actualizarCliente():
    id = crearID.get()
    Nombre = entradaNombre.get()
    Apellidos = entradaApellidos.get()
    Telefono = entradaTelefono.get()
    Tamaño = entradaTamaño.get()
    Ingredientes = entradaIngredientes.get()

    if len(Nombre == 0):
        cambiarColorCeldas("#FFB2AE")
        return
    seleccionOperacion("Actualizar", id, Nombre, Apellidos, Telefono, Tamaño, Ingredientes)

def eliminarCliente():
    id = crearID.get()
    seleccionOperacion("Eliminar", id, None, None, None, None, None)

def seleccionOperacion(comando, id, Nombre, Apellidos, Telefono, Tamaño, Ingredientes):
    global listaDatos

    if (comando == "Actualizar"):
        fila = filaListaDatos(id)
        if (fila >= 0):
            cliente = {"ID": id, "Nombre": Nombre, "Apellidos": Apellidos, "Teléfono": Telefono, "Tamaño": Tamaño, "Ingredientes": Ingredientes}
            listaDatos[fila] = cliente
    elif (comando == "Añadir"):
            cliente = {"ID": id, "Nombre": Nombre, "Apellidos": Apellidos, "Teléfono": Telefono, "Tamaño": Tamaño, "Ingredientes": Ingredientes}
            listaDatos.append(cliente)
    elif (comando == "Eliminar"):
        fila = filaListaDatos(id)
        if (fila >= 0):
            del listaDatos[fila];

    actualizarArchivoJson();
    cargarDatosJson();
    limpiarCliente();

def mostrarSeleccionActual(event):
    global posicionActual
    posicionActual = datos.selection()[0]
    ultimoCliente = (datos.item(posicionActual, "values"))
    cargarDatosFila(ultimoCliente)
    cambiarEstadoActivo("Edit")

datos.bind("<ButtonRelease>", mostrarSeleccionActual)

espacioBotonesOperaciones = LabelFrame(interfaz, text = "", bg = "PaleTurquoise4", font = ("ArialBlack", 14))
botonMostrarenTerminal = Button(espacioBotonesOperaciones, text = "Mostrar", padx = 20, pady = 10, command = imprimirEntradasCliente)
botonAñadir = Button(espacioBotonesOperaciones, text = "Añadir", padx = 20, pady = 10, command = agregarCliente)
botonActualizar = Button(espacioBotonesOperaciones, text = "Actualizar", padx = 20, pady = 10, command = actualizarCliente)
botonEliminar = Button(espacioBotonesOperaciones, text = "Eliminar", padx = 20, pady = 10, command = eliminarCliente)
botonSalir = Button(espacioBotonesOperaciones, text = "Salir", padx = 20, pady = 10, command = interfaz.quit)
botonSalir.pack(side = LEFT)

cargarArchivoJson()
cargarDatosJson()

interfaz.mainloop()