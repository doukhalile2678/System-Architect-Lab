processus = [
    {"nom": "P1", "temps": 5},
    {"nom": "P2", "temps": 2},
    {"nom": "P3", "temps": 8}
]

def tri_temps(p):
    return p["temps"]

processus.sort(key=tri_temps)

print("===== SRTF =====")

for p in processus:
    print(p["nom"], "->", p["temps"], "secondes")