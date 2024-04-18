import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from Bio.PDB import PDBParser

def plot_protein_structure(pdb_file):
    # Parse the PDB file
    parser = PDBParser()
    structure = parser.get_structure('protein', pdb_file)

    # Initialize lists to store x, y, and z coordinates of atoms
    x_coords = []
    y_coords = []
    z_coords = []

    # Extract coordinates from the structure
    for model in structure:
        for chain in model:
            for residue in chain:
                for atom in residue:
                    coords = atom.get_coord()
                    x_coords.append(coords[0])
                    y_coords.append(coords[1])
                    z_coords.append(coords[2])

    # Convert lists to numpy arrays
    x_coords = np.array(x_coords)
    y_coords = np.array(y_coords)
    z_coords = np.array(z_coords)

    # Plot the 3D structure
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x_coords, y_coords, z_coords, c='b', marker='o')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Protein Structure')
    plt.show()

# Provide the path to your .pdb file
pdb_file = 'path/to/your/protein.pdb'
plot_protein_structure(pdb_file)