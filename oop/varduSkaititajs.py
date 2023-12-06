skaitisanas_vardnica = {}
testa_dati = ["a","b", "a", "c"]

with open("teksts.txt", "r", encoding="utf-8") as fails:
    for rinda in fails:
        dati = rinda.split(" ")
        for vards in dati:
            vards = vards.strip(".,()!?:;\n \"")
            vards = vards.lower()
            if vards in skaitisanas_vardnica.keys():
                skaitisanas_vardnica[vards] += 1
            else:
                skaitisanas_vardnica[vards] = 1

lielakais = ""
lielaka_vertiba = 0

for atslega, vertiba in skaitisanas_vardnica.items():
    if vertiba > lielaka_vertiba:
        lielakais = atslega
        lielaka_vertiba = vertiba

print(lielakais, lielaka_vertiba)