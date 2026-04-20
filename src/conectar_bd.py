import os
import oracledb
from getpass import getpass


def _tentar_conexao(user: str, password: str, host: str, port: str, service: str):
    dsn = f"{host}:{port}/{service}"
    return oracledb.connect(
        user=user,
        password=password,
        dsn=dsn
    )


def conectar():
    erros = []

    print("\n=== Conexão com Oracle (FIAP) ===")
    print("Caso esteja usando o banco da FIAP, utilize:")
    print("Host: oracle.fiap.com.br")
    print("Porta: 1521")
    print("Instância: ORCL")
    print("Usuário: RMXXXXX")
    print("Senha: ddmmaa (data de nascimento)")
    print("-" * 40)

    # 1) Tentativa FIAP
    try:
        usar_fiap = input("Deseja conectar usando o ambiente FIAP? [S/N]: ").strip().upper()

        if usar_fiap == "S":
            user = input("Informe o usuário (RMXXXXX): ").strip()
            password = getpass("Informe a senha (ddmmaa): ").strip()

            conn = _tentar_conexao(
                user,
                password,
                "oracle.fiap.com.br",
                "1521",
                "ORCL"
            )

            print("Conexão com Oracle realizada com sucesso (FIAP).")
            return conn

        print("Pulando tentativa FIAP...")

    except Exception as e:
        erros.append(f"Falha na conexão FIAP: {e}")

    # 2) Fallback para variáveis de ambiente
    try:
        print("\nTentando conexão via variáveis de ambiente...")

        user = os.getenv("ORACLE_USER")
        password = os.getenv("ORACLE_PASSWORD")
        host = os.getenv("ORACLE_HOST", "localhost")
        port = os.getenv("ORACLE_PORT", "1521")
        service = os.getenv("ORACLE_SERVICE", "XEPDB1")

        if not user or not password:
            raise ValueError("Variáveis ORACLE_USER e ORACLE_PASSWORD não estão definidas.")

        conn = _tentar_conexao(user, password, host, port, service)

        print("Conexão com Oracle realizada com sucesso (ambiente local).")
        return conn

    except Exception as e:
        erros.append(f"Falha na conexão local: {e}")

    print("\nErro ao conectar ao Oracle.")
    for erro in erros:
        print(f"- {erro}")

    return None