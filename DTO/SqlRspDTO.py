import json

class SqlRspDTO:
    
    def __init__(self, success=None, sMsj=None):
        self.nCod = success
        self.sMsj = sMsj

    def to_json(self):
        apires = { 
            'nCod' : self.nCod, 
            'sMsj' : self.sMsj,
            }
        return json.dumps(apires)
    
    def from_json(self, jsonData):
        self.nCod = jsonData['nCod']
        self.sMsj = jsonData['sMsj']
        return self
