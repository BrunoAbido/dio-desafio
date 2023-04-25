import os
while True:
    os.system("cls")
    usuario = input("user: ")
    senha = input("pass: ")
    if usuario == "imed" and senha == "098":
        break
    else:
        print("Usuário ou senha invalidos")
    print("Aperte qualquer botão para continuar")

    
print("Bem-vindo")