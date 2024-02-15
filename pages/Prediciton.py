'''
---App for Bio Informatics Research w/ Dr.Hutcheson---

The prediction page is where users will go to predict renderings of protein sequences. 

Created: 2/12/2024
Author: Shane Matssuhima, Ian Thompson, Austen Furatani
'''

import streamlit as st
import py3Dmol as mdl

# Page Setup for app
st.set_page_config(
    page_title="BioInformatics App",
    layout='wide',
    page_icon="🧬",
)

PREDICT_FLAG = False # global flag to keep track of if a prediction has been made or not
SAVED_PDB = None # use as global variable on page to keep track of pdb file path

# sidebar widgets and texts are placed here
def cs_sidebar()-> None:
    st.sidebar.header("Predicting")
    st.sidebar.write("Paste the sequence in the text box bellow or upload the fasta file bellow: ")

    st.sidebar.caption("Text of Sequence: ")
    seq = st.sidebar.text_area("Sequence to predict")

    file = st.sidebar.file_uploader("Upload Fasta File Here")

    #TODO check if a file or text was used (if none report issue)

    #TODO check to make sure a sequence is usable 

    #TODO implement functional button to predict outcome and display prediction ot body
    clicked = st.sidebar.button(":green[Start Predicting]")

    if clicked:
        PREDICT_FLAG = True
        if file == None and seq == None:
            st.sidebar.error("No File or sequence could be found to predict structure")
        if file != None:
            #TODO add function that predicts reading seq
            ...
        elif seq != None:
            #TODO add function that predicts reading from fasta file
            ...
        

    

# main body of application  is placed in this function
def cs_body() -> None:
    st.title("Predicting Protein Structures")
    if PREDICT_FLAG:
        if SAVED_PDB == None:
            st.error("PDB file unable to be found.")
        else:
            # display 3d rendering of pdb file on the main page
            with open(SAVED_PDB, 'r') as f:
                data = "".join([x for x in f])
            view = mdl.view(width=800, height=800)
            view.addModelsAsFrames(data)
            view.setStyle({'model': -1}, {"cartoon": {'color': 'spectrum'}})
            view.zoomTo()
            view.show()




# main function to run app
def main() -> None:
    cs_sidebar()
    cs_body()
    return None

if __name__ == '__main__':
    main()