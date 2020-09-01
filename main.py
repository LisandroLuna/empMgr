from pip._vendor.distlib.compat import raw_input
from os import system, name
from employee import *
from position import *
from sector import *
from seniority import *


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def main():
    run = True
    while run:
        print('-Administrador de Personal-\nElija la opcion deseada:')
        opte = int(input('\r1- Agregar Empleado\n\r2- Ver Datos de Empleado\n\r3- Actualizar datos de empleados\n\r4- Borrar Empleado\n\r5- Salir\n'))
        clear()
        if opte == 1:
            try:
                print('-Crear Empleado-')
                empnam = input('Ingrese Nombre: ')
                emplas = input('Ingrese Apellido: ')
                prepos = input('Ingrese Posicion: ')
                try:
                    emppos = Position.objects.getid(name=prepos)
                except:
                    print('Posicion no valida!\n')
                    try:
                        prepos = input('Ingrese Posicion: ')
                        emppos = Position.objects.getid(name=prepos)
                    except:
                        print('Posicion no valida, se tomara la posicion por defecto.\nPuede cambiarla desde el menu editar\n')
                        input("Presiona Enter para continuar...")
                        emppos = 1
                presec = input('Ingrese Sector: ')
                try:
                    empsec = Sector.objects.getid(name=presec)
                except:
                    print('Sector no valido!\n')
                    try:
                        presec = input('Ingrese Sector: ')
                        empsec = Sector.objects.getid(name=presec)
                    except:
                        print('Sector no valid0, se tomara el Sector por defecto.\nPuede cambiarlo desde el menu editar\n')
                        input("Presiona Enter para continuar...")
                        empsec = 1
                presen = input('Ingrese Seniority: ')
                try:
                    empsen = Seniority.objects.getid(name=presen)
                except:
                    print('Seniority no valido!\n')
                    try:
                        presen = input('Ingrese Seniority: ')
                        empsen = Seniority.objects.getid(name=presen)
                    except:
                        print('Seniority no valido, se tomara el Seniority por defecto.\nPuede cambiarlo desde el menu editar\n')
                        input("Presiona Enter para continuar...")
                        empsen = 1
                empsal = int(input('Ingrese Sueldo: $'))
                try:
                    empl = Employee(name=empnam,
                                   lastname=emplas,
                                   position=emppos,
                                   sector=empsec,
                                   seniority=empsen,
                                   salary=empsal
                                   )
                except Exception as e:
                    print(e)
                try:
                    empl = Employee.objects.save(empl)
                except Exception as e:
                    print(e)
            except Exception as e:
                print(e)
            print('Se guardo empleado!\n')
            input("Presiona Enter para continuar...")
            clear()
        if opte == 2:
            try:
                print('-Ver Empleado-')
                emplid = int(input('Ingrese numero de legajo: '))
                empl = Employee.objects.get(emplid)
                print(empl.__str__() + '\n\n')
            except Exception as e:
                print(e)
            input("Presiona Enter para continuar...")
            clear()
        elif opte == 3:
            try:
                print('-Editar Empleado-')
                emplid = int(input('Ingrese numero de legajo: '))
                empl = Employee.objects.get(emplid)
                pos = str(Position.objects.get(empl.position))
                sec = str(Sector.objects.get(empl.sector))
                sen = str(Seniority.objects.get(empl.seniority))
                print('Edite la informacion del usuario.\nSi no desea modificar un campo solo presione ENTER.')
                res = raw_input('Nombre [' + str(empl.name) + ']: ')
                empl.name = res or empl.name
                res = raw_input('Apellido [' + str(empl.lastname) + ']: ')
                empl.lastname = res or empl.lastname
                res = raw_input('Puesto [' + pos + ']: ')
                pos = res or pos
                res = raw_input('Area [' + sec + ']: ')
                sec = res or sec
                res = raw_input('Categoria [' + sen + ']: ')
                sen = res or sen
                res = raw_input('Salario [$' + str(empl.salary) + ']: $')
                empl.salary = res or empl.salary
                try:
                    empl.position = Position.objects.getid(pos)
                    empl.sector = Sector.objects.getid(sec)
                    empl.seniority = Seniority.objects.getid(sen)
                except Exception as e:
                    print(e)
                try:
                    Employee.objects.save(empl)
                except Exception as e:
                    print(e)
            except Exception as e:
                print(e)
            input("Presiona Enter para continuar...")
            clear()
        elif opte == 4:
            try:
                print('-Borrar Empleado-')
                emplid = int(input('Ingrese numero de legajo: '))
                empl = Employee.objects.delete(emplid)
            except Exception as e:
                print(e)
            finally:
                print('/' + empl.__str__() + '/ ha sido eliminado!\n\n')
            input("Presiona Enter para continuar...")
        elif opte == 5:
            run = False
        else:
            print('Opcion no valida o no habilitada.')
            input("Presiona Enter para continuar...")
            clear()


if __name__ == '__main__':
    main()

