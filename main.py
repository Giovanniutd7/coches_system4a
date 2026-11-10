from tkinter import *
from tkinter import messagebox
from coches import coches
from estudiantes_system.estudiantes.estudiante import Estudiantes
from mysql.connector import Error

class App:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Sistema de Gestion")
        self.ventana.geometry("500x550")
        self.main()

    def borrarPantalla(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

    def respuesta_sql(self, respuesta):
        if respuesta:
            messagebox.showinfo("Aviso", "Accion Realizada con Exito")
        else:
            messagebox.showerror("Aviso", "Esta Accion no pudo realizarse")

    def insertar_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="Ingresar datos del coche").pack(pady=5)
        
        Label(self.ventana, text="Marca").pack()
        self.marca = Entry(self.ventana)
        self.marca.pack()

        Label(self.ventana, text="Color").pack()
        self.color = Entry(self.ventana)
        self.color.pack()

        Label(self.ventana, text="Modelo").pack()
        self.modelo = Entry(self.ventana)
        self.modelo.pack()

        Label(self.ventana, text="Velocidad").pack()
        self.velocidad = Entry(self.ventana)
        self.velocidad.pack()

        Label(self.ventana, text="Potencia").pack()
        self.potencia = Entry(self.ventana)
        self.potencia.pack()

        Label(self.ventana, text="Asientos").pack()
        self.asientos = Entry(self.ventana)
        self.asientos.pack()

        Button(self.ventana, text="Guardar", command=self.guardar_coche).pack(pady=5)
        Button(self.ventana, text="Regresar", command=self.menu_acciones).pack(pady=5)

    def guardar_coche(self):
        try:
            marca = self.marca.get().strip()
            color = self.color.get().strip()
            modelo = self.modelo.get().strip()
            velocidad = int(self.velocidad.get().strip())
            potencia = int(self.potencia.get().strip())
            asientos = int(self.asientos.get().strip())

            coche = coches.Coches(marca, color, modelo, velocidad, potencia, asientos)
            respuesta = coche.insertar()
            self.respuesta_sql(respuesta)
            del coche
            self.menu_acciones()
        except ValueError:
            messagebox.showerror("Error", "Datos invalidos")

    def eliminar_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="Ingresar el ID del coche a borrar").pack(pady=5)
        
        Label(self.ventana, text="ID").pack()
        self.id_eliminar = Entry(self.ventana)
        self.id_eliminar.pack()

        Button(self.ventana, text="Eliminar", command=self.procesar_eliminacion).pack(pady=5)
        Button(self.ventana, text="Regresar", command=self.menu_acciones).pack(pady=5)

    def procesar_eliminacion(self):
        try:
            id_coche = int(self.id_eliminar.get().strip())
            respuesta = coches.Coches.eliminar(id_coche)
            self.respuesta_sql(respuesta)
            self.menu_acciones()
        except ValueError:
            messagebox.showerror("Error", "ID invalido")

    def fijar_id_modificacion(self, event=None):
        try:
            int(self.id_modificar.get().strip())
        except ValueError:
            return
        self.id_modificar.configure(state=DISABLED)

    def modificar_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="Ingresar ID y datos nuevos").pack(pady=5)

        Label(self.ventana, text="ID del Coche").pack()
        self.id_modificar = Entry(self.ventana)
        self.id_modificar.pack()
        self.id_modificar.bind("<FocusOut>", self.fijar_id_modificacion)
        self.id_modificar.bind("<Return>", self.fijar_id_modificacion)

        Label(self.ventana, text="Marca").pack()
        self.marca = Entry(self.ventana)
        self.marca.pack()

        Label(self.ventana, text="Color").pack()
        self.color = Entry(self.ventana)
        self.color.pack()

        Label(self.ventana, text="Modelo").pack()
        self.modelo = Entry(self.ventana)
        self.modelo.pack()

        Label(self.ventana, text="Velocidad").pack()
        self.velocidad = Entry(self.ventana)
        self.velocidad.pack()

        Label(self.ventana, text="Potencia").pack()
        self.potencia = Entry(self.ventana)
        self.potencia.pack()

        Label(self.ventana, text="Asientos").pack()
        self.asientos = Entry(self.ventana)
        self.asientos.pack()

        Button(self.ventana, text="Actualizar", command=self.procesar_modificacion).pack(pady=5)
        Button(self.ventana, text="Regresar", command=self.menu_acciones).pack(pady=5)

    def procesar_modificacion(self):
        try:
            id_coche = int(self.id_modificar.get().strip())
            marca = self.marca.get().strip()
            color = self.color.get().strip()
            modelo = self.modelo.get().strip()
            velocidad = int(self.velocidad.get().strip())
            potencia = int(self.potencia.get().strip())
            asientos = int(self.asientos.get().strip())

            coche = coches.Coches(marca, color, modelo, velocidad, potencia, asientos)
            respuesta = coche.actualizar(id_coche)
            self.respuesta_sql(respuesta)
            del coche
            self.menu_acciones()
        except ValueError:
            messagebox.showerror("Error", "Datos invalidos")

    def consultar_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="Listado de Coches").pack(pady=5)

        texto = Text(self.ventana, width=55, height=18)
        texto.pack(pady=5)

        registros = coches.Coches.consultar()
        if registros and len(registros) > 0:
            for fila in registros:
                linea = f"ID: {fila[0]} | Marca: {fila[1]} | Color: {fila[2]} | Modelo: {fila[3]} | Vel: {fila[4]} | Pot: {fila[5]} | Asientos: {fila[6]}\n"
                texto.insert(END, linea)
        else:
            texto.insert(END, "No existen datos que mostrar.")

        texto.config(state=DISABLED)
        Button(self.ventana, text="Regresar", command=self.menu_acciones).pack(pady=5)

    def insertar_estudiante_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="Ingresar datos del estudiante").pack(pady=5)

        Label(self.ventana, text="Nombre").pack()
        self.nombre = Entry(self.ventana)
        self.nombre.pack()

        Label(self.ventana, text="Nota").pack()
        self.nota = Entry(self.ventana)
        self.nota.pack()

        Button(self.ventana, text="Guardar", command=self.guardar_estudiante).pack(pady=5)
        Button(self.ventana, text="Regresar", command=self.menu_estudiantes).pack(pady=5)

    def guardar_estudiante(self):
        nombre = self.nombre.get().strip()
        nota = self.nota.get().strip()
        if not nombre or not nota:
            messagebox.showerror("Error", "Nombre y nota son obligatorios")
            return

        try:
            respuesta = Estudiantes(nombre, nota).insertar()
            self.respuesta_sql(respuesta)
            self.menu_estudiantes()
        except Error as error:
            messagebox.showerror("Error", f"No se pudo guardar el estudiante: {error}")

    def eliminar_estudiante_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="Ingresar el ID del estudiante a borrar").pack(pady=5)

        Label(self.ventana, text="ID").pack()
        self.id_eliminar = Entry(self.ventana)
        self.id_eliminar.pack()

        Button(self.ventana, text="Eliminar", command=self.procesar_eliminacion_estudiante).pack(pady=5)
        Button(self.ventana, text="Regresar", command=self.menu_estudiantes).pack(pady=5)

    def procesar_eliminacion_estudiante(self):
        try:
            id_estudiante = int(self.id_eliminar.get().strip())
            respuesta = Estudiantes.eliminar(id_estudiante)
            self.respuesta_sql(respuesta)
            self.menu_estudiantes()
        except ValueError:
            messagebox.showerror("Error", "ID invalido")
        except Error as error:
            messagebox.showerror("Error", f"No se pudo eliminar el estudiante: {error}")

    def modificar_estudiante_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="Ingresar ID y datos nuevos").pack(pady=5)

        Label(self.ventana, text="ID del estudiante").pack()
        self.id_modificar = Entry(self.ventana)
        self.id_modificar.pack()
        self.id_modificar.bind("<FocusOut>", self.fijar_id_modificacion)
        self.id_modificar.bind("<Return>", self.fijar_id_modificacion)

        Label(self.ventana, text="Nombre").pack()
        self.nombre = Entry(self.ventana)
        self.nombre.pack()

        Label(self.ventana, text="Nota").pack()
        self.nota = Entry(self.ventana)
        self.nota.pack()

        Button(self.ventana, text="Actualizar", command=self.procesar_modificacion_estudiante).pack(pady=5)
        Button(self.ventana, text="Regresar", command=self.menu_estudiantes).pack(pady=5)

    def procesar_modificacion_estudiante(self):
        try:
            id_estudiante = int(self.id_modificar.get().strip())
            nombre = self.nombre.get().strip()
            nota = self.nota.get().strip()
            if not nombre or not nota:
                messagebox.showerror("Error", "Nombre y nota son obligatorios")
                return

            respuesta = Estudiantes(nombre, nota).actualizar(id_estudiante)
            self.respuesta_sql(respuesta)
            self.menu_estudiantes()
        except ValueError:
            messagebox.showerror("Error", "ID invalido")
        except Error as error:
            messagebox.showerror("Error", f"No se pudo actualizar el estudiante: {error}")

    def consultar_estudiantes_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="Listado de Estudiantes").pack(pady=5)

        texto = Text(self.ventana, width=55, height=18)
        texto.pack(pady=5)

        try:
            registros = Estudiantes.consultar()
            if registros:
                for fila in registros:
                    texto.insert(END, f"ID: {fila[0]} | Nombre: {fila[1]} | Nota: {fila[2]}\n")
            else:
                texto.insert(END, "No existen datos que mostrar.")
        except Error as error:
            texto.insert(END, f"No se pudo consultar la base de datos: {error}")

        texto.config(state=DISABLED)
        Button(self.ventana, text="Regresar", command=self.menu_estudiantes).pack(pady=5)

    def menu_acciones(self):
        self.borrarPantalla()
        Label(self.ventana, text="Menu de Coches").pack(pady=10)
        Button(self.ventana, text="1.- Agregar", command=self.insertar_view).pack(pady=2)
        Button(self.ventana, text="2.- Borrar", command=self.eliminar_view).pack(pady=2)
        Button(self.ventana, text="3.- Modificar", command=self.modificar_view).pack(pady=2)
        Button(self.ventana, text="4.- Mostrar", command=self.consultar_view).pack(pady=2)
        Button(self.ventana, text="5.- Salir", command=self.main).pack(pady=2)

    def menu_estudiantes(self):
        self.borrarPantalla()
        Label(self.ventana, text="Menu de Estudiantes").pack(pady=10)
        Button(self.ventana, text="1.- Agregar", command=self.insertar_estudiante_view).pack(pady=2)
        Button(self.ventana, text="2.- Borrar", command=self.eliminar_estudiante_view).pack(pady=2)
        Button(self.ventana, text="3.- Modificar", command=self.modificar_estudiante_view).pack(pady=2)
        Button(self.ventana, text="4.- Mostrar", command=self.consultar_estudiantes_view).pack(pady=2)
        Button(self.ventana, text="5.- Regresar", command=self.main).pack(pady=2)

    def main(self):
        self.borrarPantalla()
        Label(self.ventana, text="MENU PRINCIPAL").pack(pady=20)
        Button(self.ventana, text="1.- Coches", command=self.menu_acciones).pack(pady=5)
        Button(self.ventana, text="2.- Estudiantes", command=self.menu_estudiantes).pack(pady=5)
        Button(self.ventana, text="3.- Salir", command=self.ventana.quit).pack(pady=5)

if __name__ == "__main__":
    ventana = Tk()
    app = App(ventana)
    ventana.mainloop()


    