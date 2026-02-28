from textual.fuzzy import FuzzySearch
from textual.widgets import Input

class SearchBar(Input):
    
    def on_mount(self) -> None:
        self.placeholder = "Поиск..."
  