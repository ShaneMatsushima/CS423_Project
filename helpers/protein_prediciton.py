'''
---App for Bio Informatics Research w/ Dr.Hutcheson---
Created: 2/12/2024
Author: Shane Matssuhima
'''
import biolib as bl
import os

'''
Input: filePath, savePath
Output: path to saved pdb file
Summary: this function will predict the protein structure of a sequence and save it as 
        as pdp file to model
'''
def predict(filePath: str, savePath: str) -> str:
        alphafold = bl.load('AlphaFold/alphafold')

        arguments = '--fasta_paths ' + filePath

        result = alphafold.cli(args=arguments)

        result.save_file(savePath)

        #TODO check if file was saved properly
        if not os.path.isfile(savePath):
                ...
