import components.teachers.service as teacher
from lab_7.utils.safe_int_input import safe_int_input


def teachers_menu():
    print("База данных чителей.\n"
          "Выберите действие\n"
          "1.Создать учителя\n"
          "2.Показать всех учителей\n"
          "3.Найти учителя по id\n"
          "4.Редактировать учителя\n"
          "5.Удалить учителя\n")
    action_number = safe_int_input()
    if action_number == 1:
        create_teacher()
    elif action_number == 2:
        show_all_teachers()
    elif action_number == 3:
        find_teacher()
    elif action_number == 4:
        update_teacher()
    elif action_number == 5:
        delete_teacher()


def create_teacher():
    name = input("Введите имя учителя: ")
    phone_number = input("Введите номер телефона учителя: ")
    teacher.create_one({"name": name, "phone_number": phone_number})


def show_all_teachers():
    teachers = teacher.get_all()
    for tchr in teachers:
        print_teacher(tchr)


def find_teacher():
    id = safe_int_input("Введите id учителя: ")
    tchr = teacher.get_one_by_id(id)
    print_teacher(tchr)


def update_teacher():
    id = safe_int_input("Введите id учителя, данные которого хотите заменить: ")
    tchr = teacher.get_one_by_id(id)
    print("Учитель сейчас:")
    print_teacher(tchr)

    if (input("Обновить имя? (да/нет) ") == "да"):
        tchr["name"] = input("Введите новое имя:")
    if (input("Обновить номер телефона? (да/нет) ") == "да"):
        tchr["phone_number"] = input("Введите новый номер телефона:")

    print("Изменённый учитель: ")
    print_teacher(tchr)
    teacher.update_one_by_id(id, tchr)


def delete_teacher():
    id = safe_int_input("Введите id учителя, данные которого хотите удалить: ")
    teacher.delete_one_by_id(id)


def print_teacher(tchr):
    print(f"{tchr['id']}. {tchr['name']}. Контактный номер: {tchr['phone_number']}")
