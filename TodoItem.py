import constants
import dateutil.parser


class TodoItem:
    def __init__(self, id, list_id, name, date_moved):
        self.id = id
        self.status = list_id_to_list_friendly_name(list_id)
        self.name = name
        self.date_moved = dateutil.parser.parse(date_moved)

    @classmethod
    def parse_card(cls, card):
        return cls(card['id'], card['idList'], card['name'], card['dateLastActivity'])


def list_id_to_list_friendly_name(list_id):
    if list_id == constants.TODO_LIST_ID:
        return "Todo"
    if list_id == constants.DOING_LIST_ID:
        return "Doing"
    if list_id == constants.DONE_LIST_ID:
        return "Done"
