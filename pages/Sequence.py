'''
---App for Bio Informatics Research w/ Dr.Hutcheson---

The sequencing page is where users will go to align and analyze sequences of data. 

Created: 2/12/2024
Author: Shane Matssuhima, Ian Thompson, Austen Furutani
'''

import streamlit as st
from Bio.Blast import NCBIWWW
import json 

class proteinRaw:
    def __init__(self, s:str, gi:str):
        self.gi = gi
        self.sequence = s

    def get_gi(self):
        return self.gi
    
    def get_seq(self):
        return self.sequence

selected_seq = []

flag = False

# Page Setup for app
st.set_page_config(
    page_title="BioInformatics App",
    layout='wide',
    page_icon="🧬",
)

#TODO add dropdown for database input for blastp
# sidebar widgets and texts are placed here
def cs_sidebar()-> None:
    st.sidebar.header("Sequencing")
    file = st.sidebar.file_uploader("Upload JSON dict for gi_to_seq Here")
    if file:
        gi_dict = json.load(file)

        selected = st.sidebar.multiselect("Select GI to get Sequence", gi_dict.keys(), default=None)

        for key in selected:
            selected_seq.append(proteinRaw(gi_dict[key], key))


# main body of application  is placed in this function
def cs_body() -> None:
    # loop through all selected GI's and display their sequence alignments and analysis
    if selected_seq != None:
        for s in selected_seq:
            temp_seq = s.get_seq().upper()
            st.write(f"Protein Sequence: {temp_seq}")
            
            with st.spinner("Performing Blastp on Sequence"):
                result_handle = NCBIWWW.qblast('blastp', 'nr', sequence=temp_seq, format_type='Text')

            if result_handle != None:
                st.success(f"Blastp Data result:\n {result_handle.read()}")
            else:
                st.error('Unable to perform Blastp')


# main function to run 
def main() -> None:
    cs_sidebar()
    cs_body()
    return None

if __name__ == '__main__':
    main()