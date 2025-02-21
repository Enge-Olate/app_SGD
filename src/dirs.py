import os

get_path = 'c:/Users/marci/Documentos'
pastas = ['TESTE', 'PDF', 'DIELETRICO']

class Dirs:
    def __init__(self):
        self.get_path = get_path
        self.pastas = pastas
        
        pass
    def criar_pastas(self):
        try:
            os.chdir(self.get_path)
            for pasta in self.pastas:
                os.mkdir(pasta)
            pass
        except:
            pass