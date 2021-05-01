import unittest
import Dna_Rna_classes

class RNAClassTests(unittest.TestCase):

    def test_init(self):
        with self.assertRaises(SystemExit) as cm:
            Dna_Rna_classes.Rna('AGccGCTTttUAGC')
        self.assertEqual(cm.exception.code, 1)  # check exception if input string is incorrect

    def test_reverse_complement(self):
        rna1 = Dna_Rna_classes.Rna('AGUGCUAGC')
        self.assertEqual(rna1.reverse_complement(), 'GCUAGCACU')
        self.assertNotEqual(rna1.reverse_complement(), 'gcuagcacu')

    def test_gc_content(self):
        rna = Dna_Rna_classes.Rna('AGUC')
        self.assertEqual(rna.gc_content(), 50)


class DNAClassTests(unittest.TestCase):

    def test_init(self):
        with self.assertRaises(SystemExit) as cm:
            Dna_Rna_classes.Dna(' ')
        self.assertEqual(cm.exception.code, 1)  # check exception if input string is incorrect

        with self.assertRaises(SystemExit) as cm:
            Dna_Rna_classes.Dna('AGccGCTTttUAGC')
        self.assertEqual(cm.exception.code, 1)

    def test_reverse_complement(self):
        dna1 = Dna_Rna_classes.Dna('ATGGGCTAGCTAGCATGGGCATCTTCTAGGGATCG')
        self.assertEqual(dna1.reverse_complement(),  Dna_Rna_classes.Dna('CGATCCCTAGAAGATGCCCATGCTAGCTAGCCCAT'))

    def test_transcribe(self):
        dna = Dna_Rna_classes.Dna('AGTC')
        self.assertEqual(dna.transcribe(), Dna_Rna_classes.Rna('AGUC'))

    def test_gc_content(self):
        dna = Dna_Rna_classes.Dna('A')
        self.assertEqual(dna.gc_content(), 0)

if __name__ == '__main__':
    unittest.main()
