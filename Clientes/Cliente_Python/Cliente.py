import FinanzaLibrary

def ingresarPersona():
    np = raw_input("Nombre de la persona:")
    fch = raw_input("Fecha movimiento:")
    saldo = raw_input("Saldo:")
    data = { 'nombrePersona': np,
  			'fchMovimiento': fch,
  			'saldoMovimiento': saldo }
    FinanzaLibrary.consumePost(data)

def editarPersona():
    id = raw_input("Identificador:")
    nomPer = raw_input("Nombre de la persona:")
    fchMov = raw_input("Fecha movimiento:")
    saldoMov = raw_input("Saldo:")
    data = { 'id' : id,
			'nombrePersona': nomPer,
  			'fchMovimiento': fchMov,
  			'saldoMovimiento': saldoMov
    }
    FinanzaLibrary.consumePut(data)

def eliminarPersona():
    id = raw_input("Identificador:")
    data = { 'id' : id }
    FinanzaLibrary.consumeDelete(data)

def listarPersonas():
    FinanzaLibrary.consumeGet()

def main():
    optExit = True
    while optExit:
        try:
            print("Elija una opcion \n")
            print("1.Listar personas de Finanzas \n")
            print("2.Ingresar Persona \n")
            print("3.Editar Persona \n")
            print("4.Eliminar persona \n")
            print("5.Salir \n")

            opt = int(input("Opcion:"))            
            print(opt)

            if opt == 1:
                listarPersonas()
            if opt == 2:
                ingresarPersona()
            if opt == 3:
                editarPersona()
            if opt == 4:
                eliminarPersona()
            if opt == 5:
                optExit = False          
        except:
            print ("\n Ha ocurrido un error, favor intentar nuevamente. Si el problema persiste, llame al administrador")

if __name__=="__main__":main()


