from conectar_bd import conectar

def listar_producoes():
    conn = conectar()

    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM producao_agricola ORDER BY id")

            resultados = cursor.fetchall()

            if resultados:
                for linha in resultados:
                    print(linha)
            else:
                print("Nenhum registro encontrado.")
        except Exception as e:
            print("Erro ao consultar:", e)
        finally:
            cursor.close()
            conn.close()