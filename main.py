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
        opt = int(input('\r1- Administrar Empleados\n\r2- Administrar Caracteristicas\n\r3- Salir\n'))
        clear()
        if opt == 1:
            print('Administrar Empleados:\nElija la opcion deseada:')
            opte = int(input('\r1- Ver Datos de Empleado\n\r2- Actualizar datos de empleados\n\r3- Borrar Empleado\n\r4- Salir\n'))
            clear()
            if opte == 1:
                try:
                    emplid = int(input('Ingrese numero de legajo: '))
                    empl = Employee.objects.get(emplid)
                    print(empl.__str__() + '\n\n')
                except Exception as e:
                    print(e)
                input("Presiona Enter para continuar...")
                clear()
            elif opte == 2:
                try:
                    emplid = int(input('Ingrese numero de legajo: '))
                    empl = Employee.objects.get(emplid)
                    pos = str(Position.objects.get(empl.position))
                    sec = str(Sector.objects.get(empl.sector))
                    sen = str(Seniority.objects.get(empl.seniority))
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
                run = False
            else:
                print('Opcion no valida o no habilitada.')
                input("Presiona Enter para continuar...")
                clear()
        elif opt == 3:
            run = False
        else:
            print('Opcion no valida o no habilitada.')
            input("Presiona Enter para continuar...")
            clear()


if __name__ == '__main__':
    main()

