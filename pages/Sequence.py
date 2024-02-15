'''
---App for Bio Informatics Research w/ Dr.Hutcheson---

The sequencing page is where users will go to align and analyze sequences of data. 

Created: 2/12/2024
Author: Shane Matssuhima, Ian Thompson, Austen Furatani
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
    st.sidebar.header("Sequencing")
    

# main body of application  is placed in this function
def cs_body() -> None:
    ...

# main function to run app
def main() -> None:
    cs_sidebar()
    cs_body()
    return None

if __name__ == '__main__':
    main()