import sqlite3

from position import Position
from sector import Sector
from seniority import Seniority

DB_PATH = 'db.db'


class EmployeeDoNotExists(Exception):
    pass


class EmployeeManager(object):

    def __init__(self, database=None):
        if not database:
            database = ':memory:'
        self.conn = sqlite3.connect(database)
        self.cursor = self.conn.cursor()

    def getlastid(self):
        try:
            query = 'SELECT max(ID) FROM employee'
            self.cursor.execute(query)
            lastid = int(self.cursor.fetchone()[0]) + 1
        except:
            lastid=1
        return lastid

    def insert(self, obj):
        query = 'INSERT INTO employee (ID, NAME, LASTNAME, POSITION, SECTOR, SENIORYTY, SALARY) VALUES ("{}", "{}", "{}", "{}", "{}", "{}", "{}")'.format(obj.id, obj.name, obj.lastname, obj.position, obj.sector, obj.seniority, obj.salary)
        self.cursor.execute(query)
        self.conn.commit()
        empl = self.get(obj.id)
        return empl

    def get(self, id):
        query = 'SELECT * FROM employee WHERE ID = "{}"'.format(id)
        self.cursor.execute(query)
        data = self.cursor.fetchone()
        if not data:
            raise EmployeeDoNotExists('Dont exist Employee with ID {}'.format(id))
        empl = Employee(name=data[1], lastname=data[2], position=data[3], sector=data[4], seniority=data[5], salary=data[6])
        empl.id = id
        print(empl)
        return empl

    def update(self, obj_old, obj):
        updated = False
        add_coma = False

        query = 'UPDATE employee SET '

        if obj_old.name != obj.name:
            query += 'name="{}"'.format(obj.name)
            updated = True
            add_coma = True
        if obj_old.lastname != obj.lastname:
            if add_coma:
                query += ', '
            query += 'lastname="{}"'.format(obj.lastname)
            updated = True
            add_coma = True
        if obj_old.position != obj.position:
            if add_coma:
                query += ', '
            query += 'position="{}"'.format(obj.position)
            updated = True
            add_coma = True
        if obj_old.sector != obj.sector:
            if add_coma:
                query += ', '
            query += 'sector="{}"'.format(obj.sector)
            updated = True
            add_coma = True
        if obj_old.seniority != obj.seniority:
            if add_coma:
                query += ', '
            query += 'seniority="{}"'.format(obj.seniority)
            updated = True
            add_coma = True
        if obj_old.salary != obj.salary:
            query += 'salary="{}"'.format(obj.salary)
            updated = True

        if updated:
            query += ' WHERE ID="{}"'.format(obj.id)
            self.cursor.execute(query)
            self.conn.commit()

    def save(self, obj):
        try:
            old_obj = self.get(id=obj.id)
        except EmployeeDoNotExists:
            self.insert(obj)
        else:
            self.update(old_obj, obj)

    def delete(self, obj):
        query = 'DELETE FROM employee WHERE id="{}"'.format(obj.id)
        self.cursor.execute(query)
        self.conn.commit()


class Employee(object):
    """Employee Model"""
    objects = EmployeeManager(DB_PATH)

    def __init__(self, name, lastname, position, sector, seniority, salary):
        self.id = Employee.objects.getlastid()
        self.name = name
        self.lastname = lastname
        self.position = position
        self.sector = sector
        self.seniority = seniority
        self.salary = salary

    def __repr__(self):
        pos = str(Position.objects.get(self.position))
        sec = str(Sector.objects.get(self.sector))
        sen = str(Seniority.objects.get(self.seniority))
        fullname = str(self.lastname) + ', ' + str(self.name)
        pos = str(pos) + '/' + str(sec)
        return str(self.id).zfill(4) + ' - ' + fullname + ' - ' + pos + ' - ' + sen + ' - $' + str(self.salary)

