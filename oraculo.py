import wikiquotes
import wikiquote



intention = input('escribe tu intencion : ')
msj = input('escribe tu mensaje para publicar: ')
ctx = input('dame un poco de contexto adicional: ')


random_title = wikiquote.random_titles(max_titles=3, lang='es')
if random_title != None:

	try:
		quote = wikiquotes.random_quote(random_title[0], "spanish")
	except:
		try:
			random_title = wikiquote.random_titles(max_titles=10, lang='es')
			quote = wikiquotes.random_quote(random_title[random.list(range(10))], "spanish")
		except:
			quote = ''

	print(quote)

	veredicto = input('ejecutar / esperar (escribir la opcion) : ')

	file = open('results.txt','a')	
	file.write(intention+ '\n')
	file.write(msj+ '\n')
	file.write(ctx + '\n')
	file.write(veredicto + '\n')
	file.write('')
	file.write(quote + '\n')
	file.write('--- \n')
	
else:

	print('api failed')
