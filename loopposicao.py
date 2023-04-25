import os
os.system("cls")

nomes = ['Maria','Pedro','João']
busca = input("Quem você busca? ")

key = 0
for posicao, item in enumerate(nomes):
    if item == busca:
        key = posicao

if key != 0:
    print("A posição é:", key+1)
else:
    print("Não encontrado")
