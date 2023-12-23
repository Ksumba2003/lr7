import components.students.service as student
import components.classes.service as classes
from lab_7.utils.safe_int_input import safe_int_input


def students_menu():
    print("База данных учеников.\n"
          "Возможные действия\n"
          "1. Создать ученика\n"
          "2. Показать всех учеников\n"
          "3. Найти ученика по id\n"
          "4. Редактировать ученика\n"
          "5. Удалить ученика\n")
    action_number = safe_int_input("Выберите действие: ")
    if action_number == 1:
        create_student()
    elif action_number == 2:
        show_all_students()
    elif action_number == 3:
        find_student()
    elif action_number == 4:
        update_student()
    elif action_number == 5:
        delete_student()


def create_student():
    full_name = input("Введите ФИО ученика: ")
    age = safe_int_input("Введите возраст ученика: ")
    clas = find_class()
    student.create_one({"name": full_name, "age": age, "class_id": clas["id"]})


def find_class():
    while True:
        class_id = safe_int_input("Введите id класса ученика: ")
        clas = classes.get_one_by_id(class_id)
        if clas:
            return clas

def show_all_students():
    students = student.get_all()
    for stud in students:
        print_student(stud)


def find_student():
    id = safe_int_input("Введите id ученика: ")
    stud = student.get_one_by_id(id)
    print_student(stud)


def update_student():
    id = safe_int_input("Введите id ученика, данные которого хотите заменить: ")
    stud = student.get_one_by_id(id)
    print("Ученик сейчас:")
    print_student(stud)

    if (input("Обновить имя? (да/нет) ") == "да"):
        stud["name"] = input("Введите новое имя:")
    if (input("Обновить возраст? (да/нет) ") == "да"):
        stud["age"] = safe_int_input("Введите новый возраст:")
    if (input("Обновить класс? (да/нет) ") == "да"):
        clas = find_class()
        stud["class_id"] = clas["id"]

    print("Изменённый ученик: ")
    print_student(stud)
    student.update_one_by_id(id, stud)


def delete_student():
    id = safe_int_input("Введите id ученика, данные которого хотите удалить: ")
    student.delete_one_by_id(id)


def print_student(stud):
    print(f"{stud['id']}. {stud['name']} {stud['age']} лет, айди класса {stud['class_id']}.")

