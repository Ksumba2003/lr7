from lab_7.classes_menu import classes_menu

from lab_7.schools_menu import schools_menu
from lab_7.students_menu import students_menu
from lab_7.teachers_menu import teachers_menu
from lab_7.utils.safe_int_input import safe_int_input


def main():
    while True:
        print("Здравствуйте!\n"
              "Список существующих баз данных:\n"
              "1. Ученики\n"
              "2. Школы\n"
              "3. Учителя\n"
              "4. Классы\n")
        db_number = safe_int_input("Выберите базу данных для работы: ")
        if db_number == 1:
            students_menu()
        elif db_number == 2:
            schools_menu()
        elif db_number == 3:
            teachers_menu()
        elif db_number == 4:
            classes_menu()


if __name__ == "__main__":
    main()
