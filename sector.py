import sqlite3


DB_PATH = 'db.db'


class SectorDoNotExists(Exception):
    pass


class SectorManager(object):
    def __init__(self, database=None):
        if not database:
            database = ':memory:'
        self.conn = sqlite3.connect(database)
        self.cursor = self.conn.cursor()

    def getlastid(self):
        try:
            query = 'SELECT max(ID) FROM sector'
            self.cursor.execute(query)
            lastid = int(self.cursor.fetchone()[0]) + 1
        except:
            lastid = 1
        return lastid

    def getid(self, name):
        query = 'SELECT * FROM sector WHERE name = "{}"'.format(name)
        self.cursor.execute(query)
        data = self.cursor.fetchone()
        if not data:
            raise SectorDoNotExists('Dont exist Sector with Name {}'.format(name))
        return data[0]

    def insert(self, obj):
        query = 'INSERT INTO sector (ID, NAME) VALUES ("{}", "{}")'.format(obj.id, obj.name)
        self.cursor.execute(query)
        self.conn.commit()

    def get(self, id):
        query = 'SELECT * FROM sector WHERE ID = "{}"'.format(id)
        self.cursor.execute(query)
        data = self.cursor.fetchone()
        if not data:
            raise SectorDoNotExists('Dont exist Position with ID {}'.format(id))
        pos = Sector(name=data[1])
        pos.id = id
        return pos

    def update(self, obj_old, obj):
        updated = False
        if obj_old.name != obj.name:
            query = 'UPDATE sector SET name="{}"'.format(obj.name)
            updated = True

        if updated:
            query += ' WHERE ID="{}"'.format(obj.id)
            self.cursor.execute(query)
            self.conn.commit()

    def save(self, obj):
        try:
            old_obj = self.get(id=obj.id)
        except SectorDoNotExists:
            self.insert(obj)
        else:
            self.update(old_obj, obj)

    def delete(self, obj):
        query = 'DELETE FROM sector WHERE id="{}"'.format(obj.id)
        self.cursor.execute(query)
        self.conn.commit()


class Sector:
    """Sector Model"""
    objects = SectorManager(DB_PATH)

    def __init__(self, name):
        self.id = Sector.objects.getlastid()
        self.name = name

    def __repr__(self):
        return self.name

