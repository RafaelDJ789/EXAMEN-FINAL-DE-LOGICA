#Logica de sistemas
#Primer semestre 
# Rafael de Jesús Sandoval González
# 0907-19-14119
from tkinter import ttk
from tkinter import *

class Desk:
    def __init__(self, window):
        # Initializations
        
        #ancho
        ancho = 800
        
        #alto
        alto = 600
        
        # asignamos la ventana a una variable de la clase llamada wind
        self.wind = window

        #le asignamos el ancho y el alto a la ventana con la propiedad geometry
        self.wind.geometry(str(ancho)+'x'+str(alto))

        #centramos el contenido 
        self.wind.columnconfigure(0, weight=1)
        
        #le damos un titulo a la ventana
        self.wind.title('Aplicación con interface gráfica en Python - By Ing. Gerson Altamirano')
        
        # creamos un contenedor
        frame = LabelFrame(self.wind, text = 'Sumar 2 valores')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)
        
        # creamos un etiqueta
        Label(frame, text = 'primer numero: ').grid(row = 1, column = 0)
        
        #creamos un input donde ingresar valores
        self.var1 = Entry(frame)
        self.var1.focus()
        self.var1.grid(row = 1, column = 1)
        
        # igual que arriba una etiqueta y un campo input para ingresar valores
        Label(frame, text = 'segundo numero: ').grid(row = 2, column = 0)
        self.var2 = Entry(frame)
        self.var2.grid(row = 2, column = 1)

        Label(frame, text = 'Tercer numero: ').grid(row = 3, column = 0)
        self.var3 = Entry(frame)
        self.var3.grid(row = 3, column = 1)
        
        #Creamos un boton para ejecutar la suma
        Button(frame, text = 'Boton A', command = self.sumar).grid(row = 4, columnspan = 2, sticky = W + E)
        Button(frame, text = 'Boton B', command = self.sumar).grid(row = 5, columnspan = 2, sticky = W + E)
        #designamos un área para mensajes
        self.message = Label(text = '', fg = 'red')
        self.message.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)
        
    # creamos una función para validar que los campos no esten en blanco
    def validation(self):
        return len(self.var1.get()) != 0 and len(self.var2.get()) != 0
         
        
    
    # esta es la función que ejecuta la suma
    def sumar(self):
        if self.validation():
            if(int(self.var1.get()) > int(self.var3.get())):
                resultado = float( self.var1.get() ) * float( self.var2.get() )
                resultado2= float (resultado) *  float( self.var3.get())
                self.message['text'] = 'Se ejecuto una multiplicacion y el resultado es : {}'.format(resultado2)
            if(int(self.var1.get()) == int(self.var2.get()) == int(self.var3.get()):
                resultado = float( self.var1.get() ) + float( self.var2.get() + float( self.var3.get() )
                resultado2= float (resultado) *  float( self.var3.get())
                self.message['text'] = 'Se ejecuto una suma y el resultado es : {}'.format(resultado2)

        else:
            self.message['text'] = 'los campos son requeridos'

#validamos si estamos en la aplicación inicial
if __name__ == '__main__':
    
    #asignamos la propiedad de tkinter a la variable window
    window = Tk()
    
    #en la variable app guardamos la clase Desk y le enviamos como parametro la ventana 
    app = Desk(window)

    #ejecutamos un mainloop para que se ejecute la ventana
    window.mainloop()