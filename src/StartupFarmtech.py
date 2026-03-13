voltaFinanceiro = 0
voltaHerbicida1 = 0
voltaPesticida = 0
voltaAplicar = 0
voltaFertilizante = 0


meiodeaplicacao = ''
pesticida = ''
herbicida = ''
fertilizante = ''

areaTotal = 0
lucro = 0
pesoTotal = 0
gastosIniciais = 0

herbicidaqtd = 0
pesticidaqtd = 0
fertilizanteqtd = 0

nome = input("Digite seu nome: ").strip().title()



def financeiro():
    global voltaFinanceiro
    global areaTotal
    global pesoTotal
    global lucro
    while True:
        if voltaFinanceiro == 0:
            areaTotal = int(input("Digite, em hectares, a área total destinada ao plantio de soja: \n"))
            pesoTotal = 3200*areaTotal
            print(
                f"Serão cultivadas {pesoTotal/1000:.1f} ton em {areaTotal} ha," 
                  f"\n ou {pesoTotal*0.94/1000:.1f} ton, contabilizando perdas")
            lucro = 6300*areaTotal
            print(f"{pesoTotal/1000} ton equivale a aproximadamente {lucro:.2f}R$ por safra"
                  f" ou  {lucro*0.94:.2f}R$, contabilizando perdas")
            voltaFinanceiro = 1
            break

        else:
            print(f"Área Total: {areaTotal} ha\n"
                  f"Peso Estimado: {(pesoTotal +(pesoTotal*0.94))/2000:.1f}ton\n"
                  f"Lucro Estimado{(lucro+(lucro*0.94))/2:.2f}R$")
            voltaFinanceiro = 0
            alterar = input("Deseja alterar os dados?: ").upper()

            if alterar == "SIM" or alterar == "S":
                continue
            else:
                break


def herbicidas(): #TELA = 2
    global herbicida
    global voltaHerbicida1
    global herbicidaqtd
    global gastosIniciais
    global areaTotal
    while True:
        if voltaHerbicida1 == 0:
            tipoGrama = int(input("Você possui problemas com:\n[1]- Gramineas Curtas\n"
                                  "[2]-Gramineas Longas\n"))
            if tipoGrama == 1:
                periodo = int(input("Em qual período pretende aplicar?:\n[1]- Entre-safras\n"
                                    "[2]-Outono\n"))
                if periodo == 1:
                    print("Seu herbicida ideal é o Flumioxazin")
                    herbicida = "Flumioxazin"
                    voltaHerbicida1 = 1
                    herbicidaqtd = 80
                    gastosIniciais = gastosIniciais + 3 * herbicidaqtd * areaTotal
                    break
                elif periodo == 2:
                    print("Seu herbicida ideal é o Diclosulam")
                    herbicida = "Diclosulam"
                    voltaHerbicida1 = 1
                    herbicidaqtd = 35
                    gastosIniciais = gastosIniciais + 1.2 * herbicidaqtd * areaTotal
                    break
                else:
                    continue
            elif tipoGrama == 2:
                print("Seu herbicida ideal é o Metsulfuron")
                herbicida = "Metsulfuron"
                herbicidaqtd = 3.5
                gastosIniciais = gastosIniciais + 3.6 * herbicidaqtd * areaTotal 
                voltaHerbicida1 = 1
                break
            else:
                print("==OPÇÃO INVÁLIDA==")
                continue
        elif voltaHerbicida1 == 1:
            print(f"Seu herbicida ideal é o {herbicida}")
            break
            
def pesticidas():        
    global pesticida
    global voltaPesticida
    global pesticidaqtd
    global gastosIniciais
    global areaTotal
    while True:
        if voltaPesticida == 0:
            problema = int(input("Você possui problemas com:\n[1] insetos que atacam vagens\n"
                                 "[2] insetos sugadores\n"))
            if problema == 1:
                print("Seu pesticida ideal é a Lambda-cialotrina!")
                pesticida = " Lambda-cialotrina"
                pesticidaqtd = 40
                gastosIniciais = gastosIniciais + 0.23 * pesticidaqtd * areaTotal
                voltaPesticida = 1
                break
            elif problema == 2:
                print("Seu pesticida ideal é a Imidacloprido!")
                pesticida = " Imidacloprido"
                pesticidaqtd = 150
                gastosIniciais = gastosIniciais + 0.46 * pesticidaqtd * areaTotal
                voltaPesticida = 1
                break
            else:
                print("--OPÇÃO INVÁLIDA--")
                continue
        else:
            print(f"---Seu pesticida ideal é o {pesticida}!---")
            break

def aplicar():
    global voltaAplicar
    global meiodeaplicacao
    global areaTotal
    global gastosIniciais

    while True:
        if voltaAplicar == 0:
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
                gastosIniciais = gastosIniciais + 225000
                voltaAplicar = 1
                break
            elif meio == 2:
                print("--Preço médio do drone: 15.000,00R$--")
                print("O método de aplicação selecionado foi o Drone Agrícola!")
                meiodeaplicacao = "Drone Agrícola"
                gastosIniciais = gastosIniciais + 15000
                voltaAplicar = 1
                break
            else:
                print("OPÇÃO INVÁLIDA")
                continue
        else:
            print(f"O método selecionado foi o {meiodeaplicacao}!")

def fertFunc():        
    global fertilizante
    global voltaFertilizante
    global fertilizanteqtd
    global gastosIniciais
    global areaTotal
    while True:
        if voltaFertilizante == 0:
            problema = int(input("O seu solo possui:\n[1] Ph menor que 6\n"
                                 "[2] Mal otimização da fixação biológica\n"))
            if problema == 1:
                print("Seu fertilizante ideal é o Calcário!")
                fertilizante = " Calcário"
                fertilizanteqtd = 3000
                gastosIniciais = gastosIniciais + 0.104 * fertilizanteqtd * areaTotal
                voltaFertilizante = 1
                break
            elif problema == 2:
                print("Seu fertilizante ideal são os Inoculantes Rhizobium!")
                fertilizante = " Inoculantes Rhizobium"
                fertilizanteqtd = 0.2
                gastosIniciais = gastosIniciais + 130 * fertilizanteqtd * areaTotal
                voltaFertilizante = 1
                break
            else:
                print("--OPÇÃO INVÁLIDA--")
                continue
        else:
            print(f"---Seu fertilizante ideal é o {fertilizante}!---")

def perfil():
    print(f"\n==========BEM VINDO AO SEU PERFIL===========\n====={nome.upper()}=====")
    print(
        f"Área Cultivável: {areaTotal}\nPeso Total: {pesoTotal}kg\n" 
            f"Receita: {lucro}\nHerbicida: {herbicida} + Quantidade:" 
            f"{herbicidaqtd*areaTotal:.1f}g\nPesticida: {pesticida}" 
          f"+ Quantidade {pesticidaqtd*areaTotal:.1f}ml\nMeio de aplicação: {meiodeaplicacao}\n"
          f"Fertilizante {fertilizante} + Quantidade: {fertilizanteqtd*areaTotal:.1f}kg\n"
          f"Gastos iniciais minimos: {gastosIniciais:.2f}R$"
    )
    if herbicida == '':
        herbicida = "N/A"
    if pesticida == '':
        pesticida = "N/A"
    if fertilizante == '':
        fertilizante = "N/A"
    if meiodeaplicacao == '':
        meiodeaplicacao = "N/A"

while True:
    print("=======MENU=======\n")
    tela = int(input("Digite em qual tela você quer entrar: \n[1]- Financeiro \n"
    "[2]- Herbicidas:\n[3]- Pesticidas \n[4]- Meios de Aplicação:\n[5]- Fertilizante\n[6]- Perfil\n[7]- Sair "))

    if tela == 1:
        financeiro()
        continue
    
    elif tela == 2:
        herbicidas()
        continue
    elif tela ==3:
        pesticidas()
        continue
    elif tela ==4:
        aplicar()
        continue
    elif tela ==5:
        fertFunc()
        continue
    elif tela ==6:
        perfil()
    elif tela == 7:
        info = [areaTotal, herbicida, pesticida, fertilizante, meiodeaplicacao, nome] #Alterável e visivel ao usuário
        info2 = [lucro, pesoTotal, herbicidaqtd*areaTotal, pesticidaqtd*areaTotal, gastosIniciais] #Depende dos valores de info e não visiveis
        print(info, info2)
        quit()
    else:
        print("opção inválida")
        continue