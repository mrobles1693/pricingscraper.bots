import json

class RegistroPrecioDTO:
    
    def __init__(self, 
                 nIdRegistroPrecio = None,
                 nIdProducto = None,
                 nIdComercio = None,
                 nIdSimilar = None,
                 nIdBotExecution = None,
                 nPrecio = None,
                 nPrecioOferta = None,
                 nPrecioTarjeta = None,
                 dFecha = None,
                 ):
        self.nIdRegistroPrecio = nIdRegistroPrecio
        self.nIdProducto = nIdProducto
        self.nIdComercio = nIdComercio
        self.nIdSimilar = nIdSimilar
        self.nIdBotExecution = nIdBotExecution
        self.nPrecio = nPrecio
        self.nPrecioOferta = nPrecioOferta
        self.nPrecioTarjeta = nPrecioTarjeta
        self.dFecha = dFecha

    def to_json(self):
        jsonString = { 
            'nIdRegistroPrecio' : None,
            'nIdProducto' : int(self.nIdProducto),
            'nIdComercio' : int(self.nIdComercio),
            'nIdSimilar' : int(self.nIdSimilar),
            'nIdBotExecution' : int(self.nIdBotExecution),
            'nPrecio' : self.nPrecio,
            'nPrecioOferta' : self.nPrecioOferta,
            'nPrecioTarjeta' : self.nPrecioTarjeta,
            'dFecha' : None
            }
        return json.dumps(jsonString)
    
    def from_json(self, jsonData):
        self.nIdRegistroPrecio = jsonData['nIdRegistroPrecio']
        self.nIdProducto = jsonData['nIdProducto']
        self.nIdComercio = jsonData['nIdComercio']
        self.nIdSimilar = jsonData['nIdSimilar']
        self.nIdBotExecution = jsonData['nIdBotExecution']
        self.nPrecio = jsonData['nPrecio']
        self.nPrecioOferta = jsonData['nPrecioOferta']
        self.nPrecioTarjeta = jsonData['nPrecioTarjeta']
        self.dFecha = jsonData['dFecha']
        return self
