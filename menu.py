from calculator import add, substracts

def menu():
    opcion = 0
    
    while True:
        if opcion in (1,2):
            num1 = float(input("Ingrese el primer numero:\n"))
            num2 = float(input("Ingrese el segundo numero:\n"))
        
        if opcion == 3:
            print('\nCalculadora terminada...!!!')
            break
        elif opcion ==1:
            print('SUMAA..!!!!')
            #print('Resultado de la suma: '+str(add(num1,num2)))
        elif opcion ==2:
            print('Resta..!!!!')
            #print('Resultado de la resta: '+str(substracts(num1,num2)))
        print('------------------------------------')
        print('|1. Sumar                          |')
        print('|2. Restar                         |')
        print('|3. Salir                          |')
        print('------------------------------------')
        opcion = int(input('Ingrese alguna opcion [1-3]\n'))
