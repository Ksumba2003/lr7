import utils.json_service as json_service
import lab_7.components.classes.service as classes


def get_one_by_id(id):
    db = json_service.get_database()

    for elem in db["teachers"]:
        if elem["id"] == id:
            return elem

    return {"message": f"Элемент с {id} не найден"}


def get_all():
    db = json_service.get_database()

    return db["teachers"]


def update_one_by_id(id, teacher):
    db = json_service.get_database()

    for i, elem in enumerate(db["teachers"]):
        if elem["id"] == id:

            elem["name"] = teacher["name"]
            elem["phone_number"] = teacher["phone_number"]

            json_service.set_database(db)
            return elem

    return {"message": f"Элемент с {id} не найден"}


def delete_one_by_id(id):
    db = json_service.get_database()

    for i, elem in enumerate(db["teachers"]):
        if elem["id"] == id:

            candidate = db["teachers"].pop(i)
            json_service.set_database(db)
            classes.delete_all_by_school_id(candidate["id"])

            return candidate

    return {"message": f"Элемент с {id} не найден"}


def update_ids():
    db = json_service.get_database()
    for i, elem in enumerate(db["teachers"]):
        elem["id"] = i + 1
    json_service.set_database(db)


def create_one(teacher):
    db = json_service.get_database()

    teachers = get_all()
    if len(teachers) == 0:
        last_teacher_id = 0
    else:
        last_teacher_id = teachers[-1]["id"]
    db["teachers"].append({"id": last_teacher_id + 1, **teacher})

    json_service.set_database(db)
