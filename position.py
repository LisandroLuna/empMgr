import sqlite3


DB_PATH = 'db.db'


class PositionDoNotExists(Exception):
    pass


class PositionManager(object):
    def __init__(self, database=None):
        if not database:
            database = ':memory:'
        self.conn = sqlite3.connect(database)
        self.cursor = self.conn.cursor()

    def getlastid(self):
        try:
            query = 'SELECT max(ID) FROM position'
            self.cursor.execute(query)
            lastid = int(self.cursor.fetchone()[0]) + 1
        except:
            lastid = 1
        return lastid

    def getid(self, name):
        query = 'SELECT * FROM position WHERE name = "{}"'.format(name)
        self.cursor.execute(query)
        data = self.cursor.fetchone()
        if not data:
            raise PositionDoNotExists('Dont exist Position with Name {}'.format(name))
        return data[0]

    def insert(self, obj):
        query = 'INSERT INTO position (ID, NAME) VALUES ("{}", "{}")'.format(obj.id, obj.name)
        self.cursor.execute(query)
        self.conn.commit()

    def get(self, id):
        query = 'SELECT * FROM position WHERE ID = "{}"'.format(id)
        self.cursor.execute(query)
        data = self.cursor.fetchone()
        if not data:
            raise PositionDoNotExists('Dont exist Position with ID {}'.format(id))
        pos = Position(name=data[1])
        pos.id = id
        return pos

    def update(self, obj_old, obj):
        updated = False
        if obj_old.name != obj.name:
            query = 'UPDATE position SET name="{}"'.format(obj.name)
            updated = True

        if updated:
            query += ' WHERE ID="{}"'.format(obj.id)
            self.cursor.execute(query)
            self.conn.commit()

    def save(self, obj):
        try:
            old_obj = self.get(id=obj.id)
        except PositionDoNotExists:
            self.insert(obj)
        else:
            self.update(old_obj, obj)

    def delete(self, obj):
        query = 'DELETE FROM position WHERE id="{}"'.format(obj.id)
        self.cursor.execute(query)
        self.conn.commit()


class Position:
    """Position Model"""
    objects = PositionManager(DB_PATH)

    def __init__(self, name):
        self.id = Position.objects.getlastid()
        self.name = name

    def __repr__(self):
        return self.name
