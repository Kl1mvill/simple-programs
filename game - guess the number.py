import random

print('Игра "Угадай число"', "Правила - компьютер загадывает число от 1 до 50. Вы должны угадать число используя 10 попыток.", sep="\n")

while True:
	attempts = 0
	random_number = str(random.randint(1, 50))
	print("\n\nИгра началась, компьютер загадал число!")

	while True:
		user_option = input("\nВведите число >> ")

		if attempts == 10:
			print(f"Вы истратили все попытки, компьютер загадал число {random_number}"); break

		if user_option == random_number:
			print(f"Вы угадали. Вы использовали {attempts} попыток"); break

		elif int(user_option) > int(random_number):
			print("Ваше число больше загаданого")

		elif int(user_option) < int(random_number):
			print("Ваше число меньше загаданого")

		else:
			print("Вы допустили ошибку! Надо вводить только числа")

		attempts += 1


