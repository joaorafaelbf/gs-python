# ==========================================================
# ORBITTRACK
# Global Solution FIAP
# Rastreamento Logístico via IoT + Satélite
# ==========================================================

# ==========================================================
# LISTAS (20 informações cada)
# ==========================================================

placas = [
    "ABC1234", "DEF5678", "GHI9012", "JKL3456", "MNO7890",
    "PQR1122", "STU3344", "VWX5566", "YZA7788", "BCD9900",
    "EFG1111", "HIJ2222", "KLM3333", "NOP4444", "QRS5555",
    "TUV6666", "WXY7777", "ZAB8888", "CDE9999", "FGH0001"
]

motoristas = [
    "Carlos", "Ana", "Marcos", "Julia", "Pedro",
    "Fernanda", "Lucas", "Amanda", "Rafael", "Bianca",
    "Diego", "Larissa", "Thiago", "Camila", "Gustavo",
    "Patricia", "Bruno", "Renata", "Felipe", "Vanessa"
]

latitudes = [
    -23.55, -22.90, -19.92, -15.78, -12.97,
    -30.03, -25.42, -16.68, -8.05, -3.73,
    -20.31, -7.11, -9.66, -1.45, -5.09,
    -10.18, -14.23, -17.73, -2.53, -13.00
]

longitudes = [
    -46.63, -43.20, -43.94, -47.88, -38.50,
    -51.23, -49.27, -49.25, -34.90, -38.52,
    -40.33, -34.86, -35.73, -48.50, -42.80,
    -48.33, -51.92, -49.10, -44.30, -39.50
]

# ==========================================================
# FUNÇÕES
# ==========================================================

def descricao_projeto():
    print("\n" + "=" * 60)
    print("ORBITTRACK")
    print("=" * 60)
    print("Sistema de rastreamento logístico baseado em IoT")
    print("e comunicação via satélite para monitoramento")
    print("de cargas em regiões sem cobertura celular.")
    print("Voltado para transporte, mineração e agronegócio.")
    print("=" * 60)


def mostrar_frota():
    print("\nFROTA MONITORADA")
    print("-" * 60)

    for i in range(len(placas)):
        print(
            f"{i+1:02d} | "
            f"Placa: {placas[i]} | "
            f"Motorista: {motoristas[i]}"
        )


def consultar_localizacao():
    print("\nCONSULTA DE LOCALIZAÇÃO")

    placa = input("Digite a placa: ").upper()

    encontrado = False

    for i in range(len(placas)):
        if placas[i] == placa:

            print("\nLOCALIZAÇÃO ENCONTRADA")
            print(f"Placa: {placas[i]}")
            print(f"Motorista: {motoristas[i]}")
            print(f"Latitude: {latitudes[i]}")
            print(f"Longitude: {longitudes[i]}")

            encontrado = True
            break

    if not encontrado:
        print("Veículo não encontrado.")


def atualizar_localizacao():

    print("\nATUALIZAÇÃO VIA SATÉLITE")

    placa = input("Informe a placa: ").upper()

    for i in range(len(placas)):

        if placas[i] == placa:

            try:

                nova_lat = float(input("Nova Latitude: "))
                nova_long = float(input("Nova Longitude: "))

                latitudes[i] = nova_lat
                longitudes[i] = nova_long

                print("\n📡 Dados enviados com sucesso!")

            except ValueError:
                print("Erro: digite apenas números.")

            return

    print("Veículo não encontrado.")


def verificar_alertas():

    print("\nANÁLISE DE ALERTAS")

    alertas = 0

    for i in range(len(placas)):

        if (
            latitudes[i] < -35 or
            latitudes[i] > 5 or
            longitudes[i] < -75 or
            longitudes[i] > -30
        ):

            print(f"⚠ ALERTA DE DESVIO: {placas[i]}")
            alertas += 1

    if alertas == 0:
        print("Nenhum alerta encontrado.")


def relatorio_geral():

    print("\nRELATÓRIO GERAL")
    print("-" * 60)

    total = len(placas)

    print(f"Total de veículos monitorados: {total}")

    print("\nResumo da Frota:")

    for i in range(total):

        print(
            f"{placas[i]} | "
            f"{motoristas[i]} | "
            f"({latitudes[i]}, {longitudes[i]})"
        )


def estatisticas():

    print("\nESTATÍSTICAS")

    norte = 0
    sul = 0

    for latitude in latitudes:

        if latitude >= 0:
            norte += 1
        else:
            sul += 1

    print(f"Veículos no Hemisfério Norte: {norte}")
    print(f"Veículos no Hemisfério Sul: {sul}")

    if sul > norte:
        print("Maior concentração no Hemisfério Sul.")
    elif norte > sul:
        print("Maior concentração no Hemisfério Norte.")
    else:
        print("Distribuição equilibrada.")


# ==========================================================
# MENU
# ==========================================================

def menu():

    while True:

        print("\n")
        print("=" * 60)
        print("           ORBITTRACK - MENU PRINCIPAL")
        print("=" * 60)
        print("1 - Descrição da solução")
        print("2 - Exibir frota monitorada")
        print("3 - Consultar localização")
        print("4 - Atualizar localização")
        print("5 - Verificar alertas")
        print("6 - Relatório geral")
        print("7 - Estatísticas")
        print("8 - Encerrar")
        print("=" * 60)

        try:

            opcao = int(input("Escolha uma opção: "))

            match opcao:

                case 1:
                    descricao_projeto()

                case 2:
                    mostrar_frota()

                case 3:
                    consultar_localizacao()

                case 4:
                    atualizar_localizacao()

                case 5:
                    verificar_alertas()

                case 6:
                    relatorio_geral()

                case 7:
                    estatisticas()

                case 8:
                    print("\nSistema encerrado.")
                    break

                case _:
                    print("Opção inválida.")

        except ValueError:
            print("Digite apenas números.")


# ==========================================================
# INÍCIO DO SISTEMA
# ==========================================================

menu()
