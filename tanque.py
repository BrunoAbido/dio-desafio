tanque = 500
print("Capacidade: ", tanque)

while tanque > 0:
    retirada =  int(input("litros: "))
    if (tanque - retirada < 0):
        print("Capacidade insuficiente")
    else:
    print("Capacidade: ", tanque)


