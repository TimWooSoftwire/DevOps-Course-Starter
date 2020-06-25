import requests
import secrets

_DEFAULT_ITEMS = [
    { 'id': 1, 'status': 'Not Started', 'title': 'List saved todo items' },
    { 'id': 2, 'status': 'Not Started', 'title': 'Allow new items to be added' }
]

_BASE_API_URL = "https://api.trello.com/1/"
_DEFAULT_PAYLOAD = {'key': secrets.trello_key , 'token': secrets.trello_token}
_BOARD_ID = "5ef48df22d51c825656d5f8c"
_TODO_LIST_ID = "5ef48eae04ceb72b492830ef"
_DONE_LIST_ID = "5ef48eb03da6260d87a4e9ab"

def get_items():
    """
    Fetches all saved items from the session.

    Returns:
        list: The list of saved items.
    """
    r = requests.get(_BASE_API_URL + "boards/" + _BOARD_ID + "/cards", params=_DEFAULT_PAYLOAD)
    return parse_cards(r)

def parse_cards(raw_request):
    cards_as_json = raw_request.json()
    card_list = []
    for card in cards_as_json:
        card_list.append(parse_card(card))

    return card_list

def parse_card(card):
    return {'id': card['id'], 'status': list_id_to_list_friendly_name(card['idList']), 'title': card['name']}

def list_id_to_list_friendly_name(list_id):
    if list_id == _TODO_LIST_ID:
        return "Not Started"
    if list_id == _DONE_LIST_ID:
        return "Complete"

def add_item(name):
    request_payload = {**_DEFAULT_PAYLOAD, **{'idList': _TODO_LIST_ID, 'name': name}} # ** is weird dictionary concat syntax
    requests.post(_BASE_API_URL + "cards", params=request_payload) 
    return name

def delete_item(id):
    requests.delete(_BASE_API_URL + "cards/" + id, params = _DEFAULT_PAYLOAD)
    return id

def complete_item(id):
    request_payload = {**_DEFAULT_PAYLOAD, **{'idList': _DONE_LIST_ID}}
    requests.put(_BASE_API_URL + "cards/" + id, params=request_payload) 
    return id


