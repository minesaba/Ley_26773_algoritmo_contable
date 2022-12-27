from tkinter import *
from tkinter import messagebox

#LÓGICA y FUNCIONES

def calcular():
  resultado.set(format(float(53 * ingreso.get() * (porcentaje.get()/100) * (65/edad.get())), '.2f'))
  
def limpiar():
  edad.set("")
  ingreso.set("")
  porcentaje.set("")

def borrar():
  resp = messagebox.askquestion("¿BORRAR?","¿Desea eliminar el registro?")
  if resp == 'yes':
    limpiar()

# Salir del programa
def salir():
  resp = messagebox.askquestion("CONFIRME", "¿Desea salir del programa?")
  if resp == 'yes':   
    raiz.destroy()

# Información adicional

def mostrar_uso():
  msg = '''Calcula los siniestros que caen bajo la órbita de la Ley 26773 en la República Argentina, es decir, aquellos que ocurrieron entre el 26/10/2012 y el 23/01/2017, inclusive.'''
  messagebox.showinfo("¿QUÉ SINIESTROS CALCULA ESTE ALGORITMO?", msg)

def mostrar_infoadicional():
  msg = '''Ley 26773. Régimen de ordenamiento de la reparación de los daños derivados de los accidentes de trabajo y enfermedades profesionales.
República Argentina. Jurisdicción nacional.
Sancionada: Octubre 24 de 2012.
Promulgada: Octubre 25 de 2012.
Publicada en el Boletín Oficial del 26 Octubre 2012 (Número: 32509).'''
  messagebox.showinfo("INFORMACIÓN ADICIONAL.", msg)

def mostrar_acercade():
  messagebox.showinfo("¿QUIÉN SOY?", "Creado por María Inés\nDiciembre, 2022\nFinalidad: práctica en programación y en análisis funcional.")

# INTERFAZ GRÁFICA

# Espaciados
esp_x = 10
esp_y = 10
# Colores para el framecampos
framecampos_color_fondo = 'cyan'
framecampos_color_letra = 'black'
# Colores para el framebotones
framebotones_color_fondo = 'plum'
framebotones_color_boton = 'black'
framebotones_color_texto_boton = framebotones_color_fondo

# Raíz
raiz = Tk()
raiz.title('Riesgos del Trabajo - Ley 26773.')

# Barra de menú
barramenu = Menu(raiz)
raiz.config(menu=barramenu)

borramenu = Menu(barramenu, tearoff=0)
borramenu.add_command(label = 'Limpiar formulario')

ayudamenu = Menu(barramenu, tearoff=0)
ayudamenu.add_command(label='Normativa aplicable', command = mostrar_uso)
ayudamenu.add_command(label='Información adicional', command =mostrar_infoadicional)

ayudamenu1 = Menu(barramenu, tearoff=0)
ayudamenu1.add_command(label='Creado por', command =mostrar_acercade)

barramenu.add_cascade(label='¿Qué podés calcular?', menu=ayudamenu)
barramenu.add_cascade(label='Acerca de...', menu=ayudamenu1)

# Frame para campos
framecampos = Frame(raiz)
framecampos.config(bg=framecampos_color_fondo)
framecampos.pack(fill='both')

# Configuración y colores
def configurar_label(mi_label, fila):
    espaciado_labels = {'column':0, 'sticky': 'e', 'padx':esp_x, 'pady':esp_y}
    colores_label = {'bg':framecampos_color_fondo, 'fg': framecampos_color_letra} #bg: background , fg: foreground
    mi_label.grid(row=fila, **espaciado_labels)
    mi_label.config(**colores_label)
    
# Labels
edad_label = Label(framecampos, text='Edad')
edad_label.grid(row=0, column=0, sticky='e', padx=10, pady=10)

ingreso_label = Label(framecampos, text='Ingreso base')
ingreso_label.grid(row=1, column=0, sticky='e', padx=10, pady=10)

porcentaje_label = Label(framecampos, text='Porcentaje de incapacidad')
porcentaje_label.grid(row=2, column=0, sticky='e', padx=10, pady=10)

resultado_label = Label(framecampos, text='Resultado')
resultado_label.grid(row=3, column=0, sticky='e', padx=10, pady=10)

# Campos de entrada
edad = IntVar()
ingreso = DoubleVar()
porcentaje = DoubleVar()
resultado = DoubleVar()

edad_input = Entry(framecampos, textvariable=edad)
edad_input.grid(row=0, column=1, padx=10, pady=10)

ingreso_input = Entry(framecampos, textvariable=ingreso)
ingreso_input.grid(row=1, column=1, padx=10, pady=10)

porcentaje_input = Entry(framecampos, textvariable=porcentaje)
porcentaje_input.grid(row=2, column=1, padx=10, pady=10)

resultado_output = Entry(framecampos, textvariable=resultado, state=DISABLED)
resultado_output.grid(row=3, column=1, sticky='e', padx=10, pady=10)

# Frame para los botones
framebotones = Frame(raiz)
framebotones.pack()

boton_calcular = Button(framebotones, text='Calcular', command = calcular, width=9)
boton_calcular.config(bg=framebotones_color_boton, fg=framebotones_color_texto_boton)
boton_calcular.grid(row=0, column=2, padx=10, pady=10)

boton_borrar = Button(framebotones, text='Borrar', command = borrar, width=9)
boton_borrar.config(bg=framebotones_color_boton, fg=framebotones_color_texto_boton)
boton_borrar.grid(row=0, column=3, padx=10, pady=10)

# Frame del pie
framecopy = Frame(raiz)
framecopy.config(bg='black')
framecopy.pack(fill='both')

copy_label = Label(framecopy, text='María Inés A., 2022.')
copy_label.grid(column=0, padx=10, pady=10)

# Línea final
raiz.mainloop()
