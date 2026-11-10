import json

with open("municipios.json","r", encoding="utf-8") as arquivo:
    cidades = json.load(arquivo)

uf = input("Digite a UF: ")

cidades_mt = [item for item in cidades["data"] if item ["Uf"] == uf]

for cidade in cidades_mt :
    print(cidade["Nome"], cidade ["Uf"])