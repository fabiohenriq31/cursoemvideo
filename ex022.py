nome = input('Digite um nome: ')
print ('Nome maiúsculo: ', nome.upper())
print ('Nome minúsculo: ', nome.lower())
print ('Seu nome ao todo tem: ',len(''.join(nome.split())))
print ('Seu primeiro nome é {} e ele tem {} letras' .format(nome.split()[0],len(nome.split()[0])) )

