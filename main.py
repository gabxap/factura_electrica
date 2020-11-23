from tkinter import *
import psutil
from time import sleep


ventana = Tk()
ventana.title('By Gabxap')
ventana.geometry("600x300")
# costo por segundo

costo_soles = 0.0000201389
segundos_enchufado = 0
recibo_mostrado = False
enchufado = psutil.sensors_battery().power_plugged
estado = StringVar()
estado.set("Estado: Enchufado a la red eléctrica")


def checkearEstado():
    global segundos_enchufado
    global recibo_mostrado
    enchufado = psutil.sensors_battery().power_plugged
    if enchufado:
        segundos_enchufado += 1
        recibo_mostrado = False
        estado.set("Estado: Enchufado a la red eléctrica")
        texto_estado.config(
            fg="green",
            justify="center",
            font=("Arial", 30)
        )

    else:
        
        minutos = (int)(segundos_enchufado/60)
        segundos = (int)(segundos_enchufado % 60)
        total_pagar = segundos_enchufado * costo_soles
        estado.set("Estado: Desenchufado de la red eléctrica")
        texto_estado.config(
            fg="red",
            justify="center",
            font=("Arial", 30)
        )
        if recibo_mostrado == False:
            nuevaVentana = Toplevel(ventana)
            nuevaVentana.geometry("400x400")
            texto = Label(nuevaVentana, text="Factura")
            texto.config(
                fg="black",
                padx=50,
                pady=10,
                font=("Arial", 30, UNDERLINE, 'bold')
            )
            texto.pack()
            texto = Label(nuevaVentana, text="Tiempo consumido: " +
                          str(minutos) + " min " + str(segundos) + " seg")
            texto.config(
                fg="black",
                padx=50,
                pady=10,
                font=("Arial", 20)
            )
            texto.pack()
            texto = Label(nuevaVentana, text="Total a pagar: " +
                          str(total_pagar) + " soles")
            texto.config(
                fg="black",
                padx=50,
                pady=10,
                font=("Arial", 20)
            )
            texto.pack()
            texto = Label(nuevaVentana, text="Bajo estas perspectivas")
            texto.config(
                fg="black",
                padx=50,
                pady=10,
                font=("Arial", 20, 'bold')
            )
            texto.pack()
            texto = Label(nuevaVentana, text="x minuto: 0.001208334 soles")
            texto.config(
                pady=5,
                fg="black",
                font=("Arial", 15)
            )
            texto.pack()

            texto = Label(nuevaVentana, text="x hora: 0.07250004 soles")
            texto.config(
                pady=5,
                fg="black",
                font=("Arial", 15)
            )
            texto.pack()
            texto = Label(nuevaVentana, text="x día: 1.74000096 soles")
            texto.config(
                pady=5,
                fg="black",
                font=("Arial", 15)
            )
            texto.pack()

            texto = Label(nuevaVentana, text="x mes: 52.2000288 soles")
            texto.config(
                pady=5,
                fg="black",
                font=("Arial", 15)
            )
            texto.pack()
            recibo_mostrado = True

    ventana.after(1000, checkearEstado)


texto = Label(ventana, text="Factura de laptop al cargar")
texto.config(
    fg="white",
    bg="black",
    padx=130,
    pady=20,
    font=("Arial", 40)
)
texto.pack(side=TOP)

texto = Label(
    ventana, text="Explicación: Un aparato que usamos a diario siempre es nuestra laptop o PC. Este programa te permite saber cuanto tiempo está esta enchufada a la red eléctrica y en cúanto este tiempo se traduce en soles.")
texto.config(
    padx=130,
    pady=20,
    wraplength=600,
    justify="left",
    font=("Arial", 18)
)
texto.pack()

texto_estado = Label(ventana, textvariable=estado)
texto_estado.config(
    fg="green",
    justify="center",
    font=("Arial", 30)
)
texto_estado.pack()


ventana.after(1000, checkearEstado)
ventana.mainloop()
