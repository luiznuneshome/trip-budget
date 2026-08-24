def obter_valor_positivo(mensagem: str) -> float:
    while True:
        try:
            valor = float(input(mensagem))
            if valor < 0:
                print('O valor não pode ser negativo. Tente novamente.')
            else:
                return valor
        except ValueError:
            print('Entrada inválida. Digite um número válido.')


def obter_numero_participantes() -> int:
    while True:
        dividir = input(
            '\nEssa é uma viagem em grupo onde os participantes irão dividir os gastos? (sim/não): '
        ).strip().lower()

        if dividir in ['sim', 's']:
            try:
                num = int(input('Digite o número de participantes da viagem: '))

                if num > 0:
                    return num

                print('O número de participantes deve ser maior que zero.')

            except ValueError:
                print('Entrada inválida. Digite um número inteiro.')

        elif dividir in ['não', 'nao', 'n']:
            return 1

        else:
            print('Resposta inválida. Digite "sim" ou "não".')


def exibir_resumo(gastos: dict, total: float, participantes: int) -> None:
    print('\n' + '=' * 35)
    print('   RESUMO DO ORÇAMENTO DA VIAGEM   ')
    print('=' * 35)

    for item, valor in gastos.items():
        print(f'Valor de {item}: R$ {valor:.2f}')

    print(f'\nO valor total da viagem é: R$ {total:.2f}')

    if participantes > 1:
        valor_por_pessoa = total / participantes
        print(
            f'O valor por participante é: R$ {valor_por_pessoa:.2f} '
            f'(para cada um dos {participantes} participantes).'
        )

    print('=' * 35 + '\n')


def calcular_orcamento_viagem():

    print('Bem-vindo ao programa de cálculo de orçamento de viagem!')
    print('Responda às seguintes perguntas para saber seu orçamento.\n')

    gastos = {
        'Transporte': obter_valor_positivo(
            'Digite o valor total do transporte: '
        ),
        'Hospedagem': obter_valor_positivo(
            'Digite o valor total da hospedagem: '
        ),
        'Alimentação': obter_valor_positivo(
            'Digite o valor total da alimentação (café, almoço, jantar): '
        ),
        'Passeios e Entretenimento': obter_valor_positivo(
            'Digite o valor total dos passeios e entretenimentos: '
        ),
        'Deslocamento': obter_valor_positivo(
            'Digite o valor total do deslocamento (uber, táxi, etc.): '
        ),
        'Gastos Adicionais': obter_valor_positivo(
            'Digite o valor total dos gastos adicionais (compras, etc.): '
        ),
        'Reserva de Emergência': obter_valor_positivo(
            'Digite o valor total da reserva de emergência: '
        )
    }

    total = sum(gastos.values())
    participantes = obter_numero_participantes()

    exibir_resumo(gastos, total, participantes)