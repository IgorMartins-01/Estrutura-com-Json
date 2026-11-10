import json

with open("pokedex.json", "r", encoding= "utf-8") as arquivo:
    pokedex = json.load(arquivo)

# for pokemon in pokedex:
#     if pokemon ["name"]["english"] == "Mew":
#         print(pokemon)

poke = str(input("Digite o nome do Pokemon em inglês: "))

for pokemon in pokedex:
    if poke == pokemon["name"]["english"]:
        print(pokemon)

else:
    print("pokemon não encontrado.")