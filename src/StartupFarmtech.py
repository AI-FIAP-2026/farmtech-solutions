cultura = {
    "Soja": {"area": 0, "peso": 0, "lucro": 0, "gastos": 0,
             "herbicida": "", "pesticida": "",  "fertilizante": "",  
             "PesoHectar": 3200, "ReaisHectar": 6300,
              "herbicidaqtd": 0, "pesticidaqtd": 0, "fertilizanteqtd": 0 },
    "Cafe":   {"area": 0, "peso": 0, "lucro": 0, "gastos": 0,
             "herbicida": "", "pesticida": "",  "fertilizante": "",  
             "PesoHectar": 2300, "ReaisHectar": 72800,
              "herbicidaqtd": 0, "pesticidaqtd": 0, "fertilizanteqtd": 0 }, 
}

flagDados = 0
meiodeaplicacao = ''
gastoTotal = 0
flagCulturas = 0

nome = input("Digite seu nome: ").strip().title()
def calculoAreaTotal():
    global cultura
    return cultura['Soja']['area'] + cultura['Cafe']['area']
def calculoGastoTotal():
    global cultura
    return cultura['Soja']['gastos'] + cultura['Cafe']['gastos']
def price(i,price, quant):
    global cultura
    return cultura[i]['gastos'] + price *  quant * cultura[i]['area']
def financeiro(i):
    global cultura
    while True:
        if cultura[i]['area'] == 0:
            cultura[i]['area'] = calcularArea()
            cultura[i]['peso'] = cultura[i]['PesoHectar']*cultura[i]['area']
            print(
                f"Serão cultivadas {cultura[i]['peso']/1000:.1f} ton em {cultura[i]['area']} ha," 
                f"\n ou {cultura[i]['peso']*0.94/1000:.1f} ton, contabilizando perdas")
            cultura[i]['lucro'] = cultura[i]['ReaisHectar']*cultura[i]['area']
            print(f"{ cultura[i]['peso']/1000} ton equivale a aproximadamente {cultura[i]['lucro']:.2f}R$ por safra"
                f" ou  {cultura[i]['lucro']*0.94:.2f}R$, contabilizando perdas")
            break

        else:
            print(f"Área Total: {cultura[i]['area']} ha\n"
                f"Peso Estimado: {(cultura[i]['peso'] +(cultura[i]['peso']*0.94))/2000:.1f}ton\n"
                f"Lucro Estimado: {(cultura[i]['lucro']+(cultura[i]['lucro']*0.94))/2:.2f}R$")
            alterar = input("Deseja alterar os dados?: ").upper()

            if alterar == "SIM" or alterar == "S":
                cultura[i]['area']
            else:
                break
def herbicidas(i): 
    global cultura
    if i == "Soja":
        while True:
            if cultura['Soja']['herbicida'] == '':
                tipoGrama = int(input("Você possui problemas com:\n[1]- Gramineas Curtas\n"
                                    "[2]-Gramineas Longas\n"))
                if tipoGrama == 1:
                    periodo = int(input("Em qual período pretende aplicar?:\n[1]- Entre-safras\n"
                                        "[2]-Outono\n"))
                    if periodo == 1:
                        print("Seu herbicida ideal é o Flumioxazin")
                        cultura['Soja']['herbicida'] = "Flumioxazin"
                        cultura['Soja']['herbicidaqtd'] = 80
                        cultura['Soja']['gastos'] = price(i,3,cultura['Soja']['herbicidaqtd'])
                        break
                    elif periodo == 2:
                        print("Seu herbicida ideal é o Diclosulam")
                        cultura['Soja']['herbicida'] = "Diclosulam"
                        cultura['Soja']['herbicidaqtd'] = 35
                        cultura['Soja']['gastos'] = price(i,1.2,cultura['Soja']['herbicidaqtd'])
                        break
                    else:
                        continue
                elif tipoGrama == 2:
                    print("Seu herbicida ideal é o Metsulfuron")
                    cultura['Soja']['herbicida'] = "Metsulfuron"
                    cultura['Soja']['herbicidaqtd'] = 3.5
                    cultura['Soja']['gastos'] = price(i,3.6,cultura['Soja']['herbicidaqtd']) 
                    break
                else:
                    print("==OPÇÃO INVÁLIDA==")
                    continue
            else:
                print(f"Seu herbicida ideal é o {cultura['Soja']['herbicida']}")
                break          
    else: #caso i == Café
        while True:
            if cultura['Cafe']['herbicida'] == '':
                tipoGrama = int(input("Você possui problemas com:\n[1]- *Bidens pilosa*\n"
                                    "[2]-*Digitaria insularis*\n"))
                if tipoGrama == 1:
                    print("Seu herbicida ideal é o Flumyzin")
                    cultura['Cafe']['herbicida'] = "Flumyzin"
                    cultura['Cafe']['herbicidaqtd'] = 150
                    cultura['Cafe']['gastos'] = price(i,0.5,cultura['Cafe']['herbicidaqtd']) 
                    break
                elif tipoGrama == 2:
                    print("Seu herbicida ideal é o Cletodim")
                    cultura['Cafe']['herbicida'] = "Cletodim"
                    cultura['Cafe']['herbicidaqtd'] = 450
                    cultura['Cafe']['gastos'] = price(i,0.15,cultura['Cafe']['herbicidaqtd']) 
                    break
                else:
                    print("==OPÇÃO INVÁLIDA==")
                    continue
            else:
                print(f"Seu herbicida ideal é o {cultura['Cafe']['herbicida']}")
                break
def pesticidas(i):        
    global cultura
    if i == "Soja":
        while True:
            if cultura['Soja']['pesticida'] == '':
                problema = int(input("Você possui problemas com:\n[1] insetos que atacam vagens\n"
                                    "[2] insetos sugadores\n"))
                if problema == 1:
                    print("Seu pesticida ideal é a Lambda-cialotrina!")
                    cultura['Soja']['pesticida'] = " Lambda-cialotrina"
                    cultura['Soja']['pesticidaqtd'] = 40
                    cultura['Soja']['gastos'] = price(i,0.23,cultura['Soja']['pesticidaqtd'])
                    break
                elif problema == 2:
                    print("Seu pesticida ideal é a Imidacloprido!")
                    cultura['Soja']['pesticida'] = " Imidacloprido"
                    cultura['Soja']['pesticidaqtd'] = 150
                    cultura['Soja']['gastos'] = price(i,0.46,cultura['Soja']['pesticidaqtd'])
                    break
                else:
                    print("--OPÇÃO INVÁLIDA--")
                    continue
            else:
                print(f"---Seu pesticida ideal é o {cultura['Soja']['pesticida']}!---")
                break
    else: #se i = Café
        while True:
            if cultura['Cafe']['pesticida'] == '':
                problema = int(input("Você possui problemas com:\n[1] Bicho-mineiro do café\n"
                                    "[2]  Ferrugem do cafeeiro\n"))
                if problema == 1:
                    print("Seu pesticida ideal é o Abamectina!")
                    cultura['Cafe']['pesticida'] = "Abamectina"
                    cultura['Cafe']['pesticidaqtd'] = 270
                    cultura['Cafe']['gastos'] = price(i,0.03,cultura['Cafe']['pesticidaqtd'])
                    break
                elif problema == 2:
                    print("Seu pesticida ideal é o Epoxiconazol!")
                    cultura['Cafe']['pesticida'] = " Epoxiconazol"
                    cultura['Cafe']['pesticidaqtd'] = 750
                    cultura['Cafe']['gastos'] = price(i,0.25,cultura['Cafe']['pesticidaqtd'])
                    break
                else:
                    print("--OPÇÃO INVÁLIDA--")
                    continue
            else:
                print(f"---Seu pesticida ideal é o {cultura['Cafe']['pesticida']}!---")
                break
def fertFunc(i):        
    global cultura
    if i == "Soja":
        while True:
            if cultura['Soja']['fertilizante'] == '':
                problema = int(input("O seu solo possui:\n[1] Ph menor que 6\n"
                                    "[2] Mal otimização da fixação biológica\n"))
                if problema == 1:
                    print("Seu fertilizante ideal é o Calcário!")
                    cultura['Soja']['fertilizante'] = " Calcário"
                    cultura['Soja']['fertilizanteqtd'] = 3000
                    cultura['Soja']['gastos'] = price(i,0.104,cultura['Soja']['fertilizanteqtd'])
                    break
                elif problema == 2:
                    print("Seu fertilizante ideal são os Inoculantes Rhizobium!")
                    cultura['Soja']['fertilizante'] = " Inoculantes Rhizobium"
                    cultura['Soja']['fertilizanteqtd'] = 0.2
                    cultura['Soja']['gastos'] = price(i,130,cultura['Soja']['fertilizanteqtd'])
                    break
                else:
                    print("--OPÇÃO INVÁLIDA--")
                    continue
            else:
                print(f"---Seu fertilizante ideal é o {cultura['Soja']['fertilizante']}!---")
    else:
        while True:
            if cultura['Cafe']['fertilizante'] == '':
                problema = int(input("O seu solo precisa de adubo:\n[1] NPK\n"
                                    "[2] A base de magnésio\n"))
                if problema == 1:
                    print("Seu fertilizante ideal é o Adubo NPK!")
                    cultura['Cafe']['fertilizante'] = "NPK"
                    cultura['Cafe']['fertilizanteqtd'] = 600
                    cultura['Cafe']['gastos'] = price(i,8,cultura['Cafe']['fertilizanteqtd'])
                    break
                elif problema == 2:
                    print("Seu fertilizante ideal é o Magnésio!")
                    cultura['Cafe']['fertilizante'] = "Magnesio"
                    cultura['Cafe']['fertilizanteqtd'] = 80
                    cultura['Cafe']['gastos'] = price(i,7.9,cultura['Cafe']['fertilizanteqtd'])
                    break
                else:
                    print("--OPÇÃO INVÁLIDA--")
                    continue
            else:
                print(f"---Seu fertilizante ideal é o {cultura['Cafe']['fertilizante']}!---")
def perfil(i):
    print(f"\n==========BEM VINDO AO SEU PERFIL===========\n====={nome.upper()}=====")
    print(f"\n=========={i}===========")
    print(
        f"Área Cultivável: {cultura[i]['area']}\nPeso Total: {cultura[i]['peso']}kg\n" 
            f"Receita: {cultura[i]['lucro']}\nHerbicida: {cultura[i]['herbicida']} + Quantidade:" 
            f"{cultura[i]['herbicidaqtd']*cultura[i]['area']:.1f}g\nPesticida: {cultura[i]['pesticida']}" 
        f"+ Quantidade {cultura[i]['pesticidaqtd']*cultura[i]['area']:.1f}ml\n"
        f"Fertilizante {cultura[i]['fertilizante']} + Quantidade: {cultura[i]['fertilizanteqtd']*cultura[i]['area']:.1f}kg\n"
        f"Gastos iniciais minimos: {cultura[i]['gastos']:.2f}R$"
    )
def calcularArea():
    print("\n---- Calculadora de Área ----")
    while True:
        forma = int(input("[1] Retângulo\n[2] Triângulo\n[3] Círculo\n"))
        if forma == 1:
            try:
                largura = float(input("Digite o valor da largura em ha: "))
                comprimento = float(input("Digite o valor do comprimento em ha: "))
            except ValueError:
                print("Entrada inválida")
                continue
            return largura*comprimento
        elif forma == 2:
            try:
                base = float(input("Digite o valor da base em ha: "))
                altura = float(input("Digite o valor da altura em ha: "))
            except ValueError:
                print("Entrada inválida")
                continue
            return base*altura/2
        elif forma == 3:
            try:
                raio = float(input("Digite o valor do raio em ha:  "))
            except ValueError:
                print("Entrada inválida")
                continue
            return raio*raio*3.14
        else:
            print("Entrada inválida")
            continue
def menu(i):
    
    print(f"=======MENU {i}=======\n")
    tela = int(input("Digite em qual tela você quer entrar: \n[1]- Financeiro \n"
    "[2]- Herbicidas:\n[3]- Pesticidas \n[4]- Fertilizante\n[5]- Perfil\n"))
    match tela:
        case 1:
            financeiro(i)
        case 2:
            herbicidas(i)
        case 3:
            pesticidas(i)
        case 4:
            fertFunc(i)
        case 5:
            perfil(i)
        case _:
            print("opção inválida")
def preenchido(i):
    return (
        cultura[i]["area"] != 0 and
        cultura[i]["herbicida"] != "" and
        cultura[i]["pesticida"] != "" and
        cultura[i]["fertilizante"] != "" 
    )

    
for i in cultura: 
    while not preenchido(i):
        menu(i)
    print(f"=====Você digitou todos os dados de {i}======")
    print(perfil(i))

    
areaTotal = calculoAreaTotal()
gastoTotal = calculoGastoTotal()
def aplicar(): # tirar do loop for
    global cultura
    global gastoTotal
    global areaTotal
    global meiodeaplicacao
    while True:
        meio = int(input("Digite o meio de aplicação dos defensivos agrícolas preferido:" 
        "\n[1]Pulverizador tratorizado\n[2]Drone agrícola"))
        if meio == 1:
            print("--Preço médio do trator: 225.000,0R$--")
            print(
                f"Área inicial: {areaTotal} ha\nÁrea destinada ao trator: {areaTotal*0.12:.1f} ha"
                f"\nÁrea Final: {areaTotal*0.88:.1f} ha")
            print("O método de aplicação selecionado foi o Pulverizador Tratorizado!")
            meiodeaplicacao = "Pulverizador Tratorizado"
            areaTotal = areaTotal*0.88
            gastoTotal = gastoTotal + 225000
            break
        elif meio == 2:
            print("--Preço médio do drone: 15.000,00R$--")
            print("O método de aplicação selecionado foi o Drone Agrícola!")
            meiodeaplicacao = "Drone Agrícola"
            gastoTotal = gastoTotal + 15000
            break
        else:
            print("OPÇÃO INVÁLIDA")
            continue

aplicar()

print(cultura, f"\nGasto Total: {gastoTotal}\nArea Aproximada: {areaTotal}")

    
    
    
 
    



    