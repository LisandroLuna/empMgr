from employee import Employee, Position, Sector, Seniority


def main():
    nam1 = 'Juan'
    las1 = 'Perez'
    pos1 = Position('Empleado')
    sec1 = Sector('Finanzas')
    sen1 = Seniority('Junior')
    sal1 = 60000
    empl1 = Employee(nam1, las1, pos1.__str__(), sec1.__str__(), sen1.__str__(), sal1)

    nam2 = 'Esteban'
    las3 = 'Lopez'
    pos2 = Position('Gerente')
    sec2 = Sector('Sistemas')
    sen2 = Seniority('Senior')
    sal2 = 120000
    empl2 = Employee(nam2, las3, pos2.__str__(), sec2.__str__(), sen2.__str__(), sal2)

    print(empl1.__str__())
    print(empl2.__str__() + '\n')

    print('Actualizo Posicion, Sueldo y Seniority de: Perez, Juan:')
    empl1.chgFullFunc('Gerente', 'Operaciones', 'Senior', 130000)
    print('\t' + empl1.__str__() + '\n')

    print('Actualizo Sueldo de: Lopez, Esteban:')
    empl2.chgSal(200000)
    print('\t' + empl2.__str__() + '\n')


if __name__ == '__main__':
    main()

