
class ComponenteConexo:
    def __init__(self, id, lpointsc, lboundaryc, lbbc):
        """
        Constructor
        :param id: cantidad de componentes detectados
        :param lpointsc: lista con los puntos que definen al componente c
        :param lboundaryc: lista con los puntos que definen el borde del componente c
        :param lbbc: lista con [x,y,w,h] con x,y representa el punto inicial y w el ancho y h el largo
        """
        self._id = id
        self._lpointsc = lpointsc
        self._lboundaryc = lboundaryc
        self._lbbc = lbbc



