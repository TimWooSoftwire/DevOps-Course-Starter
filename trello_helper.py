import requests
import secrets
import constants as c
import Item

_DEFAULT_ITEMS = [
    { 'id': 1, 'status': 'Not Started', 'title': 'List saved todo items' },
    { 'id': 2, 'status': 'Not Started', 'title': 'Allow new items to be added' }
]

def get_items():
    """
    Fetches all saved items from the session.

    Returns:
        list: The list of saved items.
    """
    r = requests.get(c.BASE_API_URL + "boards/" + c.BOARD_ID + "/cards", params=c.DEFAULT_PAYLOAD)
    return parse_cards(r)

def parse_cards(raw_request):
    cards_as_json = raw_request.json()
    card_list = []
    for card in cards_as_json:
        card_list.append(parse_card(card))

    return card_list

def parse_card(card):
    return Item.Item(card['id'], card['idList'], card['name'])
    # return {'id': card['id'], 'status': list_id_to_list_friendly_name(card['idList']), 'title': card['name']}

def add_item(name):
    request_payload = {**c.DEFAULT_PAYLOAD, **{'idList': c.TODO_LIST_ID, 'name': name}} # ** is weird dictionary concat syntax
    requests.post(c.BASE_API_URL + "cards", params=request_payload) 
    return name

def delete_item(id):
    requests.delete(c.BASE_API_URL + "cards/" + id, params = c.DEFAULT_PAYLOAD)
    return id

def complete_item(id):
    request_payload = {**c.DEFAULT_PAYLOAD, **{'idList': c.DONE_LIST_ID}}
    requests.put(c.BASE_API_URL + "cards/" + id, params=request_payload) 
    return id


