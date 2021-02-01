
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

fasta_file = open("C:/bioinformatics_institute/python/genome_Drosophila.fna",'r')
read_length = 0
read_distribution = {}
# k = fasta_file.readline()
for line in fasta_file:
    if line.startswith('>'):
        if read_length == 0:
            continue
        else:
            if read_length not in read_distribution:
                read_distribution[read_length] = 1
            else:
                read_distribution[read_length] += 1
            read_length = 0
            continue
    else:
        read_length += len(line)
else:
    if read_length not in read_distribution:
        read_distribution[read_length] = 1
    else:
        read_distribution[read_length] += 1
    read_length = 0

plt.bar(read_distribution.keys(), read_distribution.values(), color='g')
plt.show()
