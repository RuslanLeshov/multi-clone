from textual.widgets.selection_list import Selection
from textual.widgets import SelectionList
from textual.reactive import reactive
from textual.widgets.selection_list import SelectionType
from textual import log, on

class SearchableSelectionList(SelectionList[int]):
    query: reactive[str] = reactive("")
    

    def __init__(self, *options: Selection[int], **kwargs):
        super().__init__(*options, **kwargs)
        self.full_options = [self._make_selection(selection) for selection in options]
        
        
    def watch_query(self, query: str) -> None:
        
        filtered_options = [option for option in self.full_options if query in option.prompt.plain.lower()]
        
        options = [self._make_selection(selection) for selection in filtered_options]
        self._values: dict[SelectionType, int] = {
            option.value: index for index, option in enumerate(options)
        }
        self._options = options
        log.info(f"Updated options: {self._options}")
        log.info(f"Full options: {self.full_options}") 
        
        if options:
            self.highlighted = 0
        else:
            self.highlighted = None
        self.watch_highlighted(self.highlighted)
        self.refresh()
    
    @on(SelectionList.SelectedChanged)
    def change_selection(self, event: SelectionList.SelectedChanged) -> None:
        log.info(f"selected: {self.selected}")