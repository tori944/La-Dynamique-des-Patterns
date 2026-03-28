"""Charge un jeu de tuiles sepuis un fichier."""

import csv


def charger_compatibilites(fname: str):
    """Charge les compatibilités depuis un fichier."""
    compatibilites = []
    with open(fname, "r") as file:
        reader = csv.DictReader(file, delimiter=";")
        for line in reader:
            compatibilites.append(
                [
                    int(line["Haut"]),
                    int(line["Bas"]),
                    int(line["Gauche"]),
                    int(line["Droite"]),
                ]
            )
    return compatibilites


def enregistrer_compatibilites(compatibilites: list[list[int]], fname: str):
    """Enregistre les compatibilités dans un fichier au format CSV."""
    with open(fname, "w") as f:
        writer = csv.DictWriter(f, fieldnames=["Haut", "Bas", "Gauche", "Droite"], delimiter=",", lineterminator="\n")
        writer.writeheader()
        writer.writerows(
            [
                {
                    "Haut": x[0],
                    "Bas": x[1],
                    "Gauche": x[2],
                    "Droite": x[3],
                }
                for x in compatibilites
            ]
        )

c = charger_compatibilites("tilesets/default.csv")
enregistrer_compatibilites(c, "tilesets/test.csv")
x = 0
breakpoint()

# Une fois dans le breakpoint :
# - afficher des variables
# - n : avance d'une seule ligne
# - c : continue le programme
# - q : quitte le breakpoint ET le programme
# - (interact : passer en mode interactif)
