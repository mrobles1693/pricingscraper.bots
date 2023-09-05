import json

class SimilarDTO:

    def __init__(self, 
                 nIdSimilar=None, 
                 nIdProducto=None, 
                 nIdComercio=None, 
                 sUrl=None, 
                 sDescripcion=None, 
                 sSKU=None, 
                 nPrecio = None,
                 bElegido = None, 
                 bManual = None, 
                 nIdUsuario_crea = None, 
                 sUsuario_crea = None, 
                 dFecha_crea = None):
        self.nIdSimilar = nIdSimilar
        self.nIdProducto = nIdProducto
        self.nIdComercio = nIdComercio
        self.sUrl = sUrl
        self.sDescripcion = sDescripcion
        self.sSKU = sSKU
        self.nPrecio = nPrecio
        self.bElegido = bElegido
        self.bManual = bManual
        self.nIdUsuario_crea = nIdUsuario_crea
        self.sUsuario_crea = sUsuario_crea
        self.dFecha_crea = dFecha_crea

    def to_json(self):
        jsonString = { 
            'nIdSimilar' : None,
            'nIdProducto' : int(self.nIdProducto),
            'nIdComercio' : int(self.nIdComercio),
            'sUrl' : str(self.sUrl),
            'sDescripcion' : str(self.sDescripcion),
            'sSKU' : str(self.sSKU),
            'nPrecio' : float(self.nPrecio),
            'bElegido' : bool(self.bElegido),
            'bManual' : bool(self.bManual),
            'nIdUsuario_crea' : 1,
            'sUsuario_crea' : None,
            'dFecha_crea' : None
            }
        return json.dumps(jsonString)
    
    def from_json(self, jsonData):
        self.nIdSimilar = jsonData['nIdSimilar']
        self.nIdProducto = jsonData['nIdProducto']
        self.nIdComercio = jsonData['nIdComercio']
        self.sUrl = jsonData['sUrl']
        self.sDescripcion = jsonData['sDescripcion']
        self.sSKU = jsonData['sSKU']
        self.nPrecio = jsonData['nPrecio']
        self.bElegido = jsonData['bElegido']
        self.bManual = jsonData['bManual']
        self.nIdUsuario_crea = jsonData['nIdUsuario_crea']
        self.sUsuario_crea = jsonData['sUsuario_crea']
        self.dFecha_crea = jsonData['dFecha_crea']
        return self
