import components.schools.service as school
from lab_7.utils.safe_int_input import safe_int_input


def schools_menu():
    print("База данных школ.\n"
          "Выберите действие\n"
          "1.Создать школу\n"
          "2.Показать все школы\n"
          "3.Найти школу по id\n"
          "4.Редактировать школу\n"
          "5.Удалить школу\n")
    action_number = safe_int_input()
    if action_number == 1:
        create_school()
    elif action_number == 2:
        show_all_schools()
    elif action_number == 3:
        find_school()
    elif action_number == 4:
        update_school()
    elif action_number == 5:
        delete_school()


def create_school():
    number = input("Введите номер школы: ")
    address = input("Введите адрес школы: ")
    school.create_one({"number": number, "address": address})


def show_all_schools():
    schools = school.get_all()
    for schl in schools:
        print_school(schl)


def find_school():
    id = safe_int_input("Введите id школы: ")
    schl = school.get_one_by_id(id)
    print_school(schl)


def update_school():
    id = safe_int_input("Введите id школы, данные которой хотите заменить: ")
    schl = school.get_one_by_id(id)
    print("Школа сейчас:")
    print_school(schl)

    if (input("Обновить номер? (да/нет) ") == "да"):
        schl["number"] = input("Введите новый номер:")
    if (input("Обновить адрес? (да/нет) ") == "да"):
        schl["address"] = input("Введите новый адрес:")

    print("Изменённая школа: ")
    print_school(schl)
    school.update_one_by_id(id, schl)


def delete_school():
    id = safe_int_input("Введите id школы, данные которой хотите удалить: ")
    school.delete_one_by_id(id)


def print_school(schl):
    print(f"{schl['id']}. Школа №{schl['number']} по адресу {schl['address']}")

