'''
---App for Bio Informatics Research w/ Dr.Hutcheson---

The prediction page is where users will go to predict renderings of protein sequences. 

Created: 2/12/2024
Author: Shane Matssuhima, Ian Thompson, Austen Furutani
'''

import streamlit as st
import streamlit.components.v1 as components
import py3Dmol as mdl
from helpers.displayStruct import displayStruct 
import tempfile
import os


from helpers.protein_prediciton import predictFasta
from helpers.sequencing import checkProteinSeq, seqToFasta

TMP_FASTA = "..\\helpers\\tmp.fasta"

# Page Setup for app
st.set_page_config(
    page_title="BioInformatics App",
    layout='wide',
    page_icon="🧬",
)

PREDICT_FLAG = False # global flag to keep track of if a prediction has been made or not
SAVED_PDB = None # use as global variable on page to keep track of pdb file path
UPLOADED_PDB = None
DISPLAY = False
NEW = False
TMP_PATH = "\\tmp"
PDB_LIST = []
# sidebar widgets and texts are placed here
def cs_sidebar()-> None:
    global DISPLAY, UPLOADED_PDB, NEW,PDB_LIST
    st.sidebar.header("Predicting")
    st.sidebar.write("Navigate to:\n https://colab.research.google.com/drive/1BaxkrRrxEOvl6mJ1spcjtxyW_H24dD7Y \n to  generate the predicted structure of a protein")

    # st.sidebar.caption("Text of Sequence: ")
    # seq = st.sidebar.text_area("Sequence to predict")

    files = st.sidebar.file_uploader("Upload .PDB File Here", accept_multiple_files=True)

    for file in files:
        temp_dir = tempfile.mkdtemp()
        path = os.path.join(temp_dir, file.name)
        PDB_LIST.append(path)
        DISPLAY = True

    
#TODO add progress bar for predicting and loading model
# main body of application  is placed in this function
def cs_body() -> None:
    global DISPLAY, NEW, PDB_LIST
    st.title("Predicting Protein Structures")
    if DISPLAY:
        for pdb in PDB_LIST:
            html = displayStruct(pdb)
            components.html(html, height = 600)
        




# main function to run app
def main() -> None:
    cs_sidebar()
    cs_body()

if __name__ == '__main__':
    main()