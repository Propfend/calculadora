novamente = 0

while novamente != 'n':
    num1 = int(input('digite um número: '))

    num2 = int(input('digite outro númmero: ' ))

    print('\n')

    print('Somar: 1')
    print('Subtrair: 2')
    print('multiplicar: 3')
    print('dividir: 4 \n\n')

    sinal = 0

    while(sinal not in (1, 2, 3, 4)):
        try:
            sinal = int(input('escolha a operação numérica: '))
        except:
            print('escolha a operação numérica válida(1, 2, 3, 4)')
   
    if sinal == 1:
        print(f'{num1} + {num2} = {num1 + num2}')
    else:
        if sinal == 2:
            print(f'{num1} - {num2} = {num1 - num2}')
        else:
            if sinal == 3:
                print(f'{num1} x {num2} = {num1 * num2}')
            else:
                if sinal == 4:
                    print(f'{num1} % {num2} = {num1 / num2}')
    
    novamente = str(input('deseja continuar?(enter/n): \n\n'))

