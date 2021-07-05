import csv
class Report:
    def __init__(self, output_file):
        self.file_header = []
        self.header_lote = []
        self.registro_detalhe = []
        self.trailer_lote = []
        self._output_file = output_file

    def print_report(self):
        """Generate the report file"""
        if self._get_report_type() == 'txt':
            self._print_txt_report()

        elif self._get_report_type() == 'csv':
            self._print_csv_report()

        elif self._get_report_type() == 'html':
            self._print_html_report()
        else:
            raise Exception('Unknow extensios for output file-Report not generated')

    def _get_report_type(self):
        return self._output_file.split('.')[-1]

    def _print_txt_report(self):
        with open(self._output_file, 'w') as output_file:
            output_file.write('------------------------------------------------------------'
                              '-------------------------------------------------------------'
                              '------------------------------------------------------------------------\n')
            output_file.write('Nome da Empresa               | Numero de Inscricao da Empresa | Nome do Banco         '
                              '      | Nome da Rua                 | Numero do Local | Nome da Cidade       | CEP     '
                              '  | Sigla do Estado\n')
            output_file.write('----------------------------------------------------------------------------'
                              '-----------------------------------------------------------------------------'
                              '----------------------------------------\n')

            for file_header in self.file_header:
                for header_lote in self.header_lote:
                    output_file.write(file_header.nome_empresa + '|' +
                                      file_header.num_inscricao + '              |' +
                                      file_header.nome_banco + '|' +
                                      header_lote.nome_rua + '|' +
                                      header_lote.num_local +  '             |' +
                                      header_lote.nome_cidade + '   |' +
                                      header_lote.cep + ' |' + header_lote.sigla_estado + '\n')
            output_file.write('----------------------------------------------------------------------------------'
                              '-----------------------------------------------------------------------------------'
                              '----------------------------\n')
            output_file.write('----------------------------------------------------------------------------------'
                              '-----------------------------------------------------\n')
            output_file.write('Nome do Favorecido          | Data de Pagamento | Valor do Pagamento | Numero do '
                              'Documento Atribuido pela Empresa | Forma de Lancamento\n')
            output_file.write('----------------------------------------------------------------------------------'
                              '-----------------------------------------------------\n')

            for registro_detalhe in self.registro_detalhe:
                for header_lote in self.header_lote:
                    output_file.write(registro_detalhe.nome_favorecido + '|' +
                                      registro_detalhe.data_pagamento + '        | ' +
                                      registro_detalhe.tipo_moeda + ' ' +
                                      registro_detalhe.valor_pagamento + '             | ' +
                                      registro_detalhe.numero_domcumento + '                 ' +
                                      header_lote.forma_lancamento + '\n')
            output_file.write('--------------------------------------------------------------------------'
                              '-------------------------------------------------------------\n')

    def _print_csv_report(self):
        header = ['Nome da Empresa', 'Numero de Inscricao da Empresa', 'Nome do Banco ',
                  'Nome da Rua', 'Numero do Local', 'Nome da Cidade', 'CEP', 'Sigla do Estado']
        header2 = ['Nome do Favorecido', 'Data de Pagamento', 'Valor do Pagamento',
                   'Numero do Documento Atribuido pela Empresa', 'Forma de Lancamento']

        with open(self._output_file, 'w') as output_file:
            writer = csv.writer(output_file, delimiter = ';', lineterminator = '\n')
            writer.writerow(header)
            for file_header in self.file_header:
                for header_lote in self.header_lote:
                    data = [file_header.nome_empresa.strip(), file_header.num_inscricao.strip(), file_header.nome_banco.strip(),
                            header_lote.nome_rua.strip(), header_lote.num_local.strip(), header_lote.nome_cidade.strip(),
                            header_lote.cep.strip(), header_lote.sigla_estado.strip()]
                    writer.writerow(data)

            writer.writerow(header2)
            for registro_detalhe in self.registro_detalhe:
                for header_lote in self.header_lote:
                    data = [registro_detalhe.nome_favorecido.strip(), registro_detalhe.data_pagamento.strip(),
                            registro_detalhe.tipo_moeda.strip() + ' ' + registro_detalhe.valor_pagamento.strip(),
                            registro_detalhe.numero_domcumento.strip(), header_lote.forma_lancamento.strip()]
                    writer.writerow(data)

    def _print_html_report(self):
        pass