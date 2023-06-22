import random

while True:
	user_selection = input("\nВыберите камень, ножницы или бумагу >> ").lower().strip()
	choosing_computer = random.choice(["камень", "бумага", "ножницы"])

	if user_selection == choosing_computer:
		print(f"Ничья! Вы и компьютер выбрали {user_selection}")

	elif user_selection == "камень":
		if choosing_computer == "бумага":
			print(f"Вы проиграли компьютер выбрал {choosing_computer}, а вы {user_selection}")
		else:
			print(f"Вы выйграли компьютер выбрал {choosing_computer},а вы выбрали {user_selection}")

	elif user_selection == "бумага":
		if choosing_computer == "ножницы":
			print(f"Вы проиграли компьютер выбрал {choosing_computer}, а вы {user_selection}")
		else:
			print(f"Вы выйграли компьютер выбрал {choosing_computer},а вы выбрали {user_selection}")

	elif user_selection == "ножницы":
		if choosing_computer == "камень":
			print(f"Вы проиграли компьютер выбрал {choosing_computer}, а вы {user_selection}")
		else:
			print(f"Вы выйграли компьютер выбрал {choosing_computer},а вы выбрали {user_selection}")

	else:
		print("Ошибка ввода! Надо вводить только слова 'камень', 'бумага' или 'ножницы'")
