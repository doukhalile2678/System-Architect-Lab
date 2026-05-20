processus = [
    {"nom": "P1", "temps": 5},
    {"nom": "P2", "temps": 2},
    {"nom": "P3", "temps": 8}
]

quantum = 2

print("===== ROUND ROBIN =====")

for p in processus:

    temps_restant = p["temps"]

    while temps_restant > 0:

        if temps_restant >= quantum:
            print(p["nom"], "->", quantum, "secondes")
            temps_restant -= quantum

        else:
            print(p["nom"], "->", temps_restant, "secondes")
            temps_restant = 0