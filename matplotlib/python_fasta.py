
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

fasta_file = open("C:/bioinformatics_institute/python/file.fa",'r')
read_length = 0
read_distribution = {}
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

df = pd.DataFrame(list(read_distribution.items()),columns = ['column1','column2'])
step = int(max(read_distribution.keys()) - min(read_distribution.keys())) * 0.05

# Plot
p = plt.bar(df['column1'],df['column2'],align='center', width=2.5, color = sns.color_palette("Blues_d"), edgecolor="k", linewidth=.5)
plt.xticks(np.arange(min(read_distribution.keys()), max(read_distribution.keys()), step))
plt.title('Read length distribution from fasta file', fontsize=15, fontweight='bold', color = 'black')
plt.xlabel('Read length', labelpad=10, fontsize=14)
plt.ylabel('Number of reads with this length', labelpad=10, fontsize=14)
plt.grid(True)

plt.savefig('C:/bioinformatics_institute/python/read_distribution.png')
plt.show()
