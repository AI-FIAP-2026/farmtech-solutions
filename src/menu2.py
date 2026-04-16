import math
import os
import subprocess
import shutil
from dataclasses import dataclass, field
from typing import Optional

import pandas as pd

# Caracteres ANSI para estilização no terminal
CYAN = "\033[96m"
VERDE = "\033[92m"
AMARELO = "\033[93m"
AZUL = "\033[94m"
VERMELHO = "\033[91m"
NEGRITO = "\033[1m"
RESET = "\033[0m"




ToneladaPorHectar = 75#
ReaisPorTonelada = 150 #

area: float = 0.0
peso_total: float = 0.0
receita: float = 0.0
lucro: float = 0.0
gastos: float = 0.0
metodo_colheita: str = "N/A"
gps_ativo: bool = False
perda_percentual: float = 0.0
perda_peso: float = 0.0
perda_rs: float = 0.0
prazo_de_colheita: float = 0.0


def find_rscript():
    """Encontra o caminho do Rscript automaticamente."""
    rscript = shutil.which("Rscript")
    if rscript:
        return rscript
    # Fallback para caminhos comuns
    common_paths = [
        r"C:\Program Files\R\R-4.5.3\bin\RScript.exe",
        r"C:\Program Files\R\R-4.4.0\bin\RScript.exe",
        r"C:\Program Files\R\R-4.3.0\bin\RScript.exe",
        r"C:\R\bin\RScript.exe"
    ]
    for path in common_paths:
        if os.path.exists(path):
            return path
    return None

def exportar_csv() -> None:
    global area, peso_total, metodo_colheita, gastos, lucro
    """Exporta dados de plantio e insumos para CSV."""
    if area == 0 or peso_total == 0:
        print(
            f"{VERMELHO}Não há dados válidos para exportação. Cadastre os dados primeiro!.{RESET}")
        return

    registros = [] #Dados que serão analisados
    registros.extend([
        {"area": area, "colheita": metodo_colheita, "perda_peso": perda_peso, "gastos": gastos,
         "lucro": lucro}
    ])

    if not registros:
        print(f"{VERMELHO}Não há dados válidos para exportação.{RESET}")
        return

    #Transforma dados em data frame
    df = pd.DataFrame(registros)
    #Verifica se o arquivo existe
    arquivo_existe = os.path.exists(nome_arquivo)
    #se o arquivo não existir = not False = True -> Ele adiciona o cabeçalho, caso contrario
    #ele apenas append as informações
    df.to_csv(nome_arquivo, mode='a', index=False, header=not arquivo_existe, encoding="utf-8-sig")
    nome_arquivo = "dados_plantio.csv"
    df.to_csv(nome_arquivo, index=False, encoding="utf-8-sig")
    print(f"{VERDE}CSV exportado: {nome_arquivo}{RESET}")

def consultar_previsao_tempo() -> None:
    """Executa o script previsao_do_tempo.r com cidade escolhida pelo usuário."""
    cidade = input(
        f"{AZUL}Digite o nome da cidade para consulta do tempo: {RESET}").strip()
    if not cidade:
        print(f"{AMARELO}Cidade não informada. Usando São Paulo como padrão.{RESET}")
        cidade = "São Paulo"

    rscript_path = find_rscript()
    if not rscript_path:
        print(
            f"{VERMELHO}Rscript não encontrado. Instale R ou adicione ao PATH.{RESET}")
        return

    try:
        resultado = subprocess.run(
            [rscript_path, "previsao_do_tempo.r", cidade], capture_output=True, text=True, check=True)
        print(f"{VERDE}== Previsão do tempo (R) =={RESET}")
        print(resultado.stdout)
    except subprocess.CalledProcessError as exc:
        print(f"{VERMELHO}Erro ao executar R: {exc.stderr}{RESET}")
    except FileNotFoundError:
        print(f"{VERMELHO}Rscript não encontrado.{RESET}")

def executar_estatisticas_r() -> None:
    """Executa script estatisticas_basicas.r com dados exportados."""
    arquivo = "dados_plantio.csv"
    if not os.path.exists(arquivo):
        print(
            f"{VERMELHO}Arquivo dados_plantio.csv não encontrado. Exporte antes.{RESET}")
        return

    rscript_path = find_rscript()
    if not rscript_path:
        print(
            f"{VERMELHO}Rscript não encontrado. Instale R ou adicione ao PATH.{RESET}")
        return

    try:
        resultado = subprocess.run(
            [rscript_path, "estatisticas_basicas.r"], capture_output=True, text=True, check=True)
        print(f"{VERDE}== Estatísticas (R) =={RESET}")
        print(resultado.stdout)
    except subprocess.CalledProcessError as exc:
        print(f"{VERMELHO}Erro ao executar R: {exc.stderr}{RESET}")
    except FileNotFoundError:
        print(f"{VERMELHO}Rscript não encontrado.{RESET}"),

def validar_area(area: float):
    minimo = 100
    maximo = 1.52e12 
    sim = ["S", "SI", "SIM", "SS"]
    nao = ["N", "NA", "NAO", "NN"]
    try:
        if area < minimo:
             raise ValueError(f"Valor deve ser maior ou igual a 100m².")
        elif area > maximo:
            confirm = input(f"{AZUL}O valor digitado está correto? [S]im, [N]ao{RESET}").strip().upper()
            if confirm in sim:
                return area
            elif confirm in nao:
                return None
            else:
                return None
        return area
    except ValueError as exc:
        print(f"{VERMELHO}Entrada inválida: {exc}. Tente novamente.{RESET}")

def validar_float(mensagem: str, minimo: float = 0.0) -> float:
    """Solicita um float validado ao usuário."""
    while True:
        try:
            valor = float(
                input(f"{AZUL}{mensagem}{RESET}").replace(",", ".").strip())
            if valor < minimo:
                raise ValueError(f"Valor deve ser maior ou igual a {minimo}.")
            return valor
        except ValueError as exc:
            print(f"{VERMELHO}Entrada inválida: {exc}. Tente novamente.{RESET}")

def validar_int(mensagem: str, opcoes: Optional[list] = None) -> int:
    """Solicita um inteiro validado ao usuário."""
    while True:
        try:
            valor = int(input(f"{AZUL}{mensagem}{RESET}").strip())
            if opcoes and valor not in opcoes:
                raise ValueError(f"Escolha uma das opções: {opcoes}.")
            return valor
        except ValueError as exc:
            print(f"{VERMELHO}Entrada inválida: {exc}. Tente novamente.{RESET}")

def calcular_area() -> None:
    global area, ToneladaPorHectar, peso_total
    """Calcula a área plantada com base na cultura."""
    comprimento = validar_float("Comprimento (m): ", 0.01)
    largura = validar_float("Largura (m): ", 0.01)
    area_calculada = comprimento * largura
    area_validade = validar_area(area_calculada)
    if area_validade is not None:
        area = area_validade
    else:
        print(f"{VERMELHO}Gravação cancelada. Insira os dados novamente.{RESET}")
    print(f"{VERDE}Área do planío de cana (retângulo): {area:.2f} m²{RESET}") 
    hectares = area / 10000.0
    peso_total = ToneladaPorHectar * hectares

def exibir_comparativo_colheita():
    print(f"\n{NEGRITO}{AMARELO}=== TABELA COMPARATIVA DE COLHEITA ==={RESET}")

    # Bloco MANUAL
    print(f"\n{NEGRITO}MANUAL:{RESET}")
    print(f"Capacidade Operacional : {CYAN}0,3 Toneladas / Hora{RESET}")
    print(f"Custo                  : {CYAN}30$ / hora (salario){RESET}")
    print(f"Perda Estimada (%)     : {CYAN}5%{RESET}")
    print(f"Perda Estimada (R$)    : {VERDE}R$ {peso_total * 0.05 * ReaisPorTonelada:.2f}{RESET}")
    print(f"Perda Estimada (kg)    : {VERDE}{peso_total * 0.05 * 1000:.2f} kg{RESET}")
    print(f"Prazo de colheita      : {AMARELO}8 dias{RESET}")
    
    print(f"-" * 40)

    # Bloco MECÂNICA
    print(f"{NEGRITO}MECANICA:{RESET}")
    print(f"Capacidade Operacional : {CYAN}50 Toneladas / hora{RESET}")
    print(f"Custo (Diesel)         : {CYAN}40L/h (240R$/h){RESET}")
    print(f"Custo (Manutenção)     : {CYAN}240R$/h{RESET}")
    print(f"Perda Estimada (%)     : {CYAN}15%{RESET}")
    print(f"Perda Estimada (R$)    : {VERDE}R$ {peso_total * 0.15 * ReaisPorTonelada:.2f}{RESET}")
    print(f"Perda Estimada (kg)    : {VERDE}{peso_total * 0.15 * 1000:.2f} kg{RESET}")
    print(f"Prazo de colheita      : {AMARELO}36 horas{RESET}")

    print(f"{AMARELO}{'-' * 40}{RESET}\n")

def definir_meio_colheita() -> None:
    global metodo_colheita, gps_ativo
    """Seleciona método de colheita e atualiza gastos."""
    if metodo_colheita == "N/A":
        exibir_comparativo_colheita()
        print()
        print(f"{AZUL}Escolha o método de colheita: {RESET}")

        tipo = validar_int("[1] MANUAL, [2] MECÂNICA: ", [1, 2])
        if tipo == 1:
            metodo_colheita = "MANUAL"
        else:
            metodo_colheita = "MECÂNICA"
            gps_ativo = perks()

        print(
            f"Método de colheita: {metodo_colheita}")
    else:
        print(
            f"Método de colheita escolhido foi: {metodo_colheita}")
        

def calcular_financeiro() -> None:
    """Calcula produção e lucro estimado."""
    global area, lucro, receita, gastos, peso_total, ToneladaPorHectar
    global perda_peso, perda_rs
    if area <= 0:
        print("Área inválida para cálculo financeiro.")
        return

    hectares = area / 10000
    peso_bruto_inicial = ToneladaPorHectar * hectares

    calcular_perdas(peso_bruto_inicial)
    gastos = calcular_gastos()
    receita = (ReaisPorTonelada* ToneladaPorHectar * hectares) - perda_rs #11250 = R$ por Hectar
    peso_total = peso_bruto_inicial - perda_peso
    lucro = receita - gastos
    print(f"Receita estimada: R$ {receita:.2f}")
    print(f"Lucro estimado (com perdas): R$ {lucro:.2f}")
    print(f"Peso estimado (com perdas): {peso_total:.2f} ton")
    
def atualizar_dados() -> None:
    global area, peso_total, metodo_colheita
    """Atualiza os dados de cultura, área e insumos do plantio."""
    if area == 0:
        print(f"{VERMELHO}PREENCHA A ÁREA PRIMEIRO!.{RESET}")
        return

    print("\n=== Atualização de Dados ===")

    print("\n1 - Alterar metodo de colheita")
    print("2 - Alterar área")
    print("0 - Voltar")

    opcao = validar_int("Escolha opção de atualização: ", [0, 1, 2])

    if opcao == 1:
        metodo_colheita = "N/A"
        definir_meio_colheita()  # Isso vai sobrescrever o metodo ativo
    elif opcao == 2:
        calcular_area()
    else:
        print(f"{AZUL}Retornando ao menu principal.{RESET}")

def calcular_perdas(a) -> None:
    global perda_peso, perda_rs, perda_percentual
    global ReaisPorTonelada
    if metodo_colheita == "MANUAL":
        perda_percentual = 0.05
        peso_bruto = (area / 10000) * ToneladaPorHectar
        perda_peso = peso_bruto * perda_percentual
        perda_rs = perda_peso *ReaisPorTonelada
    elif metodo_colheita == "MECÂNICA":
        if gps_ativo:
            perda_percentual = 0.11
            peso_bruto = (area / 10000) * ToneladaPorHectar
            perda_peso = peso_bruto * perda_percentual  
            perda_rs = perda_peso *ReaisPorTonelada
        elif not gps_ativo:
            perda_percentual = 0.15
            peso_bruto = (area / 10000) * ToneladaPorHectar
            perda_peso = peso_bruto * perda_percentual  
            perda_rs = perda_peso *ReaisPorTonelada

def calcular_gastos() -> float:
    global peso_total, metodo_colheita, gps_ativo
    if metodo_colheita == "MECÂNICA":
        extra = 0
        if gps_ativo:
            extra = 8000 #custo pelo kit do GPS
        #1 Parametros Básicos
        prazo = 36 #Horas para concluir a colheita
        produtividade_hora = 50  # toneladas por hora
        jornada_diaria = 8 #Horas trabalhadas por dia
        #2 Esforço real em 1 dia
        dias_totais = prazo/jornada_diaria #Quantos dias deve trabalhar
        horas_totais = dias_totais * jornada_diaria #Quantas horas deve trabalhar
        produtividade = produtividade_hora * horas_totais #Quanto realmente produzirá em 1 dia
        #3 Frota
        quantidade = math.ceil(peso_total / produtividade) # quantas maquinas
        #4 Custo
        custo_operacional_total = (peso_total/produtividade_hora) *480  #480 = gasolina e manutenção/hora
        custo_aquisicao = quantidade * 5000 #Preço de locação de 1 maquinário
        custoTotal = custo_operacional_total + custo_aquisicao + extra
    elif metodo_colheita == "MANUAL":
        #1 Parametros Básicos
        prazo = 192 # Horas para concluir a colheita
        produtividade_hora = 0.3  # Toneladas por hora   
        jornada_diaria = 8 # Horas trabalhadas por dia
        #2 Esforço real em 1 dia
        dias_totais = prazo/jornada_diaria #Quantos dias deve trabalhar
        horas_totais = dias_totais * jornada_diaria #Quantas horas deve trabalhar
        produtividade = produtividade_hora * horas_totais #Quanto realmente produzirá em 1 dia
        #3 Frota
        quantidade = math.ceil(peso_total / produtividade) # quantos trabalhadores
        #4 Custo
        custo_operacional_total = (peso_total/produtividade_hora) * 30  # R$ por hora (trabalhador)
        custoTotal = custo_operacional_total
        
    print(f"\n{NEGRITO}LOGÍSTICA {metodo_colheita}:{RESET}")
    print(f"Quantidade necessárias: {quantidade}")
    print(f"Custo de operação: R$ {custoTotal:.2f}")
    return custoTotal

def perks() -> None:
    global area
    """Melhorias para diminuir a perda da colheita"""
    if area == 0:
        print(f"{VERMELHO}Cadastre uma área de plantio primeiro!{RESET}")
        return
    print(f"{AZUL}GPS Agrícola com Piloto Automático (RTK){RESET}")
    tipo = validar_int("[1] Quero incluir, [2] Não quero incluir: ", [1, 2])
    a = True if tipo == 1 else False
    print(f"Sistema de GPS {a}")
    return a
   

def exibir_dados() -> None:
    global area, peso_total, lucro, gastos, metodo_colheita
    """Exibe o estado atual configurado."""
    if area == 0 or peso_total == 0:
        print(f"{VERMELHO}Defina uma área antes de ver seus dados!.{RESET}")
        return

    print(f"\n{VERDE}{NEGRITO}=== Perfil de Plantio ==={RESET}")
    print(f"{AZUL}Área: {area:.2f} m²{RESET}")
    print(f"{VERDE}--- Financeiro ---{RESET}")
    print(f"{AZUL}Peso total (ton): {peso_total:.2f}{RESET}")
    print(f"{AZUL}Lucro: R$ {lucro:.2f}{RESET}")
    print(f"{AZUL}Receita: R$ {receita:.2f}{RESET}")
    print(f"{AZUL}Gastos: R$ {gastos:.2f}{RESET}")
    print(f"{VERDE}--- Colheita ---{RESET}")
    print(f"{AZUL}Meio de colheita: {metodo_colheita}{RESET}")
    print(f"{AZUL}GPS ATIVO: {gps_ativo}{RESET}")
    print(f"{AZUL}Peso Total: {peso_total}{RESET}")
    print(f"{VERDE}--- Perdas ---{RESET}")
    print(f"{AZUL}Perda em %: {perda_percentual*100}{RESET}")
    print(f"{AZUL}Perda em R$: {perda_rs}{RESET}")
    print(f"{AZUL}Perda em ton: {perda_peso}{RESET}")

def menu() -> int:
    """Exibe o menu principal e retorna opção."""
    print(f"\n{VERDE}{NEGRITO}=== MENU PRINCIPAL ==={RESET}")
    print("1 - Área do plantio")
    print("2 - Método de colheita")
    print("3 - Financeiro")
    print("4 - Estatísticas Básicas (R)")
    print("5 - API Meteorológica (R)")
    print("6 - Exportar CSV")
    print("7 - Exibir Perfil")
    print("8 - Atualização de dados")
    print("9 - ")
    print(f"11 - Sair{RESET}")
    return validar_int(f"{AZUL}Selecione a opção: {RESET}", list(range(1, 10)))

def main() -> None:
    while True:
        opcao = menu()
        if opcao == 1:
            if area == 0:
                calcular_area()
            else: 
                print(f"{VERDE}ÁREA: {area}{RESET}")       
        elif opcao == 2:
            if area == 0:
                print(
                    f"{VERMELHO}Defina uma área antes de configurar o método de colheita!.{RESET}")
                continue
            definir_meio_colheita()
        elif opcao == 3:
            if metodo_colheita == "N/A":
                print(
                    f"{VERMELHO}Defina metodo de colheita antes de calcular financeiro.{RESET}")
                continue
            calcular_financeiro()
        elif opcao == 4:
            executar_estatisticas_r()
        elif opcao == 5:
            consultar_previsao_tempo()
        elif opcao == 6:
            exportar_csv()
        elif opcao == 7:
            exibir_dados()
        elif opcao == 8:
            atualizar_dados()
        elif opcao == 9:
            print(f"{VERDE}Encerrando aplicação. Até breve!{RESET}")
            break


if __name__ == "__main__":
    main()