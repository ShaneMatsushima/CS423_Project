'''
---App for Bio Informatics Research w/ Dr.Hutcheson---
Created: 2/12/2024
Author: Shane Matssuhima
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
    st.sidebar.header("Select A Page Above")
    

# main body of application  is placed in this function
def cs_body() -> None:
    st.title("Sequence and Predict")
    st.caption("Created By: Shane Matsushima")
    st.caption("Under Guidance of Dr.VanDeGrift and Dr.Hutcheson")
    st.divider()

    st.header("Welcome")
    st.write("This project was created to help Dr.Hutcheson with researching super family of proteins.")
    st.write("Please select a page from the sidebar to get started.")
    st.write("To find out more about the project or how to use it, follow the 'About' page.")
    st.write("NOTE: prediction takes in a sequence string or fasta file. Please be sure your input follows these guidelines. ")



# main function to run app
def main() -> None:
    cs_sidebar()
    cs_body()
    return None

if __name__ == '__main__':
    main()