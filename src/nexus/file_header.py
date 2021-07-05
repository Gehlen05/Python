class FileHeader:
    def __init__(self, myline):
        self.nome_empresa = self._get_nome(myline)
        self.num_inscricao = self._get_num_inscricao(myline)
        self.nome_banco = self._get_nome_banco(myline)

    @staticmethod
    def _get_nome(myline):
        return myline[72:102]

    @staticmethod
    def _get_num_inscricao(myline):
        return myline[18:20] + '.' + myline[20:23] + '.' + myline[23:26] + '-' + myline[26:30] + '/' + myline[30:32]

    @staticmethod
    def _get_nome_banco(myline):
        return myline[102:131]
