from Imports.myimports import *

df = pandas.read_csv('output.csv')
print(df)

seaborn.set_theme()

seaborn.lineplot(x="n", y="Time", style="HFE", data=df, linewidth=3, marker="o")
pyplot.show()

seaborn.lineplot(x="e", y="Time", style="HFN", data=df, linewidth=3, marker="o")
pyplot.show()