from conectar_bd import conectar

def inserir_producao(cultura, area_hectares, producao_esperada, producao_real, perdas_percentual, tipo_colheita, data_colheita, regiao):
    conn = conectar()

    if conn:
        try:
            cursor = conn.cursor()
            sql = """
                INSERT INTO producao_agricola
                (cultura, area_hectares, producao_esperada, producao_real, perdas_percentual, tipo_colheita, data_colheita, regiao)
                VALUES
                (:1, :2, :3, :4, :5, :6, TO_DATE(:7, 'YYYY-MM-DD'), :8)
            """
            cursor.execute(sql, (
                cultura, area_hectares, producao_esperada, producao_real,
                perdas_percentual, tipo_colheita, data_colheita, regiao
            ))
            conn.commit()
            print("Registro inserido com sucesso.")
        except Exception as e:
            print("Erro ao inserir:", e)
        finally:
            cursor.close()
            conn.close()