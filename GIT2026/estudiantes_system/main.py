try:
    from .estudiantes import estudiante
except ImportError:
    from estudiantes import estudiante

class App:
    def __init__(self):
        self.main()

    def borrarPantalla(self):
        print("\033c")
        
    def esperarTecla(self):
        input("...¡Oprima cualquier tecla para contunuar!...")
    def terminarSistema(self):
        input("....:::: GRACIAS POR UTILIZAR NUESTRO SISTEMA, \n  vuelve pronto ::::...")
    def opcionInvalida(self):
        input("\n\t.... ¡Opcion invalidad, vuelve a intentarlo!.... ") 
        
    def menu_acciones(self,tipo):
        print(f"\t\t....:::: Menu de {tipo} ::::...\n")
        opcion=input("\n\t1.- Agregar\n\t2.- Borrar\n\t3.- Modificar\n\t4.- Mostrar\n\t5.- Regresar\n\t\tEscribe una opción: ").strip()
        return opcion
    
    def respuesta_sql(self,respuesta):
        if respuesta:
            input("...¡Accion Realizada con Exito!...")
        else:
            input("...¡Esta Accion no pudo realizarse en este momento !...")

    def menu_estudiante(self):
        opc =True
        while opc:
            self.borrarPantalla()
            opc=self.menu_acciones("Estudiantes")
            match opc:
                case "1":
                    ##solicitar datos y crear objeto de Coches
                    estudiantito= self.datos_estudiante("Estudiante")
                    estudiante1= estudiante.Estudiantes(estudiantito['nombre'],estudiantito['nota'])
                    
                    respuesta= estudiante1.insertar()
                    self.respuesta_sql(respuesta)
                    ##borrar objeto que no utilizas
                    del estudiante1
                case "2":
                    self.borrarPantalla()
                    id =input("Ingrese el ID del estudiante a eliminar: ").strip()
                    respuesta=estudiante.Estudiantes.eliminar(id)
                    self.respuesta_sql(respuesta)
                case "3":
                    self.borrarPantalla()
                    id= input("Ingrese el ID del estudiante a eliminar: ").strip()
                    estudiantito=self.datos_estudiante(id)
                    estudiante1=estudiante.Estudiantes(
                        estudiantito['nombre'],
                        estudiantito['nota'],
                    )
                    respuesta=estudiante1.actualizar(id)
                    self.respuesta_sql(respuesta)
                    del estudiante1
                case "4":
                    self.borrarPantalla()

                    registros=estudiante.Estudiantes.consultar()
                    
                    num_estudiante=1
                    if len(registros)>0:
                        for fila in registros:
                            print(f"\n\testudiante numero #: {num_estudiante}\n\t\tID: {fila[0]},\n\t\tNombre: {fila[1]}\n\t\tNota: {fila[2]}")
                            num_estudiante+=1
                            self.esperarTecla()
                    else:
                        print("...!No se encontraro informacion en la BD")
                        self.esperarTecla()

                case "5":
                    opc=False
                case _:
                    self.opcionInvalida()

              
    def datos_estudiante(self,tipo):
        self.borrarPantalla()
        print(f"\n\tIngresar los datos del {tipo}")
        estudiantito={}
        estudiantito['nombre']=input("Nombre: ").upper().strip()
        estudiantito['nota']=input("Nota: ").upper().strip()
        return estudiantito
    def main(self):
        opcion=True
        while opcion:
            self.borrarPantalla()
            opcion=input("\n\t\t ::: MENU PRINCIPAL :::\n\t1- Estudiante\n\t2- Salir\n\tElige una opcion: ").lower().strip()
            match opcion:
                case "1":
                    self.borrarPantalla()
                    self.menu_estudiante()

                case "2":
                    self.borrarPantalla()
                    self.terminarSistema()
                    opcion=False
                case _:
                    self.opcionInvalida()    
if __name__=="__main__":
    app=App()
    