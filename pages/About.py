'''
---App for Bio Informatics Research w/ Dr.Hutcheson---

The about page is for information regarding running and functionality of the app. 

Created: 2/12/2024
Author: Shane Matssuhima, Ian Thompson, Austen Furutani
'''
import streamlit as st

# Page Setup for app
st.set_page_config(
    page_title="BioInformatics App",
    layout='wide',
    page_icon="🧬",
)

# sidebar widgets and texts are placed here
def cs_sidebar()-> None:
    st.sidebar.header("About Page")
    

# main body of application  is placed in this function
def cs_body() -> None:
    st.title("The Project")
    st.write("This project is part of a bioinformatics class at the University of Portland. " + 
             "The goal is to take sequences of proteins and analyze the sequencing. "+
             "With the analyzation of the sequence, the goal is to output vital information about the sequence "+
             "as well as predict the protein structure based on the sequence.")
    
    st.divider()

    st.subheader("How to Sequence")
    st.write("Given a sequence, this page allows the user to align the sequence, find areas of smiliarity, and find distant but relative sequences. "+
             "The input sequence can either be a string (placed in a text box) or by uplaoding a fasta file. "+
             "The sequence analytics will display on the screen once analyzing is complete. ")
    
    st.divider()
    
    st.subheader("How to Predict")
    st.write(" Using ______, the prediction page allows users to input a sequence or fasta file and predict the "+
             "3D structure of the protein. Once the protein is predicted, it will save as a pdb file and the pdb file "+
             "will be rendered on the screen to visually see the 3D model.")
    
    st.divider()
    st.subheader("Acknowledgements")

# main function to run app
def main() -> None:
    cs_sidebar()
    cs_body()
    return None

if __name__ == '__main__':
    main()