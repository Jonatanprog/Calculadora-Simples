 #Solicitar operação

 num1 = int(input('Digite o peimeiro número: "))

 operação=input ('''Por favor use
 + para adição
 - para subtração
 * para multiplicação
 / para divisão       ''')

 num2 = int(input('Digite o segundo número: '))

 if operação == '+':
	 print('{} + {} = '.format(num1, num2))
	 print (num1 + num2)
 
 elif operação == '-':
	print('{} - {} = '.format(num1, num2))
	print (num1 - num2)
 
 elif operação == '*':
	print('{} * {} = '.format(num1, num2))
	print (num1 * num2)

 elif operação == '/':
	print('{} / {} = '.format(num1, num2))
	print (num1 / num2)
	
 else:
	print('Por favor use uma operação matemática.')
