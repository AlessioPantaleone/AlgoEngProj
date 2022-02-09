from Imports.myimports import *

df = pandas.read_csv('output.csv')
print(df)

seaborn.set_theme()

seaborn.lineplot(x="", y="", style="", hue="", data=df, linewidth=3, marker="o")
pyplot.show()

seaborn.lineplot(x="", y="", style="", hue="", data=df, linewidth=3, marker="o")
pyplot.show()