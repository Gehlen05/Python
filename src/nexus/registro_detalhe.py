class RegistroDetalhe:
    def __init__(self, myline):
        self.nome_favorecido = self._get_nome_favorecido(myline)
        self.data_pagamento = self._get_data_pagamento(myline)
        self.tipo_moeda = self._get_tipo_moeda(myline)
        self.valor_pagamento = self._get_valor_pagamento(myline)
        self.numero_domcumento = self._get_num_doc_atribuido(myline)

    @staticmethod
    def _get_nome_favorecido(myline):
        return myline[43:72]

    @staticmethod
    def _get_data_pagamento(myline):
        dia = myline[93:95]
        mes = myline[95:97]
        ano = myline[97:101]
        return dia + '/' + mes + '/' + ano

    @staticmethod
    def _get_tipo_moeda(myline):
        tipo_moeda = {"BRL": "R$", "USA": "$"}
        return tipo_moeda[myline[101:104]]

    @staticmethod
    def _get_valor_pagamento(myline):
        decimal = str(int(myline[132:134])/100)
        inteira = str(int(myline[119:132]))
        return inteira + decimal

    @staticmethod
    def _get_num_doc_atribuido(myline):
        return myline[73:92]
