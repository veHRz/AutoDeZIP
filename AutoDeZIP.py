import sys
import os
import ast

def __afficherAide():
    print("Voici l'aide.")

def __zipperStr(__str : str):
    __zipperList([__str])

def __zipperDict(__dict: dict, __cheminActuel: str):
    pass

def __zipperList(__list: list):
    global __dictFichier
    __dictFichier["___files___"] = {}
    for fichier in __list:
        if not os.path.isfile(fichier):
            print("Le fichier '" + fichier + "' n'existe pas ou n'est pas un fichier.")
            exit()
        __dictFichier["___files___"][fichier] = open(fichier, 'r', encoding='utf-8').read()

def __reunirArgs(__args: list):
    __str = ""
    for arg in __args:
        __str += arg
    return __str

__chemin = '.'
__contenuFichier = """import sys, os

def __dezipper(__dict: dict, __cheminActuel: str):
    for dossier in __dict.keys():
        if dossier == "___files___":
            for fichier in __dict[dossier].keys():
                open(__cheminActuel+"/"+fichier, 'w', encoding="utf-8").write(__dict[dossier][fichier])
        else:
            if not os.path.isdir(__cheminActuel+"/"+dossier):
                os.mkdir(__cheminActuel+"/"+dossier)
            __dezipper(__dict[dossier], __cheminActuel+"/"+dossier)

__chemin = "."
if len(sys.argv) > 1:
    __chemin = sys.argv[1]
    if not os.path.exists(__chemin):
        print("Le chemin '" + __chemin + "' n'est pas un chemin valide.")
        exit()
__contenuFichier = {None : None}
__dezipper(__contenuFichier, __chemin)"""
__dictFichier = {}
if len(sys.argv) > 1:
    if sys.argv[1] in ("h", "help", "-h", "-help", "/h", "/help"):
        __afficherAide()
        exit()
    # if type(ast.literal_eval(sys.argv[1])) == type({'': ""}):
    #     __zipperDict(ast.literal_eval(sys.argv[1]), __chemin)
    __arg = __reunirArgs(sys.argv[1:])
    if type(ast.literal_eval(__arg)) == type([]):
        __zipperList(ast.literal_eval(__arg))
    else:
        __zipperStr(__arg)
    __contenuFichier = __contenuFichier.replace("{None : None}", str(__dictFichier))
    print(__contenuFichier)
    open("AutoDeZIPAvecFichiers.py", 'w', encoding='utf-8').write(__contenuFichier)
else:
    __afficherAide()
