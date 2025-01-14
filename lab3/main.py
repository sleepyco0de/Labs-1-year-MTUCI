def main():
    user_input = input("Введите текст, который будет записан в файл user_input.txt: ")
    with open('user_input.txt', 'a', encoding='utf-8') as file:  
        file.write('\n' + user_input)  
    print("Текст успешно записан в файл user_input.txt.")

    add_more = input("Хотите добавить текст в файл? (да/нет): ").strip().lower()
    if add_more == 'да':
        while True:
            append_input = input("Введите текст для добавления: ")
            with open('user_input.txt', 'a', encoding='utf-8') as file:
                file.write('\n' + append_input)  
            print("Текст успешно добавлен в файл user_input.txt.")
            add_more = input("Хотите добавить еще текст? (да/нет): ").strip().lower()
            if add_more == 'нет':
                break  
    elif add_more == 'нет':
        print("Выход из программы.")
    else:
        print('Неверный ввод')

if __name__ == "__main__":
    main()

# def main():
#     user_input = input("1 - Чтение Файла Сразу / 2 - Построчное Чтение")
#     if user_input == '1' and user_input.isdigit():
#         with open('example.txt', 'r', encoding='utf-8') as file:
#             return file.read()
#     elif user_input == '2' and user_input.isdigit():
#         with open('example.txt', 'r', encoding='utf-8') as file:
#             return file.readlines()
#     else:
#         return 'Неверный Ввод'
#
# if __name__ == "__main__":
#     print(*main(),sep='')

'''def main():
    try:
        user_input = input("1 - Чтение Файла Сразу / 2 - Построчное Чтение")
        if user_input == '1' and user_input.isdigit():
            with open('exaple.txt', 'r', encoding='utf-8') as file:
                return file.read()
        elif user_input == '2' and user_input.isdigit():
            with open('example.txt', 'r', encoding='utf-8') as file:
                return file.readlines()
        else:
            return 'Неверный Ввод'
    except:
        return 'FileNotFoundError'

if __name__ == "__main__":
    print(main())'''
