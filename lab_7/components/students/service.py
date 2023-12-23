import utils.json_service as json_service


def get_one_by_id(id):
    db = json_service.get_database()

    for elem in db["students"]:
        if elem["id"] == id:
            return elem

    return {"message": f"Элемент с {id} не найден"}


def get_all():
    db = json_service.get_database()

    return db["students"]


def update_one_by_id(id, student):
    db = json_service.get_database()

    for i, elem in enumerate(db["students"]):
        if elem["id"] == id:

            elem["name"] = student["name"]
            elem["age"] = student["age"]
            elem["grade"] = student["grade"]

            json_service.set_database(db)
            return elem

    return {"message": f"Элемент с {id} не найден"}


def delete_one_by_id(id):
    db = json_service.get_database()

    for i, elem in enumerate(db["students"]):
        if elem["id"] == id:

            candidate = db["students"].pop(i)
            json_service.set_database(db)
            update_ids()
            return candidate

    return {"message": f"Элемент с {id} не найден"}


def update_ids():
    db = json_service.get_database()
    for i, elem in enumerate(db["students"]):
        elem["id"] = i + 1
    json_service.set_database(db)


def delete_all_by_class_id():
    db = json_service.get_database()

    for i, elem in enumerate(db["students"]):
        if elem["class_id"] == id:
            candidate = db["students"].pop(i)
            json_service.set_database(db)
            update_ids()
            return candidate


def create_one(student):
    db = json_service.get_database()

    students = get_all()
    if len(students) == 0:
        last_student_id = 0
    else:
        last_student_id = students[-1]["id"]
    db["students"].append({"id": last_student_id + 1, **student})

    json_service.set_database(db)
