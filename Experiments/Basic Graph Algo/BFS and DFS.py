from Imports.myimports import *

ERDOSGRAPH = networkit.generators.ErdosRenyiGenerator(200, 0.2).generate()
networkit.overview(ERDOSGRAPH)

"""
Obviously incomplete
"""