from datetime import datetime
class ViewModel:
    def __init__(self, items):
        self._items = items

    @property
    def items(self):
        return self._items

    @property
    def items_in_done(self):
        return [item for item in self._items if item.status == "Done"]

    @property
    def items_in_doing(self):
        return [item for item in self._items if item.status == "Doing"]

    @property
    def items_in_todo(self):
        return [item for item in self._items if item.status == "Todo"]

    @property
    def show_all_done_items(self):
        return len(self.items_in_done) < 5 

    @property
    def recent_done_items(self):
        return [item for item in self.items_in_done if item.date_moved.date() == datetime.today().date()]

    @property
    def older_done_items(self):
        return [item for item in self.items_in_done if item.date_moved.date() != datetime.today().date()]

    