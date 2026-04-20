import oracledb
from conectar_bd import conectar

def inserir_simulacao(cultura_obj, nivel_umidade=None, defeitos_graos=None):
    conn = conectar()
    if not conn:
        raise RuntimeError("Falha ao obter conexão com o Oracle")
    cursor = None
    try:
        cursor = conn.cursor()

        id_var = cursor.var(oracledb.NUMBER)

        cursor.execute("""
            INSERT INTO CULTIVO (
                NOME_CULTURA,
                       AREA_M2,
                       STATUS_QUALIDADE
            )
            VALUES (
                       :1, :2, :3
            )
            RETURNING ID_SIMULACAO INTO :4
        """, (
            cultura_obj.cultura,
            cultura_obj.area,
            cultura_obj.status_qualidade or "Não analisado",
            id_var
        ))
        id_simulacao = int(id_var.getvalue()[0])

        cursor.execute("""
            INSERT INTO INSUMOS (
                ID_SIMULACAO,
                QNT_ADUBO,
                QNT_AGUA,
                QNT_FOSFATO,
                NOME_HERBICIDA,
                NOME_PESTICIDA,
                NOME_FERTILIZANTE
            )
            VALUES (
                :1, :2, :3, :4, :5, :6, :7
            )
        """, (
            id_simulacao,
            cultura_obj.insumos.adubo,
            cultura_obj.insumos.agua,
            cultura_obj.insumos.fosfato,
            cultura_obj.insumos.herbicida,
            cultura_obj.insumos.pesticida,
            cultura_obj.insumos.fertilizante
        ))
        
        cursor.execute("""
            INSERT INTO FINANCEIRO_METODOS (
                ID_SIMULACAO,
                METODO_APLICACAO,
                PESO_ESTIMADO_TON,
                LUCRO_ESTIMADO,
                GASTOS_TOTAIS
            )
            VALUES (
                :1, :2, :3, :4, :5
            )
        """, (
            id_simulacao,
            cultura_obj.financeiro.metodo_aplicacao,
            cultura_obj.financeiro.peso_total,
            cultura_obj.financeiro.lucro,
            cultura_obj.financeiro.gastos
        ))
        
        cursor.execute("""
            INSERT INTO QUALIDADE (
                ID_SIMULACAO,
                NIVEL_UMIDADE,
                DEFEITOS_GRAOS    
            )
            VALUES (
                :1, :2, :3   
            )
            """, (
                id_simulacao,
                nivel_umidade,
                defeitos_graos
        ))

        conn.commit()
        print(f"Simulação salva com sucesso. ID_SIMULACAO={id_simulacao}")
        return id_simulacao
    
    except Exception as e:
        conn.rollback()
        raise RuntimeError(f"Erro ao inserir simulação: {e}")

    finally:
        if cursor:
            cursor.close()
        conn.close()