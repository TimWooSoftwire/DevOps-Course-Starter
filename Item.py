import constants

class Item:
    def __init__(self, id, listId, name):
        self.id = id
        self.status = list_id_to_list_friendly_name(listId)
        self.name = name

def list_id_to_list_friendly_name(list_id):
    if list_id == constants._TODO_LIST_ID:
        return "Not Started"
    if list_id == constants._DONE_LIST_ID:
        return "Complete"
