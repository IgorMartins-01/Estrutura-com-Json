import json


with open("municipios.json","r", encoding="utf-8") as arquivo:
    cidades = json.load(arquivo)



uf_origem = input("Digite a Uf de origem: ")
uf_destino = input("Digite a Uf de destino: ")
print("Operação | 0: Entrada | 1: Saída")
operacao = int(input("Digite a opereção: "))

estadual = (uf_origem == uf_destino)

cfop = 0

if (estadual) & (operacao == 0):
    cfop = 1
if (estadual) & (operacao == 1):
    cfop = 5
if (not estadual) & (operacao == 0):
    cfop = 2
if (not estadual) & (operacao == 1):
    cfop = 6

#print(f"A operação é {cfop}")

with open("tabela-cfop.json", "r", encoding="utf-8") as arquivo:
    cfops = json.load(arquivo)


cfop_filtrado = [item for item in cfops ["list"] if item["codigo"][0] == str (cfop)]

for cfop_ in cfop_filtrado:
    print(cfop_["codigo"], cfop_["descricao"])