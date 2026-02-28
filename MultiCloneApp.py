from textual.app import App, ComposeResult
from textual.widgets import Static, Footer, Header, Label, TabbedContent
from textual.containers import Horizontal, Vertical, Container
from SelectionCatalog import SelectionCatalog
from SelectedListPanel import SelectedListPanel
from DetailsPanel import DetailsPanel
from textual.widgets import SelectionList
from textual import on
from textual.events import Mount


class MultiCloneApp(App):

    BINDINGS = [
        ("q", "quit", "Выход"),
    ]

    TITLE = "MultiClone"
    SUB_TITLE = "multiple git repositories cloner"
    CSS_PATH = "MultiClone.tcss"

    def compose(self) -> ComposeResult:
        yield Header()
        with Horizontal():
            yield SelectionCatalog()
            with Vertical():
                yield DetailsPanel()
                yield SelectedListPanel()

        yield Footer()

    @on(Mount)
    @on(SelectionList.SelectionHighlighted)
    @on(TabbedContent.TabActivated)
    def update_selection_details(self):
        active_tab = self.query_one(TabbedContent).active_pane
        selected_list = active_tab.query_one(SelectionList)

        if not selected_list:
            return
        
        selected_row = selected_list.highlighted_option.value

        self.query_one(DetailsPanel).update_details(selected_list.id, selected_row)

    @on(SelectionList.SelectedChanged)
    @on(TabbedContent.TabActivated)
    def update_selection_list_details(self):
        active_tab = self.query_one(TabbedContent).active_pane
        selected_list = active_tab.query_one(SelectionList)

        if not selected_list:
            return
        selected_ids = selected_list.selected
        selected_rows = [option.prompt.plain for option in selected_list.options if option.value in selected_ids]

        self.query_one(SelectedListPanel).update_details(selected_rows)
    
    



if __name__ == "__main__":
    app = MultiCloneApp()
    app.run()
