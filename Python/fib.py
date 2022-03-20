def fib(x):
	a, b = 0, 1

	while a < x:
		print(a, end =" ")
		a, b = b, a+b
		print()


while True:
	try:
		user_input = int(input("Введите свое значение:\n"))
	except ValueError as e:
		print("Ошибка -",e)
	else:
		break

		
fib(user_input)
