from .file_header import FileHeader
from .header_lote import HeaderLote
from .registro_detalhe import RegistroDetalhe
from datetime import datetime
from .report import Report

class Nexus:
    def __init__(self, input_file, output_file):
        self.report = Report(output_file)
        self.process(input_file, output_file)

    def process(self, input_file, output_file):
        """por messsagem"""
        try:
            log_file = open('log_file.txt', 'w')
            log_file.write('[{}] Info: Started process \n'.format(datetime.now()))

            with open('nexus/' + input_file, 'r') as myfile:
                for myline in myfile:
                    if myline[7] == '0':
                        log_file.write('[{}] Info: Reading File Header \n'.format(datetime.now()))
                        self.report.file_header.append(FileHeader(myline))
                    elif myline[7] == '1':
                        log_file.write('[{}] Info: Reading Header Lote \n'.format(datetime.now()))
                        self.report.header_lote.append(HeaderLote(myline))
                    elif myline[7] == '3':
                        log_file.write('[{}] Info: Reading Registro de Detalhe \n'.format(datetime.now()))
                        self.report.registro_detalhe.append(RegistroDetalhe(myline))
                    elif myline[7] == '5':
                        log_file.write('[{}] Info: Reading Trailer Lote \n'.format(datetime.now()))
                        pass
                    elif myline[7] == '9':
                        log_file.write('[{}] Info: Reading Trailer de Arquivo \n'.format(datetime.now()))
                        pass
                    else:
                        log_file.write('[{}] Error: Digito invalido na posicao 8 \n'.format(datetime.now()))

                log_file.write('[{}] Info: Started Report \n'.format(datetime.now()))
                self.report.print_report()
                log_file.write('[{}] Info: Finish Report \n'.format(datetime.now()))
        except Exception as error:
            log_file.write('[{}] Error: {}: \n'.format(datetime.now(), error))

        log_file.write('[{}] Info: End \n'.format(datetime.now()))
        log_file.close()







