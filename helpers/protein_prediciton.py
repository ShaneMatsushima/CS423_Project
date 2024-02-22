'''
---App for Bio Informatics Research w/ Dr.Hutcheson---

Helper file to help predict and produce pdb files to be rendered. 
This is to ensure seperation between gui and functionality for easier testing. 

Created: 2/12/2024
Author: Shane Matssuhima, Ian Thompson, Austen Furutani
'''
import biolib as bl
import os

'''
Input: filePath, saveDir
Output: path to saved pdb file
Summary: this function will predict the protein structure of a sequence and save it as 
        as pdp file to model
'''
def predictFasta(filePath: str, saveDir: str) -> str:
        alphafold = bl.load('AlphaFold/alphafold')

        arguments = '--fasta_paths ' + filePath

        result = alphafold.cli(args=arguments)

        #TODO add way to get name from file in filePath
        savePath = saveDir + "someFileName.pdb"

        result.save_file(savePath)

        #TODO check if file was saved properly
        if not os.path.isfile(savePath):
                ...
        
        return savePath
