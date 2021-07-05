class HeaderLote:
    def __init__(self, myline):
        self.nome_rua = self._get_nome_rua(myline)
        self.num_local = self._get_num_local(myline)
        self.nome_cidade = self._get_nome_cidade(myline)
        self.cep = self._get_cep(myline)
        self.sigla_estado = self._get_sigla_estado(myline)
        self.forma_lancamento = self._get_forma_lancamento(myline)

    @staticmethod
    def _get_nome_rua(myline):
        return myline[142:171]

    @staticmethod
    def _get_num_local(myline):
        return myline[172:176]

    @staticmethod
    def _get_nome_cidade(myline):
        return myline[192:212]

    @staticmethod
    def _get_cep(myline):
        return myline[212:217] + '-' + myline[217:220]

    @staticmethod
    def _get_sigla_estado(myline):
        return myline[220:222]

    @staticmethod
    def _get_forma_lancamento(myline):
        chave = (int(myline[12:13]))
        forma_pagamento = {1: "Credito em Conta Corrente", 2: "Cheque Pagamento / Administrativo", 3: "DOC/TED",
                           4: "Cartao Salario", 5: "Credito em Conta Popanca", 6: "Liberacao de Titulos HSBC",
                           7: "Emissao de Cheque Salario", 8: "Liquidacao de Parcelas de Cobranca Nao Registrada",
                           9: "Arrecadacao de Tributos Federais", 10: "OP a Disposicao",
                           11: "Pagamentos de Contas e Tributos com Código de Barras", 12: "Doc Mesma Titularidade",
                           13: "Pagamentos de Guias", 14: "Credito em Conta Corrente Mesma Titularidade",
                           16: "Tributo - DARF Normal", 17: "Tributo - GPS (Guia da PrevidÊncia Social)",
                           18: "Tributo - DaRF Simples", 19: "Tributo - IPTU - Prefeituras",
                           20: "Pagamento com Autenticação", 21: "Tributo - DARJ"}
        return forma_pagamento[chave]
