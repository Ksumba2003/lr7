import datetime

import components.classes.service as classes
import components.schools.service as schools
import components.teachers.service as teachers
from lab_7.utils.safe_int_input import safe_int_input


def classes_menu():
    print("База данных класс.\n"
          "Выберите действие\n"
          "1.Создать класс\n"
          "2.Показать все классы\n"
          "3.Найти класс по id\n"
          "4.Редактировать класс\n"
          "5.Удалить класс\n")
    action_number = safe_int_input()
    if action_number == 1:
        create_class()
    elif action_number == 2:
        show_all_classes()
    elif action_number == 3:
        find_class()
    elif action_number == 4:
        update_class()
    elif action_number == 5:
        delete_class()


def create_class():
    year = safe_int_input("Введите год поступления класса: ")
    letter = input("Введите букву класса: ")
    schl = find_school()
    tchr = find_teacher()

    classes.create_one({"year": year, "letter": letter, "school_id": schl["id"], "teacher_id": tchr["id"]})


def find_school():
    while True:
        school_id = safe_int_input("Введите id школы: ")
        shl = schools.get_one_by_id(school_id)
        if shl:
            return shl


def find_teacher():
    while True:
        teacher_id = safe_int_input("Введите id учителя: ")
        tchr = teachers.get_one_by_id(teacher_id)
        if tchr:
            return tchr


def show_all_classes():
    all_classes = classes.get_all()
    for cls in all_classes:
        print_classes(cls)


def find_class():
    id = safe_int_input("Введите id класса: ")
    cls = classes.get_one_by_id(id)
    print_classes(cls)


def update_class():
    id = safe_int_input("Введите id классы, данные которой хотите заменить: ")
    cls = classes.get_one_by_id(id)
    print("Класс сейчас:")
    print_classes(cls)

    if (input("Обновить год? (да/нет) ") == "да"):
        cls["year"] = safe_int_input("Введите новый год:")
    if (input("Обновить букву? (да/нет) ") == "да"):
        cls["letter"] = input("Введите новую букву:")
    if (input("Обновить школу? (да/нет) ") == "да"):
        school = find_school()
        cls["school_id"] = school["id"]
    if (input("Обновить учителя? (да/нет) ") == "да"):
        teacher = find_teacher()
        cls["teacher_id"] = teacher["id"]

    print("Изменённая класса: ")
    print_classes(cls)
    classes.update_one_by_id(id, cls)


def delete_class():
    id = safe_int_input("Введите id класса, данные которого хотите удалить: ")
    classes.delete_one_by_id(id)


def print_classes(cls):
    print(
        f"{cls['id']}. {get_class_number_by_year(cls['year'])}{cls['letter']} Учитель {cls['teacher_id']} Школа {cls['school_id']}")


def get_class_number_by_year(year):
    return datetime.date.today().year - year
