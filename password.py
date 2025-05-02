import random
import string

def generate_password(length):
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    special_characters = '!@#$%^&*()_+-=[]{}|;:,.<>?/'

    all_characters = lowercase_letters + uppercase_letters + digits + special_characters


    if length < 4:
        print("Внимание: Длина пароля слишком мала для гарантии всех типов символов.")

        if length <= 0:
            return "Ошибка: Длина пароля должна быть положительным числом."
        password_list = random.sample(all_characters, length)
    else:
        password_list = []
        password_list.append(random.choice(lowercase_letters))
        password_list.append(random.choice(uppercase_letters))
        password_list.append(random.choice(digits))
        password_list.append(random.choice(special_characters))

        remaining_length = length - 4
        for _ in range(remaining_length):
            password_list.append(random.choice(all_characters))


        random.shuffle(password_list)
    password = "".join(password_list)
    return password

if 1 == 1:
    while True:
        try:

            password_length_str = input("Введите желаемую длину пароля (рекомендуется >= 8): ")
            password_length = int(password_length_str)

            if password_length <= 0:
                 print("Ошибка: Длина пароля должна быть положительным числом.")
                 continue
            break

        except ValueError:

            print("Некорректный ввод. Пожалуйста, введите целое число.")

    generated_password = generate_password(password_length)
    print(f"\nСгенерированный пароль: {generated_password}")
