import os

class Dirs:
    def __init__(self, nome_pasta=None, get_path=None, pastas=None):
        if nome_pasta is None:
            nome_pasta = input('Digite o nome da pasta: ')
        if get_path is None:
            get_path = os.path.expanduser('~/Documentos')
        if pastas is None:
            pastas = ['TESTE', 'PDF', 'DIELETRICO']
        
        self.get_path = get_path
        self.pastas = pastas
        self.nome_pasta = nome_pasta
        self.mensagem = f'A pasta {self.nome_pasta} já existe.'
        
    def criar_pastas(self):
        try:
            if self.get_path:
                print(f'Tentando mudar para o diretório: {self.get_path}')
                os.chdir(self.get_path)
            else:  
                raise FileNotFoundError('Diretório não encontrado!')

            print(f'Tentando criar a pasta: {self.nome_pasta}')
            if not os.path.exists(self.nome_pasta):
                os.makedirs(self.nome_pasta)
            else:
                raise FileExistsError(self.mensagem)
            print(f'Tentando mudar para o diretório: {self.nome_pasta}')    
            os.chdir(self.nome_pasta)
            for pasta in self.pastas:
                print(f'Tentando criar a subpasta: {pasta}')
                if not os.path.exists(pasta):
                    os.makedirs(pasta)
            print(f'Pasta {self.nome_pasta} criada com sucesso!')
            
        except FileExistsError:
            print(f'Erro: {self.mensagem}')
        except FileNotFoundError:
            print('Erro: Diretório não encontrado!')
            raise os.EX_OSERR
        finally:
            print('Fim do programa!')