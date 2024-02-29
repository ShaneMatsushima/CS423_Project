'''
---App for Bio Informatics Research w/ Dr.Hutcheson---

Helper file to produce sequence functionality.
This is to ensure seperation from gui and functionality for easier testing.

Created: 2/12/2024
Author: Shane Matssuhima, Ian Thompson, Austen Furutani
'''
import json
#TODO write sequencing functions for raw data -> output: information of sequence

def loadDict(dictPath:str) -> dict:
    with open(dictPath, 'r') as file:
        return json.load(file)

def seq_to_fasta(seq_data:dict, gi:str)->str:

    output_file = "helpers\tmp.fasta" # tmp for running alphafold since it likes fasta files

    with open(output_file, 'w') as file: # clear tmp file so fasta not appended
        file.write("")

    with open(output_file, 'w') as file:
        file.write(f'>{gi}\n{seq_data[gi]}\n')
    
    return output_file

if __name__ == '__main__':
    # put test code here
    ...