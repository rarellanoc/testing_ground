import wikiquotes
import wikiquote



intention = input('write your intention : ')
msj = input('write your message : ')
ctx = input('give me a little more context : ')


random_title = wikiquote.random_titles(max_titles=3)
if random_title != None:

	try:
		quote = wikiquotes.random_quote(random_title[0], "english")
	except:
		random_title = wikiquote.random_titles(max_titles=10)
		quote = wikiquotes.random_quote(random_title[random.list(range(10))], "english")
	print(quote)

	veredicto = input('ejecutar / esperar ')

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
