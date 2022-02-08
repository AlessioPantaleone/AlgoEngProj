from Imports.myimports import *

df = pandas.read_csv('output.csv')
print(df)

seaborn.set_theme()

seaborn.relplot(x="m", y="tempo", style="hfm", data=df, linewidth=3)
pyplot.show()