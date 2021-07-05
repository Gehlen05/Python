""" Execucao --> \PycharmProjects\ProjetoNexus\src>python main.py name_file.txt name_file_2.(txt/csv)"""

import sys

import nexus

if __name__ == "__main__":
    nexus.Nexus(sys.argv[1],  sys.argv[2])
