import json

class ApiResponse:
    
    def __init__(self, success=None, errMsj=None, data=None):
        self.success = success
        self.errMsj = errMsj
        self.data = data

    def to_json(self):
        apires = { 
            'success' : self.success, 
            'errMsj' : self.errMsj,
            'data' : self.data
            }
        return json.dumps(apires)
    
    def from_json(self, jsonData):
        self.success = jsonData['success']
        self.errMsj = jsonData['errMsj']
        self.data = jsonData['data']
        return self
