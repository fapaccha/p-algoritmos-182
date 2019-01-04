class Equipo():
    
    def __init__(self, nom, ciu, camp,numj):
        self.nombre = nom
        self.ciudad = ciu
        self.campeonato = camp
        self.numJugadores = numj

    def agregar_nombre(self, n):
        """
        """
        self.nombre = n

    def obtener_nombre(self):
        """
        """
        return self.nombre

    def agregar_ciudad(self, a):
        """
        """
        self.ciudad = a
        
    def obtener_ciudad(self):
        """
        """
        return self.ciudad

    def agregar_campeonato(self, n):
        """
        """
        self.campeonato = n

    def obtener_campeonato(self):
        """
        """
        return self.campeonato
    
    def agregar_numJug(self, n):
        """
        """
        self.numJugadores = n

    def obtener_numJug(self):
        """
        """
        return self.numJugadores

    def __str__(self):
        """
        """
        return "%s - %s - %s - %s  " % (self.obtener_nombre() ,self.obtener_ciudad () ,self.obtener_campeonato (),self.obtener_numJug())

    def __repr__(self):
        """
        """
        return "%s - %s - %s - %s  " % (self.obtener_nombre() ,self.obtener_ciudad () ,self.obtener_campeonato (),self.obtener_numJug())
 

class Operaciones(object):
    
    def __init__(self, listado):
        self.listado_equipos = listado

    def ordenar_nombre(self):
        return sorted(self.listado_equipos, key=lambda equipo: equipo.obtener_nombre())

    def ordenar_campeonatos(self):
        return sorted(self.listado_equipos, key=lambda equipo: equipo.obtener_campeonato())