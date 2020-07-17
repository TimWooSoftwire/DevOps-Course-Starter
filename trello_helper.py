import requests
import constants as c
from TodoItem import TodoItem

def parse_cards(raw_request):
    cards_as_json = raw_request.json()
    card_list = [TodoItem.parse_card(card) for card in cards_as_json]
    return card_list

class TrelloAPI:
    @staticmethod
    def get_items():
        r = requests.get(f"{c.BASE_API_URL}/boards/{c.BOARD_ID}/cards", params=c.DEFAULT_PAYLOAD)
        return parse_cards(r)

    @staticmethod
    def add_item(name):
        request_payload = { 'idList': c.TODO_LIST_ID, 'name': name, **c.DEFAULT_PAYLOAD} 
        requests.post(f"{c.BASE_API_URL}/cards", params=request_payload) 
        return name

    @staticmethod
    def delete_item(id):
        requests.delete(f"{c.BASE_API_URL}/cards/{id}", params = c.DEFAULT_PAYLOAD)
        return id

    @staticmethod
    def Move_item_to_done(id):
        request_payload = {**c.DEFAULT_PAYLOAD, **{'idList': c.DONE_LIST_ID}}
        requests.put(f"{c.BASE_API_URL}/cards/{id}", params=request_payload) 
        return id

    @staticmethod
    def move_item_to_doing(id):
        request_payload = {**c.DEFAULT_PAYLOAD, **{'idList': c.DOING_LIST_ID}}
        requests.put(f"{c.BASE_API_URL}/cards/{id}", params=request_payload) 
        return id