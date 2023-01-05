import sys, os

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
__dezipper(__contenuFichier, __chemin)