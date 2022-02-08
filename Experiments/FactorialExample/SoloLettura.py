from Imports.myimports import *
# Lettura dei dati con pandas
df = pandas.read_csv('experiment')
print(df)

seaborn.set(style="ticks", color_codes=True)

seaborn.lineplot(x="F1", y="Time", style="hF2", hue="hF3", data=df, linewidth=3)
pyplot.show()

seaborn.lineplot(x="F2", y="Time", style="hF1", hue="hF3", data=df, linewidth=3)
pyplot.show()

seaborn.lineplot(x="F3", y="Time", style="hF1", hue="hF2", data=df, linewidth=3)
pyplot.show()
