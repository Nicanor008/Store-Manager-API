def get_single_item(key, attribute, record):
    result = list(filter(lambda obj: obj[key] == attribute, record))
    if result:
        return result[0]
    else:
        return {"message": "{} does not exist in the records".format(key)}


def get_all_items(records):
    if not records:
        return {"message": "No {} in the records.".format(records)}
    else:
        return records