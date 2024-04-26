# biopython
from Bio.Blast import NCBIWWW

# first get the sequence we want to parse from a FASTA file
# f_record = next(SeqIO.parse('m_cold.fasta', 'fasta'))

print('Doing the BLAST and retrieving the results...')
query='MTIAFGPVPSRRLGKSLGINSIPCKFCSYDCVYCQVGRTINKTIERREFYSPEDIFKSVEERIGKLNNEKIDYLTFVADGEPTLDINLSKEVEMLRDFDIPIAIITNSSLIWREDVRNDILNFDLVSFKVDSVDEKIWREINRPHKDLVLDKILEGMIAFRDNYKGELITETMILGSIKYTEESIIKTAEFLKELNPNKCYLNTPIRPPSEKYIKPPKIEVITKILAIFNEIIGKNKIKLLGKFEGNEFIFSENVEEDILAITSVHPMREEVIKELLNKSNISFDIINKMVNEGKLIKLEYDGKVFYMKNIKSRDKNVSNP'
result_handle = NCBIWWW.qblast('blastp', 'nr', sequence=query, format_type='Text')

print(result_handle.read())