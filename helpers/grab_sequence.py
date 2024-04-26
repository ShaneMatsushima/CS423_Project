'''
---App for Bio Informatics Research w/ Dr.Hutcheson---

Webscrapping script to grab protein sequences based on gi used from excel sheet.
the flag column has been added to select specific subgroups to look at 

Created: 2/12/2024
Author: Shane Matssuhima
'''
from Bio import Entrez
from Bio import SeqIO
import pandas as pd
from io import StringIO
import json

#set email
Entrez.email = "matsushs23@up.edu" # TODO: Change this

def unloadExcel(filePath: str,  sheetName: str) -> pd.DataFrame:
    EXCEL_FILE = filePath
    SHEET = sheetName
    parsed_df = pd.DataFrame() # initialize the DataFrame as empty

    UNCHAR_SFLD_DATA = pd.read_excel(io=EXCEL_FILE, sheet_name=SHEET)

    # parse excel sheet
    col_name = ['common_name', 'subgroup_id', 'subgroup', 'species', 'gi', 'genbank_accession_number', 'flag']
    for name in col_name:
        flagged_df = UNCHAR_SFLD_DATA.loc[UNCHAR_SFLD_DATA['flag'] == 1, name]
        parsed_df = pd.concat([parsed_df, flagged_df], axis=1)
    return parsed_df #return parsed excel file

def grabSequence(gi: str, db: str) -> str:
    handle = Entrez.efetch(db=db, id=gi, rettype='fasta')
    record = list(SeqIO.parse(handle, "fasta"))[0]
    return str(record.seq)

def loadJSON(jsonFile:str)->dict:
    with open(jsonFile) as f:
        data = json.load(f)
    return data

def saveJSON(jsonFile:str, data: dict)->None:
    with open(jsonFile,'w') as outfile:
        json.dump(data, outfile)
    return None

if __name__ == '__main__':
    # file and sheet names for parsing 
    file = "C:\\Users\\proge\\Dev\\spring24\\biotech\\Uncharacterized SFLD data.xlsx" #TODO fix this so its relative path or user input
    sheet = 'Sheet1'

    # grabs and parses important data to a parsed dataframe
    PARSED_DF = unloadExcel(file, sheet)
    print(PARSED_DF)

    # grab all sequences and place them into  a dictionary with keys being GI numbers
    gi_to_seq = {}
    for index, row in PARSED_DF.iterrows():
        gi = row['gi']
        gi = str(gi)
        if gi == "nan":
            continue
        if gi.find(',') != -1:   # there are multiple GIs per entry
            gis = gi.split(', ')
            for this_gi in gis:
                gi_to_seq[this_gi] = grabSequence(this_gi, 'protein')
        else:                     # only one GI number per entry
            gi_to_seq[gi] = grabSequence(gi, 'protein')

    
    saveJSON('gi_to_seq', gi_to_seq)


    


