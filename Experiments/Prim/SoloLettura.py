from Imports.myimports import *
# Lettura dei dati con pandas
df = pandas.read_csv('output.csv')
print(df)

seaborn.set(style="ticks", color_codes=True)
seaborn.lineplot(x="n", y="tempo", style="hfm", data=df, linewidth=2)
pyplot.show()

seaborn.lineplot(x="m", y="tempo", style="hfn", data=df, linewidth=2)
pyplot.show()