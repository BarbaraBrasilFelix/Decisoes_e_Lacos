tipo_de_prato = input("Informe o tipo de prato (cozido, assado ou frito): ") .upper()
while tipo_de_prato != "COZIDO" and tipo_de_prato != "ASSADO" and tipo_de_prato != "FRITO":
    print ("Digite um tipo de prato válido!")
    tipo_de_prato = input("Informe o tipo de prato (cozido, assado ou frito): ")

gordura = input("Pode ter gordura (sim ou não)? ") .upper()
while gordura != "SIM" and gordura != "NÃO":
    print ("Digite sim ou não!")
    gordura = input("Pode ter gordura (sim ou não)? ") .upper()

nervo = input("Pode ter nervo (sim ou não)? ")
while nervo != "SIM" and nervo != "NÃO":
    print ("Digite sim ou não!")
    nervo = input("Pode ter gordura (sim ou não)? ") .upper()

if tipo_de_prato == "COZIDO":
    if gordura == "SIM" and nervo == "SIM":
        print("O " + tipo_de_prato + " pode ter gordura e nervo.")
    elif gordura == "SIM" and nervo == "NÃO":
        print("O " + tipo_de_prato + " pode ter gordura, mas não pode ter nervo.")
    elif gordura == "NÃO" and nervo == "SIM":
        print("O " + tipo_de_prato + " não pode ter gordura, mas pode ter nervo.")
    else:
        print("O " + tipo_de_prato + " não pode ter gordura nem nervo.")
elif tipo_de_prato == "ASSADO":
    if gordura == "SIM" and nervo == "SIM":
        print("O " + tipo_de_prato + " pode ter gordura e nervo.")
    elif gordura == "SIM" and nervo == "NÃO":
        print("O " + tipo_de_prato + " pode ter gordura, mas não pode ter nervo.")
    elif gordura == "NÃO" and nervo == "SIM":
        print("O " + tipo_de_prato + " não pode ter gordura, mas pode ter nervo.")
    else:
        print("O " + tipo_de_prato + " não pode ter gordura nem nervo.")
elif tipo_de_prato == "FRITO":
    if gordura == "SIM" and nervo == "SIM":
        print("O " + tipo_de_prato + " pode ter gordura e nervo.")
    elif gordura == "SIM" and nervo == "NÃO":
        print("O " + tipo_de_prato + " pode ter gordura, mas não pode ter nervo.")
    elif gordura == "NÃO" and nervo == "SIM":
        print("O " + tipo_de_prato + " não pode ter gordura, mas pode ter nervo.")
    else:
        print("O " + tipo_de_prato + " não pode ter gordura nem nervo.")
else:
    print("Escolha um tipo de prato (cozido, assado ou frito).")