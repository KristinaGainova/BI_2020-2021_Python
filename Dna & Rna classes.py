from sys import exit

class Nucleic_acids:

    def __init__(self, seq):
        self.nucleic_seq = seq

    def gc_content(self):
        gc_number = 0
        for nucl in self.nucleic_seq:
            if nucl == 'G' or nucl == 'C':
                gc_number += 1
        gc_percent = gc_number / len(self.nucleic_seq) * 100
        return int(gc_percent)

    def iteration(self):
        for i in self.nucleic_seq:
            yield i


class Rna(Nucleic_acids):

    def __init__(self, seq):

        nucleotides = ['A', 'U', 'C', 'G']
        check_seq = False
        for nucl in seq:
            if nucl.upper() not in nucleotides:
                break
        else:
            check_seq = True

        if check_seq == False:
            exit(1)

        self.nucleic_seq = seq.upper()

    def reverse_complement(self):

        rev_complement_seq = ''
        for nucl in self.nucleic_seq:
            if nucl == 'A':
                rev_complement_seq = 'U' + rev_complement_seq
            elif nucl == 'U':
                rev_complement_seq = 'A' + rev_complement_seq
            elif nucl == 'G':
                rev_complement_seq = 'C' + rev_complement_seq
            else:
                rev_complement_seq = 'G' + rev_complement_seq
        return rev_complement_seq

    def __eq__(self, other):
        return isinstance(other, Rna) and self.nucleic_seq == other.nucleic_seq

    def __hash__(self):
        return hash(self.nucleic_seq)


class Dna(Nucleic_acids):

    def __init__(self, seq):
        nucleotides = ['A', 'T', 'C', 'G']
        check_seq = False

        for nucl in seq:
            if nucl.upper() not in nucleotides:
                break
        else:
            check_seq = True

        if not check_seq:
            exit(1)

        self.nucleic_seq = seq.upper()

    def reverse_complement(self):

        rev_complement_seq = ''

        for nucl in self.nucleic_seq:

            if nucl == 'A':
                rev_complement_seq = 'T' + rev_complement_seq

            elif nucl == 'T':
                rev_complement_seq = 'A' + rev_complement_seq

            elif nucl == 'G':
                rev_complement_seq = 'C' + rev_complement_seq

            else:
                rev_complement_seq = 'G' + rev_complement_seq

        return Dna(rev_complement_seq)

    def transcribe(self):
        rna_seq = ''
        for nucl in self.nucleic_seq:
            if nucl == 'T':
                nucl = 'U'
            rna_seq += nucl
        return Rna(rna_seq)

    def __eq__(self, other):
        return isinstance(other, Dna) and self.nucleic_seq == other.nucleic_seq

    def __hash__(self):
        return hash(self.nucleic_seq)


