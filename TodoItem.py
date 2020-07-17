import constants

class TodoItem:
    def __init__(self, id, listId, name):
        self.id = id
        self.status = list_id_to_list_friendly_name(listId)
        self.name = name

    @classmethod
    def parse_card(cls, card):
       return cls(card['id'], card['idList'], card['name'])

def list_id_to_list_friendly_name(list_id):
    if list_id == constants.TODO_LIST_ID:
        return "Todo"
    if list_id == constants.DOING_LIST_ID:
        return "Doing"
    if list_id == constants.DONE_LIST_ID:
        return "Done"

