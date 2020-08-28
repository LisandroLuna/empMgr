class Employee(object):
    def __init__(self, name, lastname, position, sector, seniority, salary):
        self.name = name
        self.lastname = lastname
        self.position = position
        self.sector = sector
        self.seniority = seniority
        self.salary = salary

    def chgName(self, newname):
        self.name = newname

    def chgLast(self, newlast):
        self.lastname = newlast

    def chgFullName(self, newname, newlast):
        self.chgName(newname)
        self.chgLast(newlast)

    def chgPos(self, newpos):
        self.position = newpos

    def chgSec(self, newsec):
        self.position = newsec

    def chgPostSec(self, newpos, newsec):
        self.chgPos(newpos)
        self.chgSec(newsec)

    def chgSen(self, newsen):
        self.seniority = newsen

    def chgSal(self, newsal):
        self.salary = newsal

    def chgFullFunc(self, newpos, newsec, newsen, newsal):
        self.chgPos(newpos)
        self.chgSec(newsec)
        self.chgSen(newsen)
        self.chgSal(newsal)

    def __repr__(self):
        fullname = self.lastname + ', ' + self.name
        pos = self.position + '/' + self.sector
        return fullname + ' - ' + pos + ' - ' + self.seniority + ' - $' + str(self.salary)


class Position:
    def __init__(self, name):
        self.name = name

    def chgName(self, newname):
        self.name = newname

    def __repr__(self):
        return self.name


class Sector:
    def __init__(self, name):
        self.name = name

    def chgName(self, newname):
        self.name = newname

    def __repr__(self):
        return self.name


class Seniority:
    def __init__(self, name):
        self.name = name

    def chgName(self, newname):
        self.name = newname

    def __repr__(self):
        return self.name




