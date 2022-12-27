import emoji
km = float (input('Quantos Km o veiculo percorreu? '))
d = int (input('Quantos dias alugado? '))
print('Valor da diaria: R$60,00')
print('Valor por Km rodado: R$0,15')
calc1 = km * 0.15
calc2 = d * 60
print (emoji.emojize('O valor do aluguel é:\nDiaria: R${}\nKm: R${}\nTotal: R$ {} \U0001f605'.format(calc2, calc1, calc1 + calc2 )))