from conectar_bd import conectar

def atualizar_producao_real(id_registro, nova_producao_real):
    conn = conectar()

    if conn:
        try:
            cursor = conn.cursor()

            sql_busca = "SELECT producao_esperada FROM producao_agricola WHERE id = :1"
            cursor.execute(sql_busca, (id_registro,))
            resultado = cursor.fetchone()

            if resultado:
                producao_esperada = resultado[0]
                nova_perda = round(((producao_esperada - nova_producao_real) / producao_esperada) * 100, 2)

                sql_update = """
                    UPDATE producao_agricola
                    SET producao_real = :1,
                        perdas_percentual = :2
                    WHERE id = :3
                """
                cursor.execute(sql_update, (nova_producao_real, nova_perda, id_registro))
                conn.commit()
                print("Registro atualizado com sucesso.")
            else:
                print("ID não encontrado.")
        except Exception as e:
            print("Erro ao atualizar:", e)
        finally:
            cursor.close()
            conn.close()