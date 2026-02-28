from typing import Text
from textual.widgets import TabbedContent, TabPane, SelectionList, Input, Label
from textual.content import ContentType
from SearchBar import SearchBar
from textual.widgets.selection_list import Selection
from textual import on
from textual.reactive import reactive
from SearchableSelectionList import SearchableSelectionList
from Projects import data as projects_data, bundles as bundles_data


class SelectionCatalog(TabbedContent):
    BORDER_TITLE = "Выбор"
    
    query: reactive[str] = reactive("")

    selections: list[Selection] = [Selection(project["name"], project_id) for project_id, project in projects_data.items()]
    bundle_selections: list[Selection] = [Selection(bundle["name"], bundle_id) for bundle_id, bundle in bundles_data.items()]
    
    def on_mount(self) -> None:
        filtered_selections = [s for s in self.selections if self.query in s.prompt.plain.lower()]
        
        projects_list = SearchableSelectionList(
            id="select-items",
            *filtered_selections
        )
        
        projects_list.data_bind(SelectionCatalog.query)
        projects_list.focus()

        self.add_pane(
            TabPane("Репозитории", SearchBar(), projects_list, id="projects"),
        )

        bundles_list = SelectionList(
           id="select-bundles",
           *self.bundle_selections 
        )

        self.add_pane(
            TabPane("Проекты", bundles_list, id="bundles")
        )

    @on(Input.Changed)
    def apply_search(self, event: Input.Changed) -> None:
        search_term = event.value.lower()
        self.query = search_term
            