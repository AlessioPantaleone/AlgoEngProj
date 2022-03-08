from Imports.myimports import *

df = pandas.read_csv('output.csv')
print(df)

seaborn.set_theme()

seaborn.lineplot(x="Nodes", y="Time", hue="Edges", data=df, linewidth=3, marker="o")
pyplot.show()

seaborn.lineplot(x="Edges", y="Time", hue="Nodes", data=df, linewidth=3, marker="o")
pyplot.show()
