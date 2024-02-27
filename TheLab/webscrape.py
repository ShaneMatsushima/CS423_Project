# test for webscraping amino acid sequence from ncbio database

# scraping sequences from NCBI database
# utilizing https://www.youtube.com/watch?v=XiWcXUS15fI tutorial
from Bio import Entrez
from Bio import SeqIO

#set email
Entrez.email = "matsushs23@up.edu"

handle = Entrez.efetch(db='protein', id='AAB99319.1', rettype='fasta')

print(handle.read())