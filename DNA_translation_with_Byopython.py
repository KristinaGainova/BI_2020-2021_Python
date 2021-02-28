
from Bio.Seq import Seq


def dna_translator(path, table="Standard"):
    with open(path, 'r') as reads:
        sequence = ''
        for line in reads:
            if line.startswith('>'):
                if sequence != '':
                    protein_seq = Seq(sequence).translate(table=table)
                    yield protein_seq
                    sequence = ''
            else:
                sequence += line.rstrip()
        protein_seq = Seq(sequence).translate(table=table)
        yield protein_seq