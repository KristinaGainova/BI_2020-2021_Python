import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
dataframe = pd.read_csv("C:/bioinformatics_institute/python/population_growth_part.csv",
                        error_bad_lines=False, encoding="ISO-8859-1")
# print(dataframe.head())
country = dataframe.country
year = dataframe.year
population_growth = dataframe.population_growth

colors_list = ['#78C850', '#F08030',  '#6890F0', '#F8D030', '#C03028', '#F85888', '#98D8D8']
plt.figure(figsize=(10, 6))
axes = plt.gca()
axes.xaxis.label.set_size(10)
axes.yaxis.label.set_size(10)

p = sns.violinplot(y=population_growth, x=country, palette=colors_list, linewidth=2, saturation=0.8, notch=True)
sns.swarmplot(x=country, y=population_growth, color="black", alpha=0.8, size=3)
plt.xticks(rotation=15)
plt.xlabel('Countries')
plt.ylabel('Population Growth (annual %) from 1961 to 2019 year')
plt.title(label='Annual population growth rate for year', loc='center',fontsize=25, backgroundcolor='green',
          color='white', fontstyle='italic')
plt.savefig('C:/bioinformatics_institute/python/violinplot.png')
plt.show()
