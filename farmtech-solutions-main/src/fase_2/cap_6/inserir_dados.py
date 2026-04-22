from conectar_bd import conectar

def inserir_simulacao(
    id_simulacao, area_m2, metodo_colheita, lucro, gastos, 
    peso_total, peso_perdido_ton, peso_perdido_rs, coef_correlacao,
    # Novos parâmetros para as outras tabelas:
    nome_cultura, status_qualidade, defeitos_graos,
    qnt_adubo, qnt_agua, qnt_fosfato, nome_herbicida, nome_pesticida, nome_fertilizante
):
    conn = conectar()
    if not conn:
        raise Exception("Conexão com Oracle falhou.")

    cursor = None
    try:
        cursor = conn.cursor()

        # 1. Gerar ID Único (Chave Primária Principal)
        cursor.execute("SELECT MAX(ID_SIMULACAO) FROM SIMULACAO_COLHEITA")
        row = cursor.fetchone()
        max_id = row[0] if row and row[0] is not None else 0
        novo_id = max(id_simulacao, max_id + 1)

        # --- INSERT 1: SIMULACAO_COLHEITA ---
        sql_simulacao = """
            INSERT INTO SIMULACAO_COLHEITA (
                ID_SIMULACAO, AREA_M2, METODO_COLHEITA, LUCRO, GASTOS, 
                PESO_TOTAL, PESO_PERDIDO_TON, PESO_PERDIDO_RS, COEF_CORRELACAO
            ) VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9)
        """
        cursor.execute(sql_simulacao, (
            novo_id, area_m2, metodo_colheita, lucro, gastos,
            peso_total, peso_perdido_ton, peso_perdido_rs, coef_correlacao
        ))

        # --- INSERT 2: CULTIVO ---
        sql_cultivo = "INSERT INTO CULTIVO (ID_SIMULACAO, NOME_CULTURA, AREA_M2, STATUS_QUALIDADE) VALUES (:1, :2, :3, :4)"
        cursor.execute(sql_cultivo, (novo_id, nome_cultura, area_m2, status_qualidade))

        # --- INSERT 3: FINANCEIRO_METODOS ---
        sql_financeiro = """
            INSERT INTO FINANCEIRO_METODOS (ID_SIMULACAO, METODO_APLICACAO, PESO_ESTIMADO_TON, LUCRO_ESTIMADO, GASTOS_TOTAIS) 
            VALUES (:1, :2, :3, :4, :5)
        """
        cursor.execute(sql_financeiro, (novo_id, metodo_colheita, peso_total, lucro, gastos))

        # --- INSERT 4: INSUMOS ---
        sql_insumos = """
            INSERT INTO INSUMOS (ID_SIMULACAO, QNT_ADUBO, QNT_AGUA, QNT_FOSFATO, NOME_HERBICIDA, NOME_PESTICIDA, NOME_FERTILIZANTE)
            VALUES (:1, :2, :3, :4, :5, :6, :7)
        """
        cursor.execute(sql_insumos, (novo_id, qnt_adubo, qnt_agua, qnt_fosfato, nome_herbicida, nome_pesticida, nome_fertilizante))

        # --- INSERT 5: QUALIDADE ---
        sql_qualidade = "INSERT INTO QUALIDADE (ID_SIMULACAO, DEFEITOS_GRAOS) VALUES (:1, :2)"
        cursor.execute(sql_qualidade, (novo_id, defeitos_graos))

        conn.commit()
        print(f"Sucesso! Simulação {novo_id} salva em todas as 5 tabelas.")

    except Exception as e:
        if conn: conn.rollback()
        print(f"Erro ao inserir no Oracle: {e}")
        raise e
    finally:
        if cursor: cursor.close()
        if conn: conn.close()