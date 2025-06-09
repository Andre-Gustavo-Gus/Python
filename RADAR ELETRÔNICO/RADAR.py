vermelho  = '\033[1;31m' 
destaque  = '\033[4m'
fim       = '\033[m'

velocidade = float(input('Qual foi a velocidade? '))
print('-' * 50)

if velocidade > 80:
    print(f'{vermelho}Multado!{fim} Você excedeu o limite {destaque}(80Km/h){fim}.')
    multa = (velocidade - 80) * 7
    print(f'Você deve pagar uma multa de R${multa:.2f}!')
else:
    print('Tudo certo! Você está dentro do limite de velocidade.')

print('Tenha um bom dia e dirija com segurança!')
print('-' * 50)