from conectar_bd import conectar

conn = conectar()

if conn:
    cursor = conn.cursor()
    cursor.execute("SELECT 'Conectado com sucesso' FROM dual")
    resultado = cursor.fetchone()
    print(resultado[0])

    cursor.close()
    conn.close()