def display_menu():
    print("Телефонный справочник")
    print("1. Добавить запись")
    print("2. Изменить запись")
    print("3. Удалить запись")
    print("4. Поиск записи")
    print("5. Показать все записи")
    print("6. Выход")


def add_entry(phonebook):
    name = input("Введите имя или фамилию: ").strip()
    phone = input("Введите номер телефона: ").strip()
    phonebook[name] = phone
    print(f"Запись для {name} добавлена.\n")


def edit_entry(phonebook):
    name = input("Введите имя или фамилию для изменения записи: ").strip()
    if name in phonebook:
        phone = input(f"Введите новый номер телефона для {name}: ").strip()
        phonebook[name] = phone
        print(f"Запись для {name} изменена.\n")
    else:
        print(f"Запись для {name} не найдена.\n")


def delete_entry(phonebook):
    name = input("Введите имя или фамилию для удаления записи: ").strip()
    if name in phonebook:
        del phonebook[name]
        print(f"Запись для {name} удалена.\n")
    else:
        print(f"Запись для {name} не найдена.\n")


def search_entry(phonebook):
    name = input("Введите имя или фамилию для поиска записи: ").strip()
    if name in phonebook:
        print(f"Номер телефона для {name}: {phonebook[name]}\n")
    else:
        print(f"Запись для {name} не найдена.\n")


def display_all_entries(phonebook):
    if phonebook:
        print("Все записи в телефонном справочнике:")
        for name, phone in phonebook.items():
            print(f"{name}: {phone}")
        print()
    else:
        print("Телефонный справочник пуст.\n")


def main():
    phonebook = {}
    while True:
        display_menu()
        choice = input("Выберите пункт меню: ").strip()
        if choice == "1":
            add_entry(phonebook)
        elif choice == "2":
            edit_entry(phonebook)
        elif choice == "3":
            delete_entry(phonebook)
        elif choice == "4":
            search_entry(phonebook)
        elif choice == "5":
            display_all_entries(phonebook)
        elif choice == "6":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите правильный пункт меню.\n")


if __name__ == "__main__":
    main()
