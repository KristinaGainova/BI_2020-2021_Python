
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:\\bioinformatics_institute\\python\\homework\\pandas\\train.csv', sep=',')
pd.set_option('display.max_columns', None) # need to get all columns when use df.head

colA_rowIndex = df[df['A'].isnull()].index.tolist()
colT_rowIndex = df[df['T'].isnull()].index.tolist()
colC_rowIndex = df[df['C'].isnull()].index.tolist()
colG_rowIndex = df[df['G'].isnull()].index.tolist()

# replace Na in column '_fraction'
for _ in colA_rowIndex:
    df.loc[_, 'A_fraction'] = 1 - df.loc[_, 'C_fraction'] - df.loc[_, 'G_fraction'] - df.loc[_, 'T_fraction']
for _ in colT_rowIndex:
    df.loc[_, 'T_fraction'] = 1 - df.loc[_, 'C_fraction'] - df.loc[_, 'G_fraction'] - df.loc[_, 'A_fraction']
for _ in colC_rowIndex:
    df.loc[_, 'C_fraction'] = 1 - df.loc[_, 'T_fraction'] - df.loc[_, 'G_fraction'] - df.loc[_, 'A_fraction']
for _ in colG_rowIndex:
    df.loc[_, 'G_fraction'] = 1 - df.loc[_, 'T_fraction'] - df.loc[_, 'C_fraction'] - df.loc[_, 'A_fraction']

plotdata = df[['pos', 'A_fraction', 'T_fraction', 'C_fraction', 'G_fraction']]
plotdata = plotdata.set_index('pos')


# Plotting of stacked barplot
plotdata.plot.bar(stacked=True)
plt.title("Frequency of occurrence of nucleotides in different positions of read", fontweight='bold')
plt.xlabel("Position in read")
plt.ylabel("Nucleotide frequency")
plt.legend(bbox_to_anchor=(1, 1))
plt.show()


# Dataframe filtering. Save new df to csv file
filter_matches = df['matches'] > df['matches'].mean()
new_df = df[filter_matches]
new_df = new_df[['pos', 'reads_all', 'mismatches', 'deletions', 'insertions']]
new_df.to_csv('C:\\bioinformatics_institute\\python\\homework\\pandas\\train_part.csv', sep=',')
