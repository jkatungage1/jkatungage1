import os


# print (f""" Le chemin du script est {sys.argv[0]} ou aussi {__file__}""")

os.system('cls')
mydict = {'george': 16, 'amber': 19}
print (list(mydict.keys())[list(mydict.values()).index(16)])