def binary_search(lst,x):
	start = 0
	finish = len(lst)-1
	attemp = 0

	while start <= finish:
		mid = (start+finish)//2
		guess = lst[mid]
		attemp += 1

		if guess == x:
			answer = "Число отгаданно за " + str(attemp) + " попыток. Число - " + str(guess)
			return answer

		elif guess > x:
			finish = mid-1

		else:
			start = mid + 1
	return None

while True:
	try:
		count_one = int(input("Введите диапозон поиска:\n"))
		x = int(input("Введите искомое число:\n"))
	except ValueError as error:
		print("Ошибка -", error)
	else:
		break

lst = [i for i in range(1, (count_one + 1))]

b_s = binary_search(lst,x)
print(b_s)

input()
