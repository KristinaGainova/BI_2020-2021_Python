
def gen_dna_seq(n):
    nucleotides = ['A', 'T', 'G', 'C']
    for digits in range(1, 1+n):
        for N in range(4 ** digits):
            q = N
            result = ''
            for i in range(digits):
                r = q % 4
                q = q // 4
                result = str(r) + result
            for _ in range(4):
                result = result.replace(str(_), nucleotides[_])
            yield result
