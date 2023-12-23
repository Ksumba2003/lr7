import utils.json_service as json_service
import lab_7.components.students.service as students


def get_one_by_id(id):
    db = json_service.get_database()

    for elem in db["classes"]:
        if elem["id"] == id:
            return elem

    return {"message": f"Элемент с {id} не найден"}


def get_all():
    db = json_service.get_database()

    return db["classes"]


def update_one_by_id(id, clas):
    db = json_service.get_database()

    for i, elem in enumerate(db["classes"]):
        if elem["id"] == id:

            elem["year"] = clas["year"]
            elem["letter"] = clas["letter"]

            json_service.set_database(db)
            return elem

    return {"message": f"Элемент с {id} не найден"}


def delete_one_by_id(id):
    db = json_service.get_database()

    for i, elem in enumerate(db["classes"]):
        if elem["id"] == id:

            candidate = db["classes"].pop(i)
            json_service.set_database(db)
            update_ids()
            students.delete_all_by_class_id(id)

            return candidate

    return {"message": f"Элемент с {id} не найден"}


def delete_all_by_school_id():
    db = json_service.get_database()

    for i, elem in enumerate(db["classes"]):
        if elem["school_id"] == id:
            candidate = db["classes"].pop(i)
            json_service.set_database(db)
            students.delete_all_by_class_id(candidate["id"])
    update_ids()


def delete_all_by_teacher_id():
    db = json_service.get_database()

    for i, elem in enumerate(db["classes"]):
        if elem["teacher_id"] == id:
            candidate = db["classes"].pop(i)
            json_service.set_database(db)
            students.delete_all_by_class_id(candidate["id"])
    update_ids()


def update_ids():
    db = json_service.get_database()
    for i, elem in enumerate(db["classes"]):
        elem["id"] = i + 1
    json_service.set_database(db)


def create_one(clas):
    db = json_service.get_database()

    classes = get_all()
    if len(classes) == 0:
        last_clas_id = 0
    else:
        last_clas_id = classes[-1]["id"]
    db["classes"].append({"id": last_clas_id + 1, **clas})

    json_service.set_database(db)
