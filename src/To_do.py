

class ToDo:
    def __init__(self,  id, titulo, descricao, status = False):
        self._id = int(id)
        self._titulo = titulo
        self._descricao = descricao
        self._status = status
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, new_id):
        self._id = new_id
        return self._id

    @property
    def titulo(self):
        return self._titulo
    
    @titulo.setter
    def titulo(self, new_titulo):
        self._titulo = new_titulo
        return self._titulo
    
    @property
    def descricao(self):
        return self._descricao
    
    @descricao.setter
    def descricao(self, new_descricao):
        self._descricao = new_descricao
        return self._descricao
    

    @property
    def status(self):
        return self._status
    

    @status.setter
    def status(self, new_status):
        self._status = new_status
        return self._status
    
    def __str__(self):
        return f'{self._id},{self._titulo},{self._descricao},{self._status}'
        
    



    
    

    




        
        

        