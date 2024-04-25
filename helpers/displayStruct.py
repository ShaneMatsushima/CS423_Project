import py3Dmol

# Load the PDB file

def displayStruct(filename):
    
    # Create a Py3Dmol view object
    
    # Add the structure to the view
    view = py3Dmol.view(js='https://3dmol.org/build/3Dmol.js',)
    pdb_file = open(filename, 'r').read()
    view.addModel(pdb_file, 'pdb')

    view.setStyle({'cartoon': {'color': 'spectrum'}})
    view.setBackgroundColor('white')
    view.zoomTo()
    view.write_html(f'viewer.html')
    with open('viewer.html', "r") as f:
            html_content = f.read()
#     # print(x)
#     import webbrowser
#     webbrowser.open('viewer.html')
    return html_content

