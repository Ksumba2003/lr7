import utils.json_service as json_service
import lab_7.components.classes.service as classes

def get_one_by_id(id):
    db = json_service.get_database()

    for elem in db["schools"]:
        if elem["id"] == id:
            return elem

    return {"message": f"Элемент с {id} не найден"}


def get_all():
    db = json_service.get_database()

    return db["schools"]


def update_one_by_id(id, school):
    db = json_service.get_database()

    for i, elem in enumerate(db["schools"]):
        if elem["id"] == id:

            elem["number"] = school["number"]
            elem["address"] = school["address"]

            json_service.set_database(db)
            return elem

    return {"message": f"Элемент с {id} не найден"}


def delete_one_by_id(id):
    db = json_service.get_database()

    for i, elem in enumerate(db["schools"]):
        if elem["id"] == id:
            candidate = db["schools"].pop(i)
            json_service.set_database(db)
            update_ids()
            classes.delete_all_by_school_id(candidate["id"])
            return candidate

    return {"message": f"Элемент с {id} не найден"}


def update_ids():
    db = json_service.get_database()
    for i, elem in enumerate(db["schools"]):
        elem["id"] = i + 1
    json_service.set_database(db)


def create_one(school):
    db = json_service.get_database()

    schools = get_all()
    if len(schools) == 0:
        last_school_id = 0
    else:
        last_school_id = schools[-1]["id"]
    db["schools"].append({"id": last_school_id + 1, **school})

    json_service.set_database(db)
