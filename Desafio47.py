# Retorna os números pares de 0 a 50.
print('\033[31mRetorna os números pares de 0 a 50\033[m')
for c in range(2, 52, 2): # Esta forma é a mais indicada pois usa menos o processador.
    print(c)
print('\n')

#Outra forma de fazer:
print('Outra forma de fazer:')
for c in range(2, 51):
    if c % 2 == 0:
        print(c)
