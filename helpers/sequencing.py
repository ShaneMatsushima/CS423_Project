'''
---App for Bio Informatics Research w/ Dr.Hutcheson---

Helper file to produce sequence functionality.
This is to ensure seperation from gui and functionality for easier testing.

Created: 2/12/2024
Author: Shane Matssuhima, Ian Thompson, Austen Furutani
'''
import json
import os
#TODO write sequencing functions for raw data -> output: information of sequence

def seqToFasta(seq:str)->str:
    
    output_file = "helpers\\tmp.fasta" # tmp for running alphafold since it likes fasta files
    print(os.path.join(os.getcwd(), output_file))

    with open(output_file, 'w') as file: # clear tmp file so fasta not appended
        file.write("")

    with open(output_file, 'w') as file:
        file.write(f'>tmp fasta\n{seq}\n')
    
    return output_file

def checkProteinSeq(seq:str) ->bool:
    seq = seq.upper()
    if  len(seq) % 3 != 0:
        return False
    if not seq:
        return False
    
    for i in seq:
        if i not in "ABCDEFGHIKLMNPQRSTVWY":
            return False
    
    return True

if __name__ == '__main__':
    # put test code here
    ...